import os

project_root = ""

# Define the directory structure
directories = [
    "data/raw",
    "data/processed",
    "code/notebooks",
    "code/scripts",
    "models",
    "logs",
    "config",
    "deploy",
    "tests",
]

# Create the directories and add .gitkeep files if they don't already exist
for directory in directories:
    full_path = os.path.join(project_root, directory)
    if not os.path.exists(full_path):
        os.makedirs(full_path)
    gitkeep_file = os.path.join(full_path, ".gitkeep")
    if not os.path.exists(gitkeep_file):
        open(gitkeep_file, 'w').close()

print("Project structure and .gitkeep files created or already exist.")
