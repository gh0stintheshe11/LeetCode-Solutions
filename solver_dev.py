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

# load the setting.json file
with open("setting.json", "r") as f:
    SETTING = json.load(f)

BASE_URL = "https://leetcode.com"
# load the .env file
load_dotenv()
# set up openai client
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# format the header
def get_common_header(suffix):
    return {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36",
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
def list_questions(limit, start):
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
                status
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
        # To this
        codeSnippets = {
            snippet["lang"]: {"langSlug": snippet["langSlug"], "code": snippet["code"]}
            for snippet in codeSnippets
        }

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
        "question_id": str(question_id),
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
                sleep_time = 2**attempt  # Exponential backoff
                time.sleep(sleep_time)
            else:
                print(
                    f"Unexpected state: {result['state']}, Message: {result['status_msg']}"
                )
                raise Exception(f"Unexpected submission state: {result}")
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
                sleep_time = 2**attempt  # Exponential backoff
                time.sleep(sleep_time)
            else:
                print(
                    f"Unexpected state: {result['state']}, Message: {result['status_msg']}"
                )
                raise Exception(f"Unexpected submission state: {result}")
        except JSONDecodeError:
            print(f"Failed to decode JSON on attempt {attempt + 1}. Retrying...")
        except KeyError:
            print(f"Unexpected response format on attempt {attempt + 1}. Retrying...")

    raise Exception("Timed out waiting for submission result")


# generate the solution using GPT model
def generate(language, question):

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
    return extract_code(codeblock)


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
def debug(language, question, current_code, submit_result):

    # get the codeSnippets from the question and get the rest
    codeSnippet = question.pop("codeSnippets")[language]

    # Create the prompt for debugging
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
We encountered an error while solving a LeetCode problem in Python.

- **Solution must be written in {language}**
- **Class and function definitions** must match the ones provided.
- Return **only the solution code**—no explanations, comments, or additional text.

### Problem:

```json
{question}
```

### Current Code:

```python
{current_code}
```

### Error Encountered:

```json
{submit_result}
```

### Task:
Please review the problem, the current code, and the error. Then generate a new solution that avoids the issue causing the error.

### Provided Code:

```python
{codeSnippet}
```
""",
            },
        ],
    )

    # Extract the generated code from the response
    codeblock = response.choices[0].message.content
    return extract_code(codeblock)


# get the next unsolved question
def get_next_unsolved(question_id):
    current_question_id = int(question_id)
    max_iterations = 1000  # Safeguard against infinite loop

    for _ in range(max_iterations):
        questions = list_questions(limit=50, start=current_question_id + 1)

        if not questions:
            return None  # No more questions available

        for question in questions:
            current_question_id = int(question["questionId"])
            if question["status"] != "ac":
                return question

        # If we've checked all questions in this batch and none are unsolved,
        # we'll move to the next batch in the next iteration
        
    return None  # Couldn't find an unsolved question within the limit

# main logic of the solver
def solver():
    print("--- Solver Start ---")

    current_question_id = SETTING["start_question"]  # default language
    language = SETTING["default_language"]  # default language

    while True:  # Outer loop to continuously solve problems
        # get the next unsolved question -> get question details
        question = get_next_unsolved(current_question_id)
        if not question:
            print("No more unsolved questions found. Exiting.")
            break

        current_question_id = int(question["questionId"])
        print(f"Next unsolved question: {question}")

        # get the question details
        question_detailed = get_question_details(question["titleSlug"])
        print(f"Get question details: {question_detailed}")

        # check if the language selected is in the codeSnippets
        if language not in question_detailed["codeSnippets"]:
            # change language to the first available language
            language = list(question_detailed["codeSnippets"].keys())[0]

        # generate initial solution
        solution = generate(language, question_detailed)
        print(f"Generated initial solution: {solution}")
        
        # leetcode api takes the langSlug instead of the language name
        langSlug = question_detailed["codeSnippets"][language]["langSlug"]

        max_submit_attempts = 3
        for submit_attempt in range(max_submit_attempts):
            # Test the solution
            test_result = test(
                question_detailed["question_id"],
                question_detailed["problem_slug"],
                langSlug,
                solution,
                question_detailed["exampleTestcases"],
            )

            max_debug_attempts = 3
            while test_result["status_msg"] != "Accepted" and max_debug_attempts > 0:
                # Debug the solution
                solution = debug(question_detailed, solution, test_result)

                # Run the test again
                test_result = test(
                    question_detailed["question_id"],
                    question_detailed["problem_slug"],
                    langSlug,
                    solution,
                    question_detailed["exampleTestcases"],
                )

                max_debug_attempts -= 1

            if test_result["status_msg"] == "Accepted":
                # If all test cases pass, submit the solution
                submit_result = submit(
                    question_detailed["question_id"],
                    question_detailed["problem_slug"],
                    langSlug,
                    solution,
                )
                print(f"Submitted solution: {submit_result}")

                if submit_result["status_msg"] == "Accepted":
                    print("Solution accepted!")
                    break  # Break out of the submit_attempt loop
                else:
                    print(f"Solution failed: {submit_result}")
                    # Add the failed test case to our test cases
                    question_detailed["exampleTestcases"].append(
                        submit_result["last_testcase"]
                    )
            else:
                print(
                    f"Failed to pass all test cases after {max_debug_attempts} debug attempts"
                )
                break  # Break out of the submit_attempt loop

        if submit_attempt == max_submit_attempts - 1:
            print(
                f"Failed to solve the question after {max_submit_attempts} submit attempts"
            )

        # Move to the next question
        current_question_id += 1
        print("Moving to next question...")
        
        


if __name__ == "__main__":

    # COOKIES = login_to_leetcode()
    COOKIES = {
        "_ga": "GA1.2.379898781.1727049186",
        "LEETCODE_SESSION": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJfYXV0aF91c2VyX2lkIjoiMTI2NzA5MjgiLCJfYXV0aF91c2VyX2JhY2tlbmQiOiJhbGxhdXRoLmFjY291bnQuYXV0aF9iYWNrZW5kcy5BdXRoZW50aWNhdGlvbkJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiI5NTBhZjMyNmYyMjc0NDE4OGIwZTJlYmQyMTk3ZWQzYzAyMmU4NWIxMTZjNDc2MzJlYjM0Yzk4M2VmZWZiNTFlIiwiaWQiOjEyNjcwOTI4LCJlbWFpbCI6ImxhbmdzLjk3MTEwNEBnbWFpbC5jb20iLCJ1c2VybmFtZSI6ImdoMHN0aW50aGVzaGUxMSIsInVzZXJfc2x1ZyI6ImdoMHN0aW50aGVzaGUxMSIsImF2YXRhciI6Imh0dHBzOi8vYXNzZXRzLmxlZXRjb2RlLmNvbS91c2Vycy9naDBzdGludGhlc2hlMTEvYXZhdGFyXzE3MTAyMDQyNjQucG5nIiwicmVmcmVzaGVkX2F0IjoxNzI3MDQ5MjAxLCJpcCI6IjE0Mi4xOTguMjE0LjE0MiIsImlkZW50aXR5IjoiMDk5OTNhYjg2OGY0NzBjZjI0ZTI2ZmE0Zjk0MzlkOWUiLCJzZXNzaW9uX2lkIjo3MzE5NTcyMX0.GYp-hdd3CZ-rpl8Fp4MCH9gFS-UEN4dLwIM9RcO3GOg",
        "gr_user_id": "1a16cc2e-88e9-4ec6-bf75-5ccc71d79065",
        "csrftoken": "A1HG38DLLl5M8AC0YCX3OETfUdztmhBvxlPNSazwLJ6nGbnNAbCSvbULFadYAE4V",
        "_ga_CDRWKZTDEX": "GS1.1.1727049185.1.1.1727049202.43.0.0",
        "_dd_s": "rum=0&expire=1727050089759",
        "87b5a3c3f1a55520_gr_session_id_sent_vst": "f400fcfc-6217-4b38-b3cb-606601aa9c8a",
        "ip_check": '(false, "142.198.214.142")',
        "87b5a3c3f1a55520_gr_session_id": "f400fcfc-6217-4b38-b3cb-606601aa9c8a",
        "messages": "W1siX19qc29uX21lc3NhZ2UiLDAsMjUsIlN1Y2Nlc3NmdWxseSBzaWduZWQgaW4gYXMgZ2gwc3RpbnRoZXNoZTExLiJdXQ:1ssWOH:qf2Naev9fwvUojTdLdlJ0OQX5H2zRdBLA6ZB9QSoAKU",
        "_gat": "1",
        "_gid": "GA1.2.18430705.1727049186",
        "__cf_bm": "vLgURSKvtXUsH9F6bbaex7rmFS0khCuJ3bLl9YlEWR4-1727049185-1.0.1.1-hZ5q8HgQ5Mj8cju5mGNnEV.b5vYt93l7Clgv9YKOtIqJwAklznYRKq_FHtzAGG4JOVfelf1NLOvzMApYBL9OIw",
    }

    language = "Python3"
    question = get_question_details("maximum-subarray")
    langSlug = question["codeSnippets"][language]["langSlug"]
    solution = open("solution.txt", "r").read()

    result = test(
        question["question_id"],
        question["problem_slug"],
        langSlug,
        solution,
        question["exampleTestcases"],
    )
    print(result)
