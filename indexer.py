# check all the question folder in the solutions folder, and format a index page for all the questions and their solutions in a index.md file

import os
import json


def list_questions():
    questions = []

    # Define the root directory for the questions
    root = "solutions"  # Update this to your actual path if needed

    # Iterate through each folder in the root directory
    for folder in os.listdir(root):
        folder_path = os.path.join(root, folder)
        if os.path.isdir(folder_path):

            solutions = []  # Store solution languages with paths
            # Get the solution language from the file names
            for file in os.listdir(folder_path):
                if file.endswith(".json"):  # Corrected the typo here
                    # Load the json file
                    with open(
                        os.path.join(folder_path, file), "r"
                    ) as f:  # Use the correct path
                        question_detail = json.load(f)  # Load the question detail data
                if not file.endswith(".json"):
                    # Extract the solution language and its file path
                    solution_language = file.split(".")[
                        0
                    ]  # Get the part before the first dot
                    solution_path = os.path.join(
                        folder_path, file
                    )  # Full path to the solution file
                    solutions.append(
                        (solution_language, solution_path)
                    )  # Store as a tuple

            questions.append(
                {
                    "frontend_question_id": question_detail["frontendQuestionId"],
                    "question_title_slug": question_detail["titleSlug"],
                    "question_title": question_detail["title"],
                    "difficulty": question_detail["difficulty"],
                    "paid_only": question_detail["paidOnly"],
                    "total_avaliable_languages": len(question_detail["codeSnippets"]),
                    "solutions": solutions,
                }
            )

    # Sort questions based on the frontend id, from small to large
    questions = sorted(questions, key=lambda x: int(x["frontend_question_id"]))
    return questions


def format_index_page(questions):
    section_header = "## Questions List"
    new_content = []

    # Create the new content for the questions list
    new_content.append(
        "| Number | Title | Difficulty | Paid | Solutions | Languages |\n"
    )
    new_content.append(
        "|---|---|---|---|---|---|\n"
    )  # Added missing columns in the separator
    for question in questions:
        # Create a string for the solutions with links to the files
        solutions_formatted = ", ".join(
            [f"[{lang[0]}]({lang[1]})" for lang in question["solutions"]]
        )
        new_content.append(
            f"| {question['frontend_question_id']} | [{question['question_title']}](https://leetcode.com/problems/{question['question_title_slug']}) | {question['difficulty']} | {question['paid_only']} | {solutions_formatted} | {len(question['solutions'])}/{question['total_avaliable_languages']} |\n"
        )
    new_content.append("\n")

    # Read the existing content of the index.md file
    with open("index.md", "r") as f:
        lines = f.readlines()
    # Find the index of the section header and replace its content
    for i, line in enumerate(lines):
        if line.startswith(section_header):
            # Find the next section header or end of file
            j = i + 1
            while j < len(lines) and not lines[j].startswith("## "):
                j += 1

            # Replace the content under the section header
            lines = (
                lines[: i + 2] + new_content + lines[j:]
            )  # +2 to skip the header and the next line
            break
    # Write the modified content back to the README.md file
    with open("index.md", "w") as f:
        f.writelines(lines)


if __name__ == "__main__":
    questions = list_questions()
    format_index_page(questions)
