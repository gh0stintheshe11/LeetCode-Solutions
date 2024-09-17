import time
import undetected_chromedriver as uc
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, ElementClickInterceptedException
import requests
import json
import os
from dotenv import load_dotenv
from bs4 import BeautifulSoup

load_dotenv()
LEETCODE_LOGIN_URL = "https://leetcode.com/accounts/login/"
LEETCODE_USERNAME = os.getenv('LEETCODE_USERNAME')
LEETCODE_PASSWORD = os.getenv('LEETCODE_PASSWORD')

#load the solution.txt file
with open('solution.txt', 'r') as file:
    SOLUTION = file.read()

def login_to_leetcode():
    print("Initializing WebDriver...")
    driver = webdriver.Chrome()
    wait = WebDriverWait(driver, 30)

    try:
        print("Navigating to LeetCode login page...")
        driver.get(LEETCODE_LOGIN_URL)

        # Wait for the loading overlay to disappear
        try:
            wait.until(EC.invisibility_of_element_located((By.ID, "initial-loading")))
        except TimeoutException:
            print("Loading overlay did not disappear. Attempting to continue...")

        # Wait for and click GitHub login button
        max_attempts = 3
        for attempt in range(max_attempts):
            try:
                github_login_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'a[href*="github/login"]')))
                github_login_button.click()
                break
            except (TimeoutException, ElementClickInterceptedException) as e:
                if attempt < max_attempts - 1:
                    print(f"Attempt {attempt + 1} failed. Retrying in 5 seconds...")
                    time.sleep(5)
                else:
                    print("Failed to click GitHub login button after multiple attempts.")
                    raise e

        # Wait for the "Continue" button on GitHub authorization page and click it
        print("Waiting for Continue button...")
        try:
            continue_button = wait.until(EC.element_to_be_clickable((By.XPATH, '//div[@id="base_content"]//button[text()="Continue"]')))
            continue_button.click()
            print("Clicked Continue button.")
        except TimeoutException:
            print("Continue button not found. Please check the page manually.")
            input("Press Enter after manually clicking Continue or if you need to proceed...")

        # Wait for GitHub login page to load
        print("Waiting for GitHub login page to load...")
        wait.until(EC.presence_of_element_located((By.ID, "login_field")))

        # Add this check before using LEETCODE_USERNAME
        if LEETCODE_USERNAME is None:
            raise ValueError("LEETCODE_USERNAME environment variable is not set")

        driver.find_element(By.ID, "login_field").send_keys(LEETCODE_USERNAME)
        driver.find_element(By.ID, "password").send_keys(LEETCODE_PASSWORD)

        # Click Sign in button
        sign_in_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'input[type="submit"][value="Sign in"]')))
        sign_in_button.click()

        # Wait for login to complete
        wait.until(EC.url_contains("https://leetcode.com/"))
        print("Login successful.")

        # Get all cookies
        cookies = driver.get_cookies()
        cookie_dict = {cookie['name']: cookie['value'] for cookie in cookies}

        return cookie_dict
    
    finally:
        driver.quit()

def list_all_questions():
    # use graphql to get all questions
    url = "https://leetcode.com/graphql"
    query = """
    query {
        allQuestions {
            title
            titleSlug
            difficulty
            isPaidOnly
        }
    }
    """
    
    headers = {
        'Content-Type': 'application/json',
        'Referer': 'https://leetcode.com',
        'Origin': 'https://leetcode.com',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }
    
    response = requests.post(url, json={'query': query}, headers=headers)
    response.raise_for_status()  # Raise an exception for bad status codes
    
    data = response.json()
    questions = data['data']['allQuestions']
    
    return questions

def get_question_details(problem_slug):
    url = "https://leetcode.com/graphql"
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
    
    variables = {
        "titleSlug": problem_slug
    }
    
    headers = {
        'Content-Type': 'application/json',
        'Referer': 'https://leetcode.com',
        'Origin': 'https://leetcode.com',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }
    
    response = requests.post(url, json={'query': query, 'variables': variables}, headers=headers)
    response.raise_for_status()  # Raise an exception for bad status codes
    
    if response.status_code == 200:
        questions = response.json()['data']['question']
        # get the question id   
        question_id = questions['questionId']
        # get the problem title
        problem_title = questions['title']
        # get the content
        content = questions['content']
        # chnage the content from html to markdown for better processing
        content = BeautifulSoup(content, 'html.parser').get_text()
        # get the hints
        hints = questions['hints']
        # get the example test cases
        exampleTestcases = questions['exampleTestcases']
        # get the code snippets
        codeSnippets = questions['codeSnippets']
        #reformat the codeSnippets to be a dicts with lang as key and code as value
        codeSnippets = {snippet['lang']: snippet['code'] for snippet in codeSnippets}
        return question_id, problem_title, content, hints, exampleTestcases, codeSnippets
    else:
        raise Exception(f"Failed to get question details: {response.status_code}")

# submit solution
def submit_solution(question_id, problem_slug, lang, code, cookies):
    url = f"https://leetcode.com/problems/{problem_slug}/submit/"
    
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
        "Referer": f"https://leetcode.com/problems/{problem_slug}/",
        "X-CSRFToken": cookies.get('csrftoken', ''),
    }
    
    # Convert cookies dict to string format for header
    cookie_string = '; '.join([f"{name}={value}" for name, value in cookies.items()])
    headers['Cookie'] = cookie_string

    data = {
        "lang": lang,
        "question_id": question_id,
        "typed_code": code,
    }
    
    response = requests.post(url, headers=headers, json=data)
    response.raise_for_status()
    
    return response.json()

# get submission result
def get_submission_status(submission_id, cookies):
    url = f"https://leetcode.com/submissions/detail/{submission_id}/check/"
    
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
        "Referer": "https://leetcode.com/submissions/",
        "X-Requested-With": "XMLHttpRequest",
        "X-CSRFToken": cookies.get('csrftoken', ''),
    }
    
    session = requests.Session()
    session.cookies.update(cookies)
    
    response = session.get(url, headers=headers)
    response.raise_for_status()
    
    if response.status_code == 200:
        return response.json()
    else:
        soup = BeautifulSoup(response.text, 'html.parser')
        error_message = soup.find('div', class_='error-message')
        if error_message:
            raise Exception(f"Error: {error_message.text.strip()}")
        else:
            raise Exception(f"Unexpected response: {response.status_code}")

# check the result of the submission
def check_result(submission_id, cookies):
    # Poll for the result
    max_attempts = 10
    for attempt in range(max_attempts):
        result = get_submission_status(submission_id, cookies)
        print(f"Attempt {attempt + 1}: {result}")
        
        if result['state'] == 'SUCCESS':
            return result
        elif result['state'] in ['PENDING', 'STARTED']:
            time.sleep(2)  # Wait for 2 seconds before trying again
        else:
            raise Exception(f"Unexpected submission state: {result['state']}")
    
    raise Exception("Timed out waiting for submission result")

# test solution
def test_solution(question_id, problem_slug, lang, code, test_case, cookies):
    url = f"https://leetcode.com/problems/{problem_slug}/interpret_solution/"
    
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
        "Referer": f"https://leetcode.com/problems/{problem_slug}/",
        "Content-Type": "application/json",
        "X-CSRFToken": cookies.get('csrftoken', ''),
    }
    
    data = {
        "question_id": question_id,
        "lang": lang,
        "typed_code": code,
        "data_input": test_case
    }
    
    response = requests.post(url, headers=headers, data=json.dumps(data), cookies=cookies)
    response.raise_for_status()
    
    return response.json()



if __name__ == "__main__":
    cookies = {'_ga': 'GA1.2.56629168.1726609680',
 'LEETCODE_SESSION': 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJfYXV0aF91c2VyX2lkIjoiMTI2NzA5MjgiLCJfYXV0aF91c2VyX2JhY2tlbmQiOiJhbGxhdXRoLmFjY291bnQuYXV0aF9iYWNrZW5kcy5BdXRoZW50aWNhdGlvbkJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiI5NTBhZjMyNmYyMjc0NDE4OGIwZTJlYmQyMTk3ZWQzYzAyMmU4NWIxMTZjNDc2MzJlYjM0Yzk4M2VmZWZiNTFlIiwiaWQiOjEyNjcwOTI4LCJlbWFpbCI6ImxhbmdzLjk3MTEwNEBnbWFpbC5jb20iLCJ1c2VybmFtZSI6ImdoMHN0aW50aGVzaGUxMSIsInVzZXJfc2x1ZyI6ImdoMHN0aW50aGVzaGUxMSIsImF2YXRhciI6Imh0dHBzOi8vYXNzZXRzLmxlZXRjb2RlLmNvbS91c2Vycy9naDBzdGludGhlc2hlMTEvYXZhdGFyXzE3MTAyMDQyNjQucG5nIiwicmVmcmVzaGVkX2F0IjoxNzI2NjA5NjkyLCJpcCI6IjE0Mi4xOTguMjE0LjE0MiIsImlkZW50aXR5IjoiZThkYjFhOTEwZWUwODhiNDY5ZWNmZDJiNmE5YjlkYTUiLCJzZXNzaW9uX2lkIjo3MjY2ODc5Mn0.bxFFduqm2Nd0_I94WWuIbj_0eWo015oF2X5XBDUQ3kM',
 'gr_user_id': '8064b639-1552-4ae5-bac5-18e205b69a46',
 'csrftoken': '8UpC2D7q1jaQduhYoCWRt5LQUyjn8YTwzjTZHRKFKPQALBuBNC60z8q2XLaLQS7r',
 '_ga_CDRWKZTDEX': 'GS1.1.1726609680.1.1.1726609693.47.0.0',
 '_dd_s': 'rum=0&expire=1726610584389',
 '87b5a3c3f1a55520_gr_session_id_sent_vst': 'e770d55e-34f4-4c6a-9d6d-119090784bbb',
 'messages': 'W1siX19qc29uX21lc3NhZ2UiLDAsMjUsIlN1Y2Nlc3NmdWxseSBzaWduZWQgaW4gYXMgZ2gwc3RpbnRoZXNoZTExLiJdXQ:1sqg3Q:AKLlRIiJTG9qaGU7wZIRWP0tfNyfugvOZKMibtowTH0',
 '87b5a3c3f1a55520_gr_session_id': 'e770d55e-34f4-4c6a-9d6d-119090784bbb',
 'ip_check': '(false, "142.198.214.142")',
 '_gat': '1',
 '_gid': 'GA1.2.1583653120.1726609680',
 '__cf_bm': 'bImS6L.YQZ3zwWInfjQ27QcVO3hpGQDqxQsoLwUATRk-1726609679-1.0.1.1-.Iol71JMNRdZe1SRo88XK2QqbK.ZrcreiBaYo2PBU1TvnzoU7nxtTOCYUHjL2Vnh2mEPkfd5ZkumRkF6KxQ1EQ'}
    try:
        # get the question details
        question_id, problem_title, content, hints, exampleTestcases, codeSnippets = get_question_details('two-sum')
        print(question_id, problem_title, content, hints, exampleTestcases, codeSnippets)

        #submission_id = submit_solution('two-sum', 'c', SOLUTION, cookies)['submission_id']
        #print(submission_id)

        #final_result = check_result(submission_id, cookies)
        #print("Final result:", final_result)

    except requests.exceptions.HTTPError as e:
        print(f"HTTP Error occurred: {e}")
        print(f"Response content: {e.response.content}")