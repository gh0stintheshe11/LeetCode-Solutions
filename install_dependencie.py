import sys
import subprocess

requirements_files = [
    'requirements.txt'
]

def install_requirements(requirements_file):
    """
    Installs the dependencies specified in the given requirements file.
    """
    python = sys.executable
    try:
        subprocess.check_call(
            [python, '-m', 'pip', 'install', '--upgrade', '-r', requirements_file],
            #stdout=subprocess.DEVNULL,
            #stderr=subprocess.DEVNULL  # Suppress error messages
        )
        print(f"Successfully installed requirements from {requirements_file}")
    except subprocess.CalledProcessError as e:
        print(f"Failed to install requirements from {requirements_file}. Error: {e}")

def install_all(requirements_files):
    for file in requirements_files:
        install_requirements(file)
    print(">>> All requirements checked <<<\n")

def main():
    install_all(requirements_files)

if __name__ == "__main__":
    main()