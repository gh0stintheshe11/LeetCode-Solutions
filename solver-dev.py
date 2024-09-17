import time
import undetected_chromedriver as uc
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, ElementClickInterceptedException
import requests
import json

LEETCODE_LOGIN_URL = "https://leetcode.com/accounts/login/"
LEETCODE_USERNAME = 'langs.971104@gmail.com'  # Replace with your LeetCode username
LEETCODE_PASSWORD = 'zd971121'  # Replace with your LeetCode password
CSRF_TOKEN = 'csrf_token'
LEETCODE_SESSION = 'leetcode_session'

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

        # Input username and password
        driver.find_element(By.ID, "login_field").send_keys(LEETCODE_USERNAME)
        driver.find_element(By.ID, "password").send_keys(LEETCODE_PASSWORD)

        # Click Sign in button
        sign_in_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'input[type="submit"][value="Sign in"]')))
        sign_in_button.click()

        # Wait for login to complete
        wait.until(EC.url_contains("https://leetcode.com/"))
        print("Login successful.")

        # Get CSRF token and cookies
        CSRF_TOKEN = driver.get_cookie('csrftoken')['value']
        LEETCODE_SESSION = driver.get_cookie('LEETCODE_SESSION')['value']

        return CSRF_TOKEN, LEETCODE_SESSION
    
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

def submit_solution(problem_slug, language, code):
    session = requests.Session()
    
    # Set cookies   
    session.cookies.set('csrftoken', CSRF_TOKEN)
    session.cookies.set('LEETCODE_SESSION', LEETCODE_SESSION)
    
    submit_url = f'https://leetcode.com/problems/{problem_slug}/submit/'
    
    data = {
        'lang': language,
        'question_slug': problem_slug,
        'typed_code': code
    }
    
    headers = {
        'Content-Type': 'application/json',
        'X-CSRFToken': CSRF_TOKEN,
        'Referer': f'https://leetcode.com/problems/{problem_slug}/',
        'Origin': 'https://leetcode.com',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }
    
    try:
        response = session.post(submit_url, data=json.dumps(data), headers=headers)
        response.raise_for_status()  # Raise an exception for bad status codes
        
        submission_data = response.json()
        submission_id = submission_data.get('submission_id')
        
        if submission_id:
            print(f"Submission successful. Submission ID: {submission_id}")
            return submission_id
        else:
            print("Submission failed. No submission ID returned.")
            print(f"Response content: {response.text}")
            return None
    
    except requests.exceptions.RequestException as e:
        print(f"Submission failed. Error: {e}")
        if hasattr(e, 'response') and e.response is not None:
            print(f"Status code: {e.response.status_code}")
            print(f"Response content: {e.response.text}")
        return None

if __name__ == "__main__":
    login_to_leetcode()
    
    submit_solution('two-sum', 'python3', 'print(123)')