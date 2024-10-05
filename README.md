# LeetCode Solutions

## Overview

The **LeetCode Solutions** is a collection of all LeetCode solutions for practice and learning purposes.

The solutions are stored in the [solutions directory](./solutions). Github can will omit folders after 1000, but you can still use search to go to sepecific question folder.

## Automation

The [retriver.py](./retriver.py) is a python script that automates the process of fetching and storing solutions to LeetCode problems. 

- Fetches all solved questions from LeetCode.
- Retrieves detailed information about each question, including hints and example test cases.
- Collects the fastest accepted submissions for each question in multiple programming languages.
- Saves question details and submission codes in a structured format within a designated folder.
  
## Setup

1. **Clone the Repository**

   Clone this repository to your local machine:

   ```bash
   git clone https://github.com/yourusername/LeetCode-Solutions.git
   cd LeetCode-Solutions
   ```

2. **Environment Variables**

   Create a `.env` file in the root directory of the project to store your github credentials:

   ```plaintext
   LEETCODE_USERNAME=your_github_username
   LEETCODE_PASSWORD=your_github_password
   ```

   Replace `your_github_username` and `your_github_password` with your actual github credentials.

   the reason for using github is we need to by pass the bot detection of LeetCode. Using 3rd party login like github is a good way to do so.

## Usage

1. **Run the Script**

   To start the retrieval process, run the `retriver.py` script:

   ```bash
   python retriver.py
   ```

   This will:
   - Fetch all solved questions.
   - Retrieve details for each question.
   - Save the question details and submission codes in the `solutions` directory.

## Directory Structure

```
LeetCode-Solutions/
│
├── retriver.py          # Main script to retrieve solutions
├── check.py             # Script to clean up empty files and directories
├── .env                 # Environment variables for credentials
└── solutions/           # Directory where solutions are stored
    ├── 745.find-smallest-letter-greater-than-target/
    │   ├── question.json
    │   ├── C.cpp
    │   ├── Python.py
    │   └── ...
    └── ...
```