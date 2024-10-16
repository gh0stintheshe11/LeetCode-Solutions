# LeetCode Solutions

This repo archives all solutions for all LeetCode problems in all available languages. (continous updating...)

## Table of Contents
- [Questions list](#questions-list)
- [Automation Tools](#automation-tools)
- [Contributing](#contributing)
- [Disclaimer](#disclaimer)

## [Questions list](index.md)

> [!NOTE]
> The question list has to be put in an separate [index.md](index.md) file. It is impossible to list all questions in the readme.md since github only display first 500KB of the readme file :(

## Automation Tools

- [Solver](#solver)
- [Retriver](#retriver)

### Installation

1. Clone the repository:
   ```
   git clone https://github.com/yourusername/LeetCode-Solutions.git
   cd LeetCode-Solutions
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

> [!IMPORTANT]\
> Solver uses OpenAI's GPT-4o model to generate solutions so you need to set up your OpenAI API key in the ```.env``` file. Alternatively, you can modify the code to use any model you want.

> [!IMPORTANT]\
> Both Solver and Retriver use the github login method to login to LeetCode so you need to set up your github login credentials in the ```.env``` file.

### [Solver](#solver)

Solver is an automated script designed to solve LeetCode problems using AI-powered code generation. It interacts with the LeetCode platform to fetch problems, generate solutions, submit them, and handle debugging if necessary.

- Use ```python solver.py``` to run the solver.

The solver will automatically:
1. Log in to LeetCode
2. Find the next unsolved problem
3. Generate a solution using GPT-4
4. Test the solution
5. Submit the solution if tests pass
6. Debug and retry if the solution fails

### [Retriver](#retriver)

Retriver is an automated script designed to fetch solved LeetCode problems and solutions from the LeetCode platform, then archives the problem details and solutions.

- Use ```python retriver.py``` to run the retriver.

The retriver will:
1. Log in to LeetCode
2. Fetch all solved problems
3. Archive the problem details and solutions

## Contributing

Contributions are welcome!

## Disclaimer

This tool is for educational purposes only. Please use it responsibly and in accordance with LeetCode's terms of service.
