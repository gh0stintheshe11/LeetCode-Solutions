# check all the question folder in the solutions folder, and format a index page for all the questions and their solutions in a index.md file

import os

def list_questions():
    questions = []
    
    # Define the root directory for the questions
    root = 'solutions'  # Update this to your actual path if needed

    # Iterate through each folder in the root directory
    for folder in os.listdir(root):
        folder_path = os.path.join(root, folder)
        if os.path.isdir(folder_path):
            # Get the question number and title from the folder name
            question_number = folder.split('.')[0]
            question_title = folder.split('.')[1] if len(folder.split('.')) > 1 else ''
            solution_languages = []  # Store solution languages with paths
            
            # Get the solution language from the file names
            for file in os.listdir(folder_path):
                if not file.endswith('.json'):
                    # Extract the solution language and its file path
                    solution_language = file.split('.')[0]  # Get the part before the first dot
                    solution_path = os.path.join(folder_path, file)  # Full path to the solution file
                    solution_languages.append((solution_language, solution_path))  # Store as a tuple
            
            questions.append((question_number, question_title, solution_languages))
    
    # Sort the questions by the question number from 0 to 9999
    questions.sort(key=lambda x: int(x[0]))
    return questions


def format_index_page(questions):
    section_header = '## Questions list'
    new_content = []

    # Create the new content for the questions list
    new_content.append('| Number | Title | Solutions |\n')
    new_content.append('|---|---|---|\n')
    for question in questions:
        # Create a string for the solutions with links to the files
        solutions = ', '.join([f'[{lang[0]}]({lang[1]})' for lang in question[2]])
        new_content.append(f'| {question[0]} | [{question[1]}](https://leetcode.com/problems/{question[1]}) | {solutions} |\n')
    new_content.append('\n')

    # Read the existing content of the README.md file
    with open('README.md', 'r') as f:
        lines = f.readlines()

    # Find the index of the section header and replace its content
    for i, line in enumerate(lines):
        if line.startswith(section_header):
            # Find the next section header or end of file
            j = i + 1
            while j < len(lines) and not lines[j].startswith('## '):
                j += 1
            
            # Replace the content under the section header
            lines = lines[:i + 2] + new_content + lines[j:]  # +2 to skip the header and the next line
            break

    # Write the modified content back to the README.md file
    with open('README.md', 'w') as f:
        f.writelines(lines)


if __name__ == '__main__':
    questions = list_questions()
    format_index_page(questions)
