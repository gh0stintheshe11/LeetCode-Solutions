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
    with open('index.md', 'w') as f:
        f.write('# LeetCode Solutions\n\n')
        f.write('|Number|Title|Solutions|')
        f.write('\n')
        f.write('|---|---|---|')
        f.write('\n')
        for question in questions:
            # Create a string for the solutions with links to the files
            solutions = ', '.join([f'[{lang[0]}]({lang[1]})' for lang in question[2]])
            f.write(f'|{question[0]}|[{question[1]}](https://leetcode.com/problems/{question[1]})|{solutions}|')
            f.write('\n')

#if __name__ == '__main__':
#    questions = list_questions()
#    format_index_page(questions)
