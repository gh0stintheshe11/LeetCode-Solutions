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
import shutil
import indexer
from concurrent.futures import ThreadPoolExecutor

load_dotenv()

# Define COOKIES at the top to avoid NameError
COOKIES = {}

BASE_URL = "https://leetcode.com"

# file type based on the langSlug
FILE_TYPE = {
    "C++": ".cpp",
    "Java": ".java",
    "Python": ".py",
    "Python3": ".py",
    "MySQL": ".sql",
    "MS SQL Server": ".sql",
    "Oracle": ".sql",
    "C": ".c",
    "C#": ".cs",
    "JavaScript": ".js",
    "Ruby": ".rb",
    "Bash": ".sh",
    "Swift": ".swift",
    "Go": ".go",
    "Scala": ".scala",
    "Kotlin": ".kt",
    "Rust": ".rs",
    "PHP": ".php",
    "TypeScript": ".ts",
    "Racket": ".rkt",
    "Erlang": ".erl",
    "Elixir": ".ex",
    "Dart": ".dart",
    "PostgreSQL": ".sql",
    "Pandas": ".py",  # Typically uses Python files
    "React": ".jsx",  # or .js for standard JS files
    "Vanilla JS": ".js",
}


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
        "filters": {"status": "AC"},
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


def get_fastest_accepted_submission(problem_slug):
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
        "status": None,  # Leave it as None to fetch all statuses
    }

    headers = get_common_header(f"problems/{problem_slug}/submissions/")

    response = requests.post(
        url,
        headers=headers,
        cookies=COOKIES,
        json={"query": query, "variables": variables},
    )

    if response.status_code != 200:
        print(f"Error fetching submissions: {response.status_code}, {response.text}")
        response.raise_for_status()

    data = (
        response.json()
        .get("data", {})
        .get("questionSubmissionList", {})
        .get("submissions", [])
    )

    # Filter for accepted submissions and get the one with lowest runtime
    accepted_submissions = [
        submission for submission in data if submission["statusDisplay"] == "Accepted"
    ]

    if not accepted_submissions:
        print(f"No accepted submissions found for {problem_slug}")
        return ""

    submission_dict = {}
    # Keep only the accepted submission with the lowest runtime for each language
    for submission in accepted_submissions:
        lang = submission["lang"]
        # Convert runtime to an integer for comparison
        runtime_ms = int(submission["runtime"].replace(" ms", ""))

        if lang not in submission_dict:
            submission_dict[lang] = submission  # First submission for this language
        else:
            # Compare the current runtime with the stored one
            stored_runtime_ms = int(submission_dict[lang]["runtime"].replace(" ms", ""))
            if runtime_ms < stored_runtime_ms:
                submission_dict[lang] = submission  # Update if lower runtime found

    print(submission_dict)
    return submission_dict


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

    variables = {"submissionId": submission_id}

    headers = get_common_header(f"submissions/{submission_id}/details")

    response = requests.post(
        url,
        headers=headers,
        cookies=COOKIES,
        json={"query": query, "variables": variables},
    )

    if response.status_code != 200:
        print(
            f"Error fetching submission details: {response.status_code}, {response.text}"
        )
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


def remove_empty_file():
    for folder in os.listdir("solutions"):
        for file in os.listdir(f"solutions/{folder}"):
            file_path = f"solutions/{folder}/{file}"  # Define file_path here
            # Check if the file exists
            if os.path.exists(file_path):
                # Check if the file is empty
                if os.path.getsize(file_path) == 0:
                    os.remove(file_path)  # Remove the empty file
                    print(f"Removed empty file: {file_path}")
    print("Removed empty files.")


def remove_empty_folder():
    # remove all folder if there is only one question.json
    for folder in os.listdir("solutions"):
        if len(
            os.listdir(f"solutions/{folder}")
        ) == 1 and "question.json" in os.listdir(f"solutions/{folder}"):
            folder_path = f"solutions/{folder}"
            if os.path.exists(folder_path):
                shutil.rmtree(folder_path)
                print(f"Removed directory: {folder_path}")
            else:
                print(f"Directory does not exist: {folder_path}")
    print("Removed empty folders.")


def retriver_new():
    # remove the empty file and folder
    remove_empty_file()
    remove_empty_folder()
    # if the question is already retrieved, skip it
    question_already_retrieved = get_already_retrieved()
    question_solved = list_all_solved()
    # first pop all the question that is already retrieved
    question_solved = [
        question
        for question in question_solved
        if question["questionId"] not in question_already_retrieved
    ]

    while question_solved != []:

        # keep looping until all questions are done
        while True:
            # get the next solved question
            if question_solved:
                question = question_solved.pop(0)
            else:
                print("No more solved questions available.")
                break
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

                # get the fastest accepted submission
                fastest_accepted_submission = get_fastest_accepted_submission(
                    question["titleSlug"]
                )
                # for all the lang in the fastest_accepted_submission, get the submission details
                for lang in fastest_accepted_submission:
                    submission_id = fastest_accepted_submission[lang]["id"]
                    langName = fastest_accepted_submission[lang]["langName"]

                    # get the submission details
                    submission_details = get_submission_details(submission_id)

                    # Check if submission_details is empty and if this is the only submission
                    if not submission_details and len(fastest_accepted_submission) == 1:
                        # Remove the question folder and skip to the next question
                        question_folder = f"solutions/{question['questionId']}.{question['titleSlug']}"
                        if os.path.exists(question_folder):
                            shutil.rmtree(question_folder)  # Remove the folder
                        print(
                            f"Removed folder: {question_folder} as there were no valid submissions."
                        )
                        continue  # Skip to the next question
                    elif not submission_details:
                        # this is not the only submission, skip to next lang
                        continue
                    else:
                        # Save the code to the folder as solution according to the langSlug
                        with open(
                            f"solutions/{question['questionId']}.{question['titleSlug']}/{langName.replace(' ', '')}{FILE_TYPE[langName]}",
                            "w",
                            encoding="utf-8",
                        ) as f:
                            f.write(submission_details)

        # if there is no question left in the current question_solved, reset the question_solved and run again
        remove_empty_file()
        remove_empty_folder()
        question_already_retrieved = get_already_retrieved()
        question_solved = list_all_solved()
        question_solved = [
            question
            for question in question_solved
            if question["questionId"] not in question_already_retrieved
        ]

    # remove the empty file and folder
    remove_empty_file()
    remove_empty_folder()

    # check if the folder number is the same as the question_solved number
    question_solved = list_all_solved()
    if len(os.listdir("solutions")) == len(question_solved):
        print("All questions are retrieved.")
    else:
        print("Some questions are not retrieved.")


def retriver_update():
    # get all the question that is solved
    question_solved = list_all_solved()
    question_updated = []
    while question_solved != question_updated:
        question_left = [
            question for question in question_solved if question not in question_updated
        ]
        for question in question_left:
            # get the fastest accepted submission
            fastest_accepted_submission = get_fastest_accepted_submission(
                question["titleSlug"]
            )
            # get all the langugaes that already in the existing solution
            existing_solution = os.listdir(
                f"solutions/{question['questionId']}.{question['titleSlug']}"
            )
            # remove the question.json from the existing_solution
            existing_solution = [
                file for file in existing_solution if file != "question.json"
            ]
            # remove the file extension
            existing_solution = [file.split(".")[0] for file in existing_solution]

            # Corrected filtering logic
            fastest_accepted_submission = {
                lang: submission
                for lang, submission in fastest_accepted_submission.items()
                if submission["langName"] not in existing_solution
            }

            # for all the lang in the fastest_accepted_submission, they are new accepted submissions, get the submission details
            for lang in fastest_accepted_submission:
                submission_id = fastest_accepted_submission[lang]["id"]
                langName = fastest_accepted_submission[lang]["langName"]
                # get the submission details
                submission_details = get_submission_details(submission_id)

                # Check if submission_details is None or empty
                if submission_details is None:
                    print(
                        f"No submission details found for submission ID: {submission_id}. Skipping write."
                    )

                    continue  # Skip to the next iteration if no details are found

                # Save the code to the folder as solution according to the langSlug
                with open(
                    f"solutions/{question['questionId']}.{question['titleSlug']}/{langName.replace(' ', '')}{FILE_TYPE[langName]}",
                    "w",
                    encoding="utf-8",
                ) as f:
                    f.write(submission_details)
            question_updated.append(question)

        # remove the empty file and folder
        remove_empty_file()
        remove_empty_folder()


# use multithreading to update the existing solution -> get all the question that is solved -> use each thread to send a request to get the fastest accepted submission -> if the submission is not in the existing solution, add it
def retriver_update_mt():
    # get all the question that is solved
    question_solved = list_all_solved()
    # for each question in question_solved, use a thread to update it
    with ThreadPoolExecutor(max_workers=10) as executor:
        executor.map(retriver_update_mt_helper, question_solved)


# helper function for retriver_update_mt
def retriver_update_mt_helper(question):
    # get the fastest accepted submission
    fastest_accepted_submission = get_fastest_accepted_submission(question["titleSlug"])
    # get all the langugaes that already in the existing solution
    existing_solution = os.listdir(
        f"solutions/{question['questionId']}.{question['titleSlug']}"
    )
    # remove the question.json from the existing_solution
    existing_solution = [file for file in existing_solution if file != "question.json"]
    # remove the file extension
    existing_solution = [file.split(".")[0] for file in existing_solution]

    # Corrected filtering logic
    fastest_accepted_submission = {
        lang: submission
        for lang, submission in fastest_accepted_submission.items()
        if submission["langName"] not in existing_solution
    }

    # for all the lang in the fastest_accepted_submission, they are new accepted submissions, get the submission details
    for lang in fastest_accepted_submission:
        submission_id = fastest_accepted_submission[lang]["id"]
        langName = fastest_accepted_submission[lang]["langName"]
        # get the submission details
        submission_details = get_submission_details(submission_id)

        # Check if submission_details is None or empty
        if submission_details is None:
            print(
                f"No submission details found for submission ID: {submission_id}. Skipping write."
            )
            continue  # Skip to the next iteration if no details are found

        # Save the code to the folder as solution according to the langSlug
        with open(
            f"solutions/{question['questionId']}.{question['titleSlug']}/{langName.replace(' ', '')}{FILE_TYPE[langName]}",
            "w",
            encoding="utf-8",
        ) as f:
            f.write(submission_details)

# remove all file whose file name contains space
def clean_up():
    for folder in os.listdir("solutions"):
        for file in os.listdir(f"solutions/{folder}"):
            if " " in file:
                os.remove(f"solutions/{folder}/{file}")
                print(f"Removed file: {file}")
    print("Removed all files with spaces.")

if __name__ == "__main__":

    COOKIES = login_to_leetcode()

    retriver_new()
    retriver_update_mt()
    clean_up()
    indexer.format_index_page(indexer.list_questions())


