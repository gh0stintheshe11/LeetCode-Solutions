# Import necessary libraries
import os  # For operating system related operations
import re  # For regular expression operations
import time  # For adding delays in the script
import random  # For making random selections
import undetected_chromedriver as uc  # For using an undetected version of Chrome WebDriver
import anthropic  # For interacting with the Claude AI API

# Import Selenium WebDriver and related modules for web automation
from selenium import webdriver
from selenium.webdriver.common.by import By  # For locating elements on web pages
from selenium.webdriver.common.keys import Keys  # For simulating keyboard input
from selenium.webdriver.support.ui import WebDriverWait  # For waiting for elements to appear
from selenium.webdriver.support import expected_conditions as EC  # For defining expected conditions for WebDriverWait
from selenium.common.exceptions import TimeoutException, NoSuchElementException  # For handling specific exceptions
from selenium.webdriver.common.action_chains import ActionChains  # For performing complex user interactions
from selenium.common.exceptions import TimeoutException  # For handling timeout exceptions
from bs4 import BeautifulSoup  # For parsing HTML content

# Constants and Global Variables
CLAUDE_MODEL = "claude-3-sonnet-20240229"  # Specifies the version of Claude AI to use
MAX_TOKENS = 1000  # Maximum number of tokens for Claude API responses
TEMPERATURE = 0  # Controls randomness in Claude's responses (0 means deterministic)
FAILED_PROBLEMS = set()  # Stores problems that couldn't be solved
API_KEY = "Your API Key Here"  # Placeholder for Claude API key
STARTING_A_NEW_PROBLEM_PROMPT = "Solve this LeetCode problem in Python, optimizing for the fastest runtime approach with the best time complexity unless there is a required time complexity in the description, in that case your solution must match that time complexity. Provide only the Python code solution, with no additional text, comments, or questions before or after the code:"  # Prompt for Claude when starting a new problem
SUBMITTING_A_CODE_ERROR_PROMPT = "We need to fix our code for a leetcode python problem. Here's what the problem description was: "  # Prompt for Claude when submitting a code with errors
OUR_CURRENT_CODE_PROMPT = "Here's what the Python code we tried was:"  # Prompt to introduce the current code to Claude
END_OF_PROMPT_INSTRUCTIONS_FOR_CLEAR_RESPONSE = "Provide only the Python code solution, with no additional text, comments, or questions before or after the code. The solution must start with the same class solution object and function definition(s) and their parameter(s) that the starting code had."  # Instructions for Claude to provide a clear response
ADVOCATE_FOR_BETTER_SOLUTION_ON_RETRY = "Don't use the same approach as the current code which looks like this, review what part of the description we're likely not meeting the requirements of and make a new solution with an approach that likely is a better fix."  # Prompt for Claude to suggest a better solution on retry
CODE_EXAMPLE_PREFIX = "Here's the starting code provided by LeetCode:"  # Prefix for introducing LeetCode's starting code to Claude

CURRENT_PAGE = 1  # Tracks the current page of LeetCode problems

MAX_RETRIES = 2  # Maximum number of attempts to solve a problem
LEETCODE_PROBLEMSET_URL = "https://leetcode.com/problemset/?page=1&topicSlugs=array&status=NOT_STARTED"  # URL for LeetCode problem set
LEETCODEFILTER = 'https://leetcode.com/problemset/?page='  # Base URL for filtered LeetCode problems
LEETCODEPOSTFILTER = '&topicSlugs=array&status=NOT_STARTED'  # Additional filter parameters for LeetCode problems

LEETCODE_PROBLEM_URL_PREFIX = "https://leetcode.com/problems/"  # Prefix for individual LeetCode problem URLs
LEETCODE_LOGIN_URL = "https://leetcode.com/accounts/login/"  # URL for LeetCode login page
problem_title = ''  # Placeholder for storing the current problem title
LEETCODE_USERNAME = 'Hermesroblox'  # LeetCode username, replace with your own.
LEETCODE_PASSWORD = ''  # Placeholder for LeetCode password (left blank for security)



class WebAutomation:
    def __init__(self):
        print("Initializing WebAutomation...")
        self.driver = webdriver.Chrome()  # Initialize a Chrome WebDriver instance
        self.wait = WebDriverWait(self.driver, 30)  # Create a WebDriverWait object with a 30-second timeout
        print("WebAutomation initialized.")

    def navigate_to(self, url):
        print(f"Navigating to {url}...")
        self.driver.get(url)  # Use the WebDriver to navigate to the specified URL
        print(f"Navigation complete.")

    def find_element(self, by, value):
        print(f"Finding element by {by}: {value}...")
        element = self.wait.until(EC.presence_of_element_located((by, value)))  # Wait for the element to be present in the DOM
        print("Element found.")
        return element

    def click_element(self, by, value):
        print(f"Clicking element by {by}: {value}...")
        element = self.wait.until(EC.element_to_be_clickable((by, value)))  # Wait for the element to be clickable
        element.click()  # Click the element
        print("Element clicked.")

    def input_text(self, by, value, text):
        print(f"Inputting text into element by {by}: {value}...")
        element = self.find_element(by, value)  # Find the input element
        element.clear()  # Clear any existing text in the element
        element.send_keys(text)  # Input the new text
        print("Text input complete.")

    def get_text(self, by, value):
        print(f"Getting text from element by {by}: {value}...")
        text = self.find_element(by, value).text  # Find the element and get its text content
        print(f"Text retrieved: {text}...") 
        return text

    def current_url(self):
        url = self.driver.current_url  # Get the current URL from the WebDriver
        print(f"Current URL: {url}")
        return url

    def press_keys(self, by, value, *keys):
        print(f"Pressing keys {keys} on element by {by}: {value}...")
        element = self.find_element(by, value)  # Find the element to send keys to
        element.send_keys(keys)  # Send the specified keys to the element
        print("Keys pressed.")

    def ensure_python_language(self):
        print("Ensuring Python language is selected...")
        try:
            lang_select = self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button.text-sm.font-normal.group")))  # Wait for the language selector to be clickable
            
            if "python" in lang_select.text.lower():
                print("Python is already selected.")
                return

            print("Clicking language selector...")
            lang_select.click()  # Click the language selector to open the dropdown
            time.sleep(1)  # Wait for dropdown to open

            print("Selecting Python from dropdown...")
            python_option = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//div[contains(@class, 'text-text-primary') and text()='Python']")))  # Wait for the Python option to be clickable
            python_option.click()  # Select Python
            
            print("Successfully set language to Python.")
        except (TimeoutException, NoSuchElementException) as e:
            print(f"Error setting language to Python: {str(e)}")
            print("Attempting to continue with current language selection.")

    def login(self, username, password):
        print("Attempting to log in...")
        self.navigate_to(LEETCODE_LOGIN_URL)  # Navigate to the LeetCode login page
        
        # Wait for the loading overlay to disappear
        try:
            self.wait.until(EC.invisibility_of_element_located((By.ID, "initial-loading")))
        except TimeoutException:
            print("Loading overlay did not disappear. Attempting to continue...")

        # Wait for and click GitHub login button
        max_attempts = 3
        for attempt in range(max_attempts):
            try:
                github_login_button = self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'a[href*="github/login"]')))  # Wait for the GitHub login button to be clickable
                github_login_button.click()  # Click the GitHub login button
                break
            except (TimeoutException, ElementClickInterceptedException) as e:
                if attempt < max_attempts - 1:
                    print(f"Attempt {attempt + 1} failed. Retrying in 5 seconds...")
                    time.sleep(5)  # Wait for 5 seconds before retrying
                else:
                    print("Failed to click GitHub login button after multiple attempts.")
                    raise e

        # Wait for the "Continue" button on GitHub authorization page and click it
        print("Waiting for Continue button...")
        try:
            continue_button = self.wait.until(EC.element_to_be_clickable((By.XPATH, '//div[@id="base_content"]//button[text()="Continue"]')))  # Wait for the Continue button to be clickable
            continue_button.click()  # Click the Continue button
            print("Clicked Continue button.")
        except TimeoutException:
            print("Continue button not found. Please check the page manually.")
            input("Press Enter after manually clicking Continue or if you need to proceed...")

        # Wait for GitHub login page to load
        print("Waiting for GitHub login page to load...")
        self.wait.until(EC.presence_of_element_located((By.ID, "login_field")))  # Wait for the username field to be present
        
        # Input username and password
        self.input_text(By.ID, "login_field", username)  # Enter the username
        self.input_text(By.ID, "password", password)  # Enter the password
        
        # Click Sign in button
        sign_in_button = self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'input[type="submit"][value="Sign in"]')))  # Wait for the Sign in button to be clickable
        sign_in_button.click()  # Click the Sign in button
        
        # Wait for login to complete
        try:
            self.wait.until(EC.url_contains("https://leetcode.com/"))  # Wait for the URL to change to LeetCode
            print("Login successful.")
            
            # Wait for 5 seconds after successful login
            print("Waiting 5 seconds after successful login...")
            time.sleep(5)
            
            # Navigate to the problems page
            print("Navigating to problems page...")
            self.navigate_to(LEETCODE_PROBLEMSET_URL)  # Navigate to the LeetCode problem set page
            
            # Wait for the problems page to load
            self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'div[role="rowgroup"]')))  # Wait for the problem list to be present
            print("Successfully navigated to problems page.")
            
        except TimeoutException:
            print("Login failed. Please check your credentials or solve any CAPTCHA manually.")
            input("Press Enter after solving any CAPTCHA...")  # Wait for manual intervention if needed

    def manual_login(self):
        print("Navigating to login page...")
        self.navigate_to(LEETCODE_LOGIN_URL)  # Navigate to the LeetCode login page
        print("Please log in manually.")
        print("Waiting for login to complete or 30 seconds to pass...")
        
        try:
            # Wait until we're on the problems page or 30 seconds have passed
            self.wait.until(EC.url_contains("https://leetcode.com/problemset/"))  # Wait for the URL to change to the problem set page
            print("Successfully reached the problems page.")
        except TimeoutException:
            print("30 seconds have passed. Proceeding with the script.")
        
        # Check if we're logged in by looking for a common element on the logged-in homepage
        try:
            self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'div[role="rowgroup"]')))  # Wait for the problem list to be present
            print("Login successful.")
        except TimeoutException:
            print("Login status uncertain. Please ensure you're logged in before proceeding.")
            input("Press Enter to continue...")

class LeetCodeInteraction:
    def __init__(self, web_automation):
        self.web = web_automation  # Store the WebAutomation instance for interacting with the website

    def get_problem_description(self):
        print("Getting problem description...")
        try:
            # Get the HTML content of the description
            description_element = self.web.find_element(By.CSS_SELECTOR, 'div[data-track-load="description_content"]')  # Find the element containing the problem description
            html_content = description_element.get_attribute('innerHTML')  # Get the HTML content of the description
            
            # Parse the HTML
            soup = BeautifulSoup(html_content, 'html.parser')  # Create a BeautifulSoup object to parse the HTML
            
            # Function to recursively process elements
            def process_element(element):
                if isinstance(element, str):
                    return element
                if element.name == 'sup':
                    return f'^{element.text}'  # Format superscript
                elif element.name == 'sub':
                    return f'_{element.text}'  # Format subscript
                elif element.name == 'code':
                    code_content = ''.join(process_element(child) for child in element.children)
                    return f'`{code_content}`'  # Format inline code
                elif element.name in ['p', 'div', 'li']:
                    return '\n' + ''.join(process_element(child) for child in element.children)  # Add newlines for paragraphs, divs, and list items
                elif element.name == 'strong' or element.name == 'b':
                    return f'**{element.text}**'  # Format bold text
                elif element.name == 'em' or element.name == 'i':
                    return f'*{element.text}*'  # Format italic text
                elif element.name == 'pre':
                    return f'\n```\n{element.text}\n```\n'  # Format code blocks
                else:
                    return ''.join(process_element(child) for child in element.children)  # Process other elements recursively

            # Process the entire soup
            processed_text = process_element(soup)
            
            # Remove extra newlines and spaces
            processed_text = re.sub(r'\n\s*\n', '\n\n', processed_text).strip()  # Clean up the processed text
            
            print(f"Problem description retrieved: {processed_text}...") 
            return processed_text
        except Exception as e:
            print(f"Error getting problem description: {str(e)}")
            return ""

    def get_starting_code(self):
        print("Getting starting code...")
        try:
            # Wait for 5 seconds before attempting to get the starting code
            time.sleep(5)
            # Wait for the Monaco editor to load
            self.web.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '.view-lines')))  # Wait for the code editor to be present
            
            # Get all lines of code
            code_lines = self.web.driver.find_elements(By.CSS_SELECTOR, '.view-line')  # Find all lines of code in the editor
            
            # Combine all lines into a single string
            code = '\n'.join([line.text for line in code_lines if line.text])  # Join all non-empty lines of code
            
            print(f"Starting code retrieved: {code}...")
            return code
        except Exception as e:
            print(f"Error getting starting code: {str(e)}")
            return ""

    def clear_code_editor(self):
        print("Clearing code editor...")
        try:
            # Use JavaScript to clear the editor
            js_clear_editor = """
            var editor = monaco.editor.getEditors()[0];
            editor.setValue('');
            """
            self.web.driver.execute_script(js_clear_editor)  # Execute JavaScript to clear the editor
            print("Code editor cleared.")
        except Exception as e:
            print(f"Error clearing code editor: {str(e)}")

    def input_code(self, code):
        print("Inputting code into editor...")
        self.clear_code_editor()  # Clear the existing code in the editor
        try:
            # Use JavaScript to set the value of the editor
            js_set_editor_value = f"""
            var editor = monaco.editor.getEditors()[0];
            editor.setValue(`{code}`);
            """
            self.web.driver.execute_script(js_set_editor_value)  # Execute JavaScript to set the new code in the editor
            print("Code input complete.")
        except Exception as e:
            print(f"Error inputting code: {str(e)}")

    def run_code(self):
        print("Running code...")
        try:
            # Find and click the "Run" button
            run_button = self.web.find_element(By.CSS_SELECTOR, 'button[data-e2e-locator="console-run-button"]')  # Find the Run button
            run_button.click()  # Click the Run button
            print("Code execution initiated.")
        except Exception as e:
            print(f"Error running code: {str(e)}")
            # Fallback to keyboard shortcut if button not found
            self.web.press_keys(By.CSS_SELECTOR, '.monaco-editor textarea', Keys.CONTROL, Keys.ENTER)  # Use keyboard shortcut to run code

    def get_test_results(self):
        print("Getting test results...")
        try:
            # Wait for either the test result or runtime error
            result_or_error = self.web.wait.until(EC.presence_of_element_located((
                By.CSS_SELECTOR, 
                'div[data-e2e-locator="console-result"], div.font-menlo.text-xs.text-red-60'
            )))  # Wait for either the test result or error message to appear
            
            if "Runtime Error" in result_or_error.text:
                # Handle runtime error
                error_message = result_or_error.text
                input_elements = self.web.driver.find_elements(By.XPATH, "//div[contains(@class, 'bg-fill-4')]/div/div[contains(@class, 'font-menlo')]")
                input_text = input_elements[0].text if input_elements else "Input not found"
                
                full_results = {
                    "result": "Runtime Error",
                    "error_message": error_message,
                    "cases": [{"Input": input_text}]
                }
            else:
                # Handle normal test results (existing code)
                result_text = result_or_error.text
                detailed_results = []
                case_buttons = self.web.driver.find_elements(By.CSS_SELECTOR, 'div.cursor-pointer.rounded-lg.px-4.py-1.font-medium')  # Find all test case buttons
                
                for button in case_buttons:
                    button.click()  # Click each test case button
                    time.sleep(1)  # Wait for the case details to load
                    
                    case_details = {}
                    
                    # Find Input section
                    input_elements = self.web.driver.find_elements(By.XPATH, "//div[contains(@class, 'bg-fill-4')]/div/div[contains(@class, 'font-menlo')]")
                    if input_elements:
                        case_details['Input'] = input_elements[0].text
                    
                    # Find Output and Expected sections
                    sections = self.web.driver.find_elements(By.CSS_SELECTOR, 'div.flex.h-full.w-full.flex-col.space-y-2')
                    
                    for section in sections:
                        try:
                            label = section.find_element(By.CSS_SELECTOR, 'div.text-xs.font-medium').text.strip()
                            if label in ['Output', 'Expected']:
                                content = section.find_element(By.CSS_SELECTOR, 'div.font-menlo').text
                                case_details[label] = content
                        except NoSuchElementException:
                            continue
                    
                    if case_details:
                        detailed_results.append(case_details)
                
                full_results = {
                    "result": result_text,
                    "cases": detailed_results
                }
            
            print(f"Test results retrieved: {full_results}")
            return full_results
        except TimeoutException:
            print("Timeout waiting for test results")
            return {"result": "Timeout waiting for test results", "cases": []}
        except Exception as e:
            print(f"An error occurred while getting test results: {str(e)}")
            return {"result": f"Error: {str(e)}", "cases": []}

    def submit_solution(self):
        print("Submitting solution...")
        try:
            submit_button = self.web.find_element(By.CSS_SELECTOR, 'button[data-e2e-locator="console-submit-button"]')  # Find the Submit button
            submit_button.click()  # Click the Submit button
            print("Solution submitted successfully.")
            time.sleep(5)  # Wait for submit sleep
            print("Sleeping for 5 seconds after submit.")
        except Exception as e:
            print(f"Error submitting solution: {str(e)}")
class ClaudeAPIIntegration:
    def __init__(self, api_key):
        print("Initializing Claude API...")
        self.client = anthropic.Anthropic(api_key=api_key)  # Initialize the Anthropic client with the provided API key
        print("Claude API initialized.")

    def send_prompt(self, prompt):
        print("Sending prompt to Claude API...", prompt)
        message = self.client.messages.create(
            model=CLAUDE_MODEL,  # Use the specified Claude model
            max_tokens=MAX_TOKENS,  # Set the maximum number of tokens for the response
            temperature=TEMPERATURE,  # Set the temperature for response generation
            messages=[
                {"role": "user", "content": prompt}  # Create a message with the user's prompt
            ]
        )
        response = self.extract_text_from_response(message.content)  # Extract the text from Claude's response
        print(f"Received response from Claude API: {response}...")
        return response

    @staticmethod
    def extract_text_from_response(response):
        print("Extracting text from Claude API response...")
        match = re.search(r"TextBlock\(text=(.*?), type='text'\)", str(response), re.DOTALL)  # Search for the text content in the response
        if match:
            text = match.group(1).strip('"').replace('\\"', '"')  # Extract and clean the text
            text = re.sub(r'```\w*\n?|```', '', text)  # Remove code block markers
            text = re.sub(r'`([^`\n]+)`', r'\1', text)  # Remove inline code markers
            text = text.replace('\\n', '\n')  # Replace escaped newlines with actual newlines
            return text.strip("'").strip()  # Remove any leading/trailing quotes and whitespace
        print("No text block found in response.")
        return ""

class CodeGenerationAndErrorHandling:
    def __init__(self, claude_api):
        self.claude_api = claude_api  # Store the ClaudeAPIIntegration instance

    def generate_code(self, problem_description, starting_code):
        print("Generating code for problem...")
        prompt = f"{STARTING_A_NEW_PROBLEM_PROMPT}\n\n{problem_description}\n\n{CODE_EXAMPLE_PREFIX}\n{starting_code}"  # Create a prompt for Claude to generate code
        return self.claude_api.send_prompt(prompt)  # Send the prompt to Claude and return the response

    def handle_error(self, problem_description, current_code, starting_code, error_message, error_info):
        print("Handling error and generating corrected code...")
        prompt = f"{SUBMITTING_A_CODE_ERROR_PROMPT}\n\n{problem_description}\n\n{ADVOCATE_FOR_BETTER_SOLUTION_ON_RETRY}\n{current_code}\n\nError Message:\n{error_message}\n\nDetailed Error Information:\n{error_info}\n\n{CODE_EXAMPLE_PREFIX}\n{starting_code}\n\n{END_OF_PROMPT_INSTRUCTIONS_FOR_CLEAR_RESPONSE}"  # Create a prompt for Claude to fix the code
        print("Prompt we're sending is: ", prompt)
        return self.claude_api.send_prompt(prompt)  # Send the prompt to Claude and return the response

def complete_individual_problem(leetcode, code_gen, problem_title):
    print(f"Starting to solve problem: {problem_title}")
    current_url = leetcode.web.current_url()
    if not current_url.startswith(LEETCODE_PROBLEM_URL_PREFIX):
        print("Error: Not on a LeetCode problem page")
        raise ValueError("Not on a LeetCode problem page")

    leetcode.web.ensure_python_language()  # Make sure Python is selected as the programming language
    problem_description = leetcode.get_problem_description()  # Get the problem description
    starting_code = leetcode.get_starting_code()  # Get the initial code provided by LeetCode

    for attempt in range(MAX_RETRIES):
        print(f"Attempt {attempt + 1} of {MAX_RETRIES}")
        if attempt == 0:
            code = code_gen.generate_code(problem_description, starting_code)  # Generate initial code solution
        else:
            code = code_gen.handle_error(problem_description, code, starting_code, results['result'], error_info)  # Generate fixed code based on previous error
        print(f"Code for attempt {attempt + 1}:\n{code}")
        leetcode.input_code(code)  # Input the generated code into LeetCode
        leetcode.run_code()  # Run the code
        print("Waiting for test results...")
        time.sleep(5)  # Wait for results
        results = leetcode.get_test_results()  # Get the test results

        print(f"Test Results:\n{results}")  # Print the full test results

        if results['result'] == "Accepted":
            print("Problem solved successfully!")
            leetcode.submit_solution()  # Submit the solution if it's accepted
            return True
        elif results['result'] == "Runtime Error":
            print(f"Runtime Error encountered. Error message: {results['error_message']}")
            error_info = f"Runtime Error:\n{results['error_message']}\nInput: {results['cases'][0]['Input']}"
        else:
            print(f"Error encountered. Attempting to fix...")
            error_info = "\n".join([f"Case {i+1}:\n" + "\n".join([f"{k}: {v}" for k, v in case.items()]) for i, case in enumerate(results['cases'])])

    print(f"Max retries reached. Adding problem '{problem_title}' to failed list and moving to next problem.")
    FAILED_PROBLEMS.add(problem_title)  # Add the problem to the failed problems set if max retries are reached
    return False

def navigate_to_new_problem(web_automation):
    global CURRENT_PAGE
    print(f"Navigating to problem set page {CURRENT_PAGE}...")
    web_automation.navigate_to(f"{LEETCODEFILTER}{CURRENT_PAGE}{LEETCODEPOSTFILTER}")  # Navigate to the problem set page
    
    while True:
        print(f"Waiting 5 seconds for problem list on page {CURRENT_PAGE} to load...")
        time.sleep(5)

        print("Waiting for problem list to load...")
        WebDriverWait(web_automation.driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, 'div[role="rowgroup"]'))
        )  # Wait for the problem list to load
        
        print("Selecting a random non-premium, non-failed problem...")
        problem_rows = web_automation.driver.find_elements(By.CSS_SELECTOR, 'div[role="row"]')  # Find all problem rows
        available_problems = []

        for row in problem_rows:
            cells = row.find_elements(By.CSS_SELECTOR, 'div[role="cell"]')
            if len(cells) >= 2:
                title_cell = cells[1]  # The title is in the second cell
                
                # Check if the problem is not premium and not failed
                title_link = title_cell.find_element(By.CSS_SELECTOR, 'a[href^="/problems/"]')
                if 'opacity-60' not in title_link.get_attribute('class') and title_link.text not in FAILED_PROBLEMS:
                    available_problems.append(title_link)
        
        if available_problems:
            random_problem = random.choice(available_problems)  # Choose a random problem from available problems
            problem_url = random_problem.get_attribute('href')
            problem_title = random_problem.text
            print(f"Selected problem: {problem_title} from page {CURRENT_PAGE}")
            print(f"Navigating to: {problem_url}")
            web_automation.navigate_to(problem_url)  # Navigate to the selected problem
            print("Waiting 5 seconds for problem page to load...")
            time.sleep(5)  # Wait for 5 seconds after navigating to the problem
            return problem_title
        else:
            print(f"No available problems on page {CURRENT_PAGE}. Attempting to go to next page...")
            next_button = web_automation.driver.find_element(By.XPATH, '//button[@aria-label="next"]')
            if next_button.is_enabled():
                next_button.click()  # Click the next page button if available
                CURRENT_PAGE += 1
                print(f"Navigating to page {CURRENT_PAGE}...")
                time.sleep(5)  # Wait for 5 seconds after clicking next
            else:
                print("No more pages available. Resetting to page 1 and falling back to 'Two Sum' problem...")
                CURRENT_PAGE = 1
                web_automation.navigate_to(f"{LEETCODE_PROBLEM_URL_PREFIX}two-sum")  # Navigate to the 'Two Sum' problem as a fallback
                print("Waiting 5 seconds for problem page to load...")
                time.sleep(5)
                return "Two Sum"

    # Ensure Python language is selected
    web_automation.ensure_python_language()
    
def main():
    global CURRENT_PAGE
    print("Starting LeetCode Solver...")
    web_automation = WebAutomation()  # Initialize the WebAutomation instance
    leetcode = LeetCodeInteraction(web_automation)  # Initialize the LeetCodeInteraction instance
    claude_api = ClaudeAPIIntegration(API_KEY)  # Initialize the ClaudeAPIIntegration instance with the API key
    code_gen = CodeGenerationAndErrorHandling(claude_api)  # Initialize the CodeGenerationAndErrorHandling instance

    # Use the new automated login method
    web_automation.login(LEETCODE_USERNAME, LEETCODE_PASSWORD)  # Log in to LeetCode using the provided credentials

    while True:
        try:
            problem_title = navigate_to_new_problem(web_automation)  # Navigate to a new problem
            if complete_individual_problem(leetcode, code_gen, problem_title):  # Attempt to solve the problem
                print(f"Successfully solved problem: {problem_title}. Moving to next problem...")
            else:
                print(f"Failed to solve problem: {problem_title}. Skipping to next problem...")
        except Exception as e:
            print(f"An error occurred: {e}")
            print("Attempting to continue with next problem...")
            # Reset to page 1 if an error occurs
            CURRENT_PAGE = 1

if __name__ == "__main__":
    main()  # Run the main function if this script is executed directly
