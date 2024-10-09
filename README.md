# LeetCode Solver Bot

## Description

LeetCode Solver Bot is an automated tool designed to solve LeetCode problems using AI-powered code generation. It interacts with the LeetCode platform to fetch problems, generate solutions, submit them, and handle debugging if necessary.

## Features

- Automated login to LeetCode using GitHub authentication
- Fetching unsolved LeetCode problems
- AI-powered solution generation using GPT-4
- Automated solution submission and testing
- Debugging capabilities for failed submissions
- Support for multiple programming languages (currently focused on Python)

## Code Structure

- `solver_dev.py`: Main script containing all the core functionality
- `.env`: Environment variables (not tracked in git)
- `requirements.txt`: List of dependencies
- `install_dependencies.sh`: Script to install dependencies

## Installation

1. Clone the repository:
   ```
   git clone https://github.com/yourusername/LeetCode-Solver-Bot.git
   cd LeetCode-Solver-Bot
   ```

2. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

3. Set up environment variables:
   Create a `.env` file in the root directory with the following content:
   ```
   LEETCODE_USERNAME=your_github_username
   LEETCODE_PASSWORD=your_github_password
   OPENAI_API_KEY=your_openai_api_key
   ```

## Usage

To start the LeetCode Solver Bot, run:

```
python solver.py
```

The bot will automatically:
1. Log in to LeetCode
2. Find the next unsolved problem
3. Generate a solution using GPT-4
4. Test the solution
5. Submit the solution if tests pass
6. Debug and retry if the solution fails

## Contributing

Contributions to the LeetCode Solver Bot are welcome!

## Disclaimer

This tool is for educational purposes only. Please use it responsibly and in accordance with LeetCode's terms of service.