import time
import undetected_chromedriver as uc
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import (
    TimeoutException,
    ElementClickInterceptedException,
)
from requests.exceptions import JSONDecodeError
import requests
import json
import os
from dotenv import load_dotenv
from bs4 import BeautifulSoup

BASE_URL = "https://leetcode.com"


def get_common_headers(suffix):
    return {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
        "Referer": f"{BASE_URL}/{suffix}",
        "Content-Type": "application/json",
        "X-CSRFToken": COOKIES.get("csrftoken", ""),
        "X-Requested-With": "XMLHttpRequest",
    }


# load the solution.txt file
with open("solution.txt", "r") as file:
    SOLUTION = file.read()


def login_to_leetcode():
    print("Initializing WebDriver...")
    driver = webdriver.Chrome()
    wait = WebDriverWait(driver, 30)

    # load the .env file
    load_dotenv()
    # get the github username and password from the .env file
    LEETCODE_USERNAME = os.getenv("LEETCODE_USERNAME")
    LEETCODE_PASSWORD = os.getenv("LEETCODE_PASSWORD")

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

        driver.find_element(By.ID, "login_field").send_keys(LEETCODE_USERNAME)
        driver.find_element(By.ID, "password").send_keys(LEETCODE_PASSWORD)

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
        headers=get_common_headers(""),
        cookies=COOKIES,
    )
    response.raise_for_status()  # Raise an exception for bad status codes

    data = response.json()
    questions = data["data"]["problemsetQuestionList"]["questions"]

    return questions


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
        headers=get_common_headers(""),
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
        return (
            question_id,
            problem_slug,
            problem_title,
            content,
            hints,
            exampleTestcases,
            codeSnippets,
        )
    else:
        raise Exception(f"Failed to get question details: {response.status_code}")


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
            headers=get_common_headers(f"problems/{problem_slug}/"),
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
                headers=get_common_headers(f"problems/{problem_slug}/"),
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


# test solution
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
        headers=get_common_headers(f"problems/{problem_slug}/"),
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
                headers=get_common_headers(f"problems/{problem_slug}/"),
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

    try:
        # get the question details
        (
            question_id,
            problem_slug,
            problem_title,
            content,
            hints,
            exampleTestcases,
            codeSnippets,
        ) = get_question_details("subsequence-of-size-k-with-the-largest-even-sum")
        print(
            question_id, problem_slug, problem_title, content, hints, exampleTestcases
        )

        # list all questions
        # questions = list_questions(limit=10, start=2000)
        # print(questions)

        # submit_result = submit(question_id, problem_slug, 'c', SOLUTION)
        # print(submit_result)

        test_result = test(question_id, problem_slug, 'c', SOLUTION, exampleTestcases)
        print(test_result)

    except requests.exceptions.HTTPError as e:
        print(f"HTTP Error occurred: {e}")
        print(f"Response content: {e.response.content}")
