import re
import os
import time
import json
import requests
from dotenv import load_dotenv
from bs4 import BeautifulSoup
import undetected_chromedriver as uc
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import (
    TimeoutException,
    ElementClickInterceptedException,
)

load_dotenv()

BASE_URL = "https://leetcode.com"

# Define COOKIES at the top to avoid NameError
COOKIES = {}


# format the header
def get_common_header(suffix):
    return {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36",
        "Referer": f"{BASE_URL}/{suffix}",
        "Content-Type": "application/json",
        "X-CSRFToken": COOKIES.get("csrftoken", ""),  # Ensure COOKIES is defined
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
def list_all_solved():
    print("Fetching all solved questions...")
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
        "skip": 0,
        "limit": 10000,  # A large number to fetch all questions
        "filters": {
            "status": "AC"
        },
    }

    response = requests.post(
        url,
        json={"query": query, "variables": variables},
        headers=get_common_header(""),
        cookies=COOKIES,
    )
    response.raise_for_status()

    data = response.json()
    questions = data["data"]["problemsetQuestionList"]["questions"]
    total = data["data"]["problemsetQuestionList"]["total"]
    print(f"{total} solved questions fetched.")

    # Sort questions by ID
    questions.sort(key=lambda q: int(q["questionId"]))

    return questions


# get the detailed info of the selected question
def get_question_details(problem_slug):
    print(f"Fetching question {problem_slug} details...")
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

    if response.status_code != 200:
        print(
            f"Error fetching question details: {response.content}"
        )  # Log response content
        raise Exception(f"Failed to get question details: {response.status_code}")

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


def get_last_accepted_submission(problem_slug):
    url = f"{BASE_URL}/graphql"
    
    query = """
    query submissionList($offset: Int!, $limit: Int!, $lastKey: String, $questionSlug: String!, $lang: Int, $status: Int) {
      questionSubmissionList(
        offset: $offset
        limit: $limit
        lastKey: $lastKey
        questionSlug: $questionSlug
        lang: $lang
        status: $status
      ) {
        lastKey
        hasNext
        submissions {
          id
          title
          titleSlug
          status
          statusDisplay
          lang
          langName
          runtime
          timestamp
          url
          isPending
          memory
          hasNotes
          notes
        }
      }
    }
    """

    variables = {
        "offset": 0,
        "limit": 20,  # Limit to the number of submissions you want to fetch
        "lastKey": None,
        "questionSlug": problem_slug,
        "lang": None,  # You can specify a language or leave it as None
        "status": None  # Leave it as None to fetch all statuses
    }
    
    headers = get_common_header(f"problems/{problem_slug}/submissions/")
    
    response = requests.post(url, headers=headers, cookies=COOKIES, json={
        "query": query,
        "variables": variables
    })
    
    if response.status_code != 200:
        print(f"Error fetching submissions: {response.status_code}, {response.text}")
        response.raise_for_status()
    
    data = response.json().get("data", {}).get("questionSubmissionList", {}).get("submissions", [])
    
    # Filter for accepted submissions and get the one with lowest runtime
    accepted_submissions = [
        submission for submission in data if submission["statusDisplay"] == "Accepted"
    ]
    
    if not accepted_submissions:
        print(f"No accepted submissions found for {problem_slug}")
        return ""
    
    # Sort submissions by runtime in ascending order (most recent first)
    accepted_submissions.sort(key=lambda x: int(x["runtime"].replace(" ms", "")))
    print(accepted_submissions)
    
    # Get the URL of the most recent accepted submission
    last_submission_url = accepted_submissions[0]["id"]

    print(f"Most recent accepted submission URL: {last_submission_url}")
    return last_submission_url

def get_submission_details(submission_id):
    url = f"{BASE_URL}/graphql"
    
    query = """
    query submissionDetails($submissionId: Int!) {
      submissionDetails(submissionId: $submissionId) {
        runtime
        runtimeDisplay
        runtimePercentile
        runtimeDistribution
        memory
        memoryDisplay
        memoryPercentile
        memoryDistribution
        code
        timestamp
        statusCode
        user {
          username
          profile {
            realName
            userAvatar
          }
        }
        lang {
          name
          verboseName
        }
        question {
          questionId
        }
        notes
        topicTags {
          tagId
          slug
          name
        }
        runtimeError
        compileError
        lastTestcase
      }
    }
    """

    variables = {
        "submissionId": submission_id
    }
    
    headers = get_common_header(f"submissions/{submission_id}/details")
    
    response = requests.post(url, headers=headers, cookies=COOKIES, json={
        "query": query,
        "variables": variables
    })
    
    if response.status_code != 200:
        print(f"Error fetching submission details: {response.status_code}, {response.text}")
        response.raise_for_status()

    submission_details = response.json().get("data", {}).get("submissionDetails", {})
    
    if not submission_details:
        print(f"Submission details not found for submission ID: {submission_id}")
        return None

    # Get the code from the submission details
    code = submission_details.get("code", "")
    return code

def get_already_retrieved():
    # get all the folder under the solution folder
    folders = os.listdir("solutions")
    # return the list of question_id
    question_ids = [folder.split(".")[0] for folder in folders]
    return question_ids

def retriver():
    # if the question is already retrieved, skip it
    question_already_retrieved = get_already_retrieved()
    question_solved = list_all_solved()
    # first pop all the question that is already retrieved
    question_solved = [question for question in question_solved if question["questionId"] not in question_already_retrieved]
    
    # keep looping until all questions are done
    while True:
        # get the next solved question
        question = question_solved.pop(0)
        if question:
            # get the question details
            question_details = get_question_details(question["titleSlug"])
            # create a new folder wiht the question id.slug under the solution folder
            os.makedirs(
                f"solutions/{question['questionId']}.{question['titleSlug']}",
                exist_ok=True,
            )
            # save the question details to the folder as a json file
            with open(
                f"solutions/{question['questionId']}.{question['titleSlug']}/question.json",
                "w",
                encoding="utf-8",
            ) as f:
                json.dump(question_details, f, ensure_ascii=False)
            # get the last accepted code
            last_accepted_submission = get_last_accepted_submission(question["titleSlug"])
            print(last_accepted_submission)
            # get the submission details
            
            submission_details = get_submission_details(last_accepted_submission["id"])
            # save the code to the folder as solution. according to the langSlug
            with open(
                f"solution/{question['questionId']}.{question['titleSlug']}/solution.txt",
                "w",
                encoding="utf-8",
            ) as f:
                f.write(submission_details["code"])
        else:
            print("No more solved questions available.")
            break


if __name__ == "__main__":

    COOKIES = {
        "_ga": "GA1.2.791469091.1728104384",
        "LEETCODE_SESSION": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJfYXV0aF91c2VyX2lkIjoiMTI2NzA5MjgiLCJfYXV0aF91c2VyX2JhY2tlbmQiOiJhbGxhdXRoLmFjY291bnQuYXV0aF9iYWNrZW5kcy5BdXRoZW50aWNhdGlvbkJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiI5NTBhZjMyNmYyMjc0NDE4OGIwZTJlYmQyMTk3ZWQzYzAyMmU4NWIxMTZjNDc2MzJlYjM0Yzk4M2VmZWZiNTFlIiwiaWQiOjEyNjcwOTI4LCJlbWFpbCI6ImxhbmdzLjk3MTEwNEBnbWFpbC5jb20iLCJ1c2VybmFtZSI6ImdoMHN0aW50aGVzaGUxMSIsInVzZXJfc2x1ZyI6ImdoMHN0aW50aGVzaGUxMSIsImF2YXRhciI6Imh0dHBzOi8vYXNzZXRzLmxlZXRjb2RlLmNvbS91c2Vycy9naDBzdGludGhlc2hlMTEvYXZhdGFyXzE3MTAyMDQyNjQucG5nIiwicmVmcmVzaGVkX2F0IjoxNzI4MTA0Mzk2LCJpcCI6IjE0Mi4xOTguMjE0LjE0MiIsImlkZW50aXR5IjoiMDk5OTNhYjg2OGY0NzBjZjI0ZTI2ZmE0Zjk0MzlkOWUiLCJzZXNzaW9uX2lkIjo3NDU5MDkwN30.k9P1jtpWeUCZnmOBD-bm7Lzygu6vOKiPao3Jcjvv218",
        "gr_user_id": "363a4356-e134-405d-bbf8-ffd5c19a2028",
        "csrftoken": "jWHrYsRBv4Qhf1O8ViucEnkcqUpWzF0Ryx7BzbzXHmd5nqRThIePFlSfdQfLLV8D",
        "_ga_CDRWKZTDEX": "GS1.1.1728104384.1.1.1728104397.47.0.0",
        "_dd_s": "rum=0&expire=1728105288024",
        "87b5a3c3f1a55520_gr_session_id_sent_vst": "1b156a3d-5e60-48e7-b9e3-b16e2c1e4f51",
        "ip_check": '(false, "142.198.214.142")',
        "87b5a3c3f1a55520_gr_session_id": "1b156a3d-5e60-48e7-b9e3-b16e2c1e4f51",
        "messages": "W1siX19qc29uX21lc3NhZ2UiLDAsMjUsIlN1Y2Nlc3NmdWxseSBzaWduZWQgaW4gYXMgZ2gwc3RpbnRoZXNoZTExLiJdXQ:1swwtY:_uyiwNTflM_dou9VZKAfDWgYE-W4MjxOVTx1JWUyWnk",
        "_gat": "1",
        "_gid": "GA1.2.41745013.1728104384",
        "__cf_bm": "5V24iRo6KmIMuJacKUAiS8uWGMAjYEbxA5.6y5H7YMA-1728104383-1.0.1.1-dBkCs8VYNyaYKi2VqX63Z1Srwlot.WZXV.Zp0b9zmn0_w1qOD1ufoN5tAJ.1qr8j4pv3388uyus9V9AHRwQnoA",
    }

    
