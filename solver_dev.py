import re
import os
import time
import json
import requests
from requests.exceptions import JSONDecodeError
from dotenv import load_dotenv
from bs4 import BeautifulSoup
from openai import OpenAI
import undetected_chromedriver as uc
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import (
    TimeoutException,
    ElementClickInterceptedException,
)

BASE_URL = "https://leetcode.com"
# load the .env file
load_dotenv()


# format the header
def get_common_header(suffix):
    return {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
        "Referer": f"{BASE_URL}/{suffix}",
        "Content-Type": "application/json",
        "X-CSRFToken": COOKIES.get("csrftoken", ""),
        "X-Requested-With": "XMLHttpRequest",
    }


# login to the leetcode -> since leetcode use CAPTCHA, we need to use 3rd party login to wrok around that
def login_to_leetcode():
    print("Initializing WebDriver...")
    driver = webdriver.Chrome()
    wait = WebDriverWait(driver, 30)

    try:
        print("Navigating to LeetCode login page...")
        driver.get(f"{BASE_URL}/accounts/login/")

        # Wait for the loading overlay to disappear
        try:
            wait.until(EC.invisibility_of_element_located((By.ID, "initial-loading")))
        except TimeoutException:
            print("Loading overlay did not disappear. Attempting to continue...")

        # Wait for and click GitHub login button
        max_attempts = 3
        for attempt in range(max_attempts):
            try:
                github_login_button = wait.until(
                    EC.element_to_be_clickable(
                        (By.CSS_SELECTOR, 'a[href*="github/login"]')
                    )
                )
                github_login_button.click()
                break
            except (TimeoutException, ElementClickInterceptedException) as e:
                if attempt < max_attempts - 1:
                    print(f"Attempt {attempt + 1} failed. Retrying in 5 seconds...")
                    time.sleep(5)
                else:
                    print(
                        "Failed to click GitHub login button after multiple attempts."
                    )
                    raise e

        # Wait for the "Continue" button on GitHub authorization page and click it
        print("Waiting for Continue button...")
        try:
            continue_button = wait.until(
                EC.element_to_be_clickable(
                    (By.XPATH, '//div[@id="base_content"]//button[text()="Continue"]')
                )
            )
            continue_button.click()
            print("Clicked Continue button.")
        except TimeoutException:
            print("Continue button not found. Please check the page manually.")
            input(
                "Press Enter after manually clicking Continue or if you need to proceed..."
            )

        # Wait for GitHub login page to load
        print("Waiting for GitHub login page to load...")
        wait.until(EC.presence_of_element_located((By.ID, "login_field")))

        driver.find_element(By.ID, "login_field").send_keys(
            os.getenv("LEETCODE_USERNAME")
        )
        driver.find_element(By.ID, "password").send_keys(os.getenv("LEETCODE_PASSWORD"))

        # Click Sign in button
        sign_in_button = wait.until(
            EC.element_to_be_clickable(
                (By.CSS_SELECTOR, 'input[type="submit"][value="Sign in"]')
            )
        )
        sign_in_button.click()

        # Wait for login to complete
        wait.until(EC.url_contains(f"{BASE_URL}/"))
        print("Login successful.")

        # Get all cookies
        cookies = driver.get_cookies()
        cookie_dict = {cookie["name"]: cookie["value"] for cookie in cookies}

        return cookie_dict

    finally:
        driver.quit()


# list certain amount of questions
def list_questions(limit=0, start=0):
    url = f"{BASE_URL}/graphql"
    query = """
    query problemsetQuestionList($categorySlug: String, $limit: Int, $skip: Int, $filters: QuestionListFilterInput) {
        problemsetQuestionList: questionList(
            categorySlug: $categorySlug
            limit: $limit
            skip: $skip
            filters: $filters
        ) {
            total: totalNum
            questions: data {
                questionId
                titleSlug
                difficulty
                isPaidOnly
                acRate
            }
        }
    }
    """

    variables = {
        "categorySlug": "",
        "skip": start,
        "limit": (
            limit if limit > 0 else 100000
        ),  # Use a large number to get all questions if limit is 0
        "filters": {},
    }

    response = requests.post(
        url,
        json={"query": query, "variables": variables},
        headers=get_common_header(""),
        cookies=COOKIES,
    )
    response.raise_for_status()  # Raise an exception for bad status codes

    data = response.json()
    questions = data["data"]["problemsetQuestionList"]["questions"]

    return questions


# get the detailed info of the selected question
def get_question_details(problem_slug):
    url = f"{BASE_URL}/graphql"
    query = f"""
    query getQuestionDetail($titleSlug: String!) {{
        question(titleSlug: $titleSlug) {{
            questionId
            title
            content
            hints
            exampleTestcases
            codeSnippets {{
                lang
                langSlug
                code
            }}
        }}
    }}
    """

    variables = {"titleSlug": problem_slug}

    response = requests.post(
        url,
        json={"query": query, "variables": variables},
        headers=get_common_header(""),
        cookies=COOKIES,
    )
    response.raise_for_status()  # Raise an exception for bad status codes

    if response.status_code == 200:
        questions = response.json()["data"]["question"]
        # get the question id
        question_id = questions["questionId"]
        # get the problem title
        problem_title = questions["title"]
        # get the content
        content = questions["content"]
        # chnage the content from html to markdown for better processing
        content = BeautifulSoup(content, "html.parser").get_text()
        # get the hints
        hints = questions["hints"]
        # get the example test cases
        exampleTestcases = questions["exampleTestcases"]
        # get the code snippets
        codeSnippets = questions["codeSnippets"]
        # reformat the codeSnippets to be a dicts with lang as key and code as value
        codeSnippets = {snippet["lang"]: snippet["code"] for snippet in codeSnippets}

        # format question to a json
        question = {
            "question_id": question_id,
            "problem_slug": problem_slug,
            "problem_title": problem_title,
            "content": content,
            "hints": hints,
            "exampleTestcases": exampleTestcases,
            "codeSnippets": codeSnippets,
        }
        return question
    else:
        raise Exception(f"Failed to get question details: {response.status_code}")


# submit the solution, check the submit status
def submit(question_id, problem_slug, lang, code):

    submit_url = f"{BASE_URL}/problems/{problem_slug}/submit/"

    submit_data = {
        "lang": lang,
        "question_id": question_id,
        "typed_code": code,
    }

    # Submit the solution
    try:
        response = requests.post(
            submit_url,
            headers=get_common_header(f"problems/{problem_slug}/"),
            json=submit_data,
            cookies=COOKIES,
        )
        response.raise_for_status()
        submission_id = response.json()["submission_id"]
    except JSONDecodeError:
        raise Exception("Failed to decode JSON response from submission")
    except KeyError:
        raise Exception("Submission response does not contain 'submission_id'")

    # Check the result
    submit_status_url = f"{BASE_URL}/submissions/detail/{submission_id}/check/"

    max_attempts = 10
    for attempt in range(max_attempts):
        try:
            response = requests.get(
                submit_status_url,
                headers=get_common_header(f"problems/{problem_slug}/"),
                cookies=COOKIES,
            )
            response.raise_for_status()
            result = response.json()
            if result["state"] == "SUCCESS":
                return result
            elif result["state"] in ["PENDING", "STARTED"]:
                time.sleep(2)  # Wait for 2 seconds before trying again
            else:
                raise Exception(f"Unexpected submission state: {result['state']}")
        except JSONDecodeError:
            print(f"Failed to decode JSON on attempt {attempt + 1}. Retrying...")
        except KeyError:
            print(f"Unexpected response format on attempt {attempt + 1}. Retrying...")

    raise Exception("Timed out waiting for submission result")


# send the test soution, check the test status
def test(question_id, problem_slug, lang, code, test_case):

    test_url = f"{BASE_URL}/problems/{problem_slug}/interpret_solution/"

    data = {
        "question_id": str(question_id),
        "lang": lang,
        "typed_code": code,
        "data_input": test_case,
    }

    response = requests.post(
        test_url,
        headers=get_common_header(f"problems/{problem_slug}/"),
        json=data,
        cookies=COOKIES,
    )
    response.raise_for_status()
    interpret_id = response.json()["interpret_id"]

    # Now, let's check the result
    test_status_url = f"https://leetcode.com/submissions/detail/{interpret_id}/check/"

    max_attempts = 10
    for attempt in range(max_attempts):
        try:
            response = requests.get(
                test_status_url,
                headers=get_common_header(f"problems/{problem_slug}/"),
                cookies=COOKIES,
            )
            response.raise_for_status()
            result = response.json()
            if result["state"] == "SUCCESS":
                return result
            elif result["state"] in ["PENDING", "STARTED"]:
                time.sleep(2)  # Wait for 2 seconds before trying again
            else:
                raise Exception(f"Unexpected submission state: {result['state']}")
        except JSONDecodeError:
            print(f"Failed to decode JSON on attempt {attempt + 1}. Retrying...")
        except KeyError:
            print(f"Unexpected response format on attempt {attempt + 1}. Retrying...")

    raise Exception("Timed out waiting for submission result")


# generate the solution using GPT model
def generate(language, question):

    client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

    # get the codeSnippets from the question and get the rest
    codeSnippets = question.pop("codeSnippets")[language]

    response = client.chat.completions.create(
        model="gpt-4",
        messages=[
            {
                "role": "system",
                "content": "You are a master of solving LeetCode problems and generating solutions.",
            },
            {
                "role": "user",
                "content": f"""
### Instruction:
**Solve this LeetCode problem in Python** using the most efficient approach with optimal time complexity unless specified otherwise. 

- **Solution must be written in {language}**
- **Class and function definitions** must match the ones provided.
- Return **only the solution code**—no explanations, comments, or additional text.

### Problem:

```json
{question}
```

### Provided Code:

```
{codeSnippets}
```
""",
            },
        ],
    )

    codeblock = response.choices[0].message.content
    return codeblock


# extract the code from the markdown code block
def extract_code(markdown_code):
    # Pattern to match code blocks
    pattern = r"```(\w+)?\n(.*?)```"
    matches = re.findall(pattern, markdown_code, re.DOTALL)

    # extract the first code block
    language, code = matches[0]
    # Remove leading/trailing whitespace and any extra newlines
    code = code.strip()
    # Remove common leading whitespace to preserve indentation
    lines = code.split("\n")
    if lines:
        common_indent = len(re.match(r"\s*", lines[0]).group())
        code = "\n".join(line[common_indent:] for line in lines)

    return code


# debug the code if there is an error
def debug(question, code):
    pass # for now


# three cases:
# 1. first-time generate -> solve problme prompt: prompt + question
# 2. few-time generate with bug -> debug prompt: prompt + question + current code + submit result
# 3. no bug  -> next one

if __name__ == "__main__":

    COOKIES = {
        "_ga": "GA1.1.426359378.1726628628",
        "LEETCODE_SESSION": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJfYXV0aF91c2VyX2lkIjoiMTI2NzA5MjgiLCJfYXV0aF91c2VyX2JhY2tlbmQiOiJhbGxhdXRoLmFjY291bnQuYXV0aF9iYWNrZW5kcy5BdXRoZW50aWNhdGlvbkJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiI5NTBhZjMyNmYyMjc0NDE4OGIwZTJlYmQyMTk3ZWQzYzAyMmU4NWIxMTZjNDc2MzJlYjM0Yzk4M2VmZWZiNTFlIiwiaWQiOjEyNjcwOTI4LCJlbWFpbCI6ImxhbmdzLjk3MTEwNEBnbWFpbC5jb20iLCJ1c2VybmFtZSI6ImdoMHN0aW50aGVzaGUxMSIsInVzZXJfc2x1ZyI6ImdoMHN0aW50aGVzaGUxMSIsImF2YXRhciI6Imh0dHBzOi8vYXNzZXRzLmxlZXRjb2RlLmNvbS91c2Vycy9naDBzdGludGhlc2hlMTEvYXZhdGFyXzE3MTAyMDQyNjQucG5nIiwicmVmcmVzaGVkX2F0IjoxNzI2NjI4NjQxLCJpcCI6IjE0Mi4xOTguMjE0LjE0MiIsImlkZW50aXR5IjoiMDk5OTNhYjg2OGY0NzBjZjI0ZTI2ZmE0Zjk0MzlkOWUiLCJzZXNzaW9uX2lkIjo3MjY4MTg0OH0.kIYCkJZPHc_FmxtYYELbJnRfMChc9EgvSpyj1PbyI18",
        "gr_user_id": "c5962b4f-92d1-43f5-b30f-d7dcfd682ea5",
        "csrftoken": "0C1GZxivujOgm3atDkim5HlTFin1SwcNVmTxqjCmHoE9562IAcdWZZDbYK3W2eFD",
        "_ga_CDRWKZTDEX": "GS1.1.1726628628.1.1.1726628641.47.0.0",
        "_dd_s": "rum=0&expire=1726629533220",
        "87b5a3c3f1a55520_gr_session_id_sent_vst": "be00a9cd-708f-4620-a677-2d197e054029",
        "messages": "W1siX19qc29uX21lc3NhZ2UiLDAsMjUsIlN1Y2Nlc3NmdWxseSBzaWduZWQgaW4gYXMgZ2gwc3RpbnRoZXNoZTExLiJdXQ:1sqkz3:jvYNsBAkj6uJr_UtdnHvA8Lg6DrdqleuobW0mUhJYqg",
        "87b5a3c3f1a55520_gr_session_id": "be00a9cd-708f-4620-a677-2d197e054029",
        "ip_check": '(false, "142.198.214.142")',
        "_gat": "1",
        "_gid": "GA1.2.1788959296.1726628628",
        "__cf_bm": "00.U5i7D7reawJrMqmFhbpLxDbdqqp8Wez.rQNUkshg-1726628628-1.0.1.1-5i6wSM1nE8ozWoHF.YMTX1yDQdrzuuGXWdP8Zo1JrhBNWr4gfdqHzIEYPn6YTiw4oGSP_i3u0OMPwJL3SzlpEw",
    }

    language = "Python3"

    try:
        # get the question details
        question = get_question_details(
            "subsequence-of-size-k-with-the-largest-even-sum"
        )

        # list all questions
        # questions = list_questions(limit=10, start=2000)
        # print(questions)

        solution = """
class Solution:
    def largestEvenSum(self, nums, k):
        if k == 1: return max([i for i in nums if i%2==0], default=-1)
        odd, even = sorted([i for i in nums if i%2!=0], reverse=True), sorted([i for i in nums if i%2==0], reverse=True)
        max_sum, p1, p2, count = 0, 0, 0, k
        while count > 0:
            if p1 == len(even): return max_sum + sum(odd[:count]) if count % 2 == 0 else max_sum + sum(odd[:count-1]) if count > 1 else -1
            if p2 + 1 >= len(odd) or count == 1: return max_sum + sum(even[:count])
            if even[p1] > sum(odd[p2:p2+2]): return max_sum + sum(even[:count])
            else: max_sum += sum(odd[p2:p2+2]); count -= 2; p2 += 2
            if count > 0: max_sum += even[p1]; count -= 1; p1 += 1
        return max_sum if max_sum%2==0 else -1

        """
        submit_result = submit(
            question["question_id"], question["problem_slug"], "python3", solution
        )
        print(submit_result)

        # test_result = test(question_id, problem_slug, 'python3', solution, exampleTestcases)
        # print(test_result)

    except requests.exceptions.HTTPError as e:
        print(f"HTTP Error occurred: {e}")
        print(f"Response content: {e.response.content}")
