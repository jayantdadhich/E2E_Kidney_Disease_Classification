import os
from pathlib import Path
import logging

#logging string
logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s:')

project_name = 'cnnClassifier'

list_of_files = [
    ".github/workflows/.gitkeep",               #Whenever we are creating folder and is blank and we commit, it will not upload that. We will remove this when we use CI-CD pipeline
    f"src/{project_name}/__init__.py",                  
    f"src/{project_name}/components/__init__.py",
    f"src/{project_name}/utils/__init__.py",
    f"src/{project_name}/config/__init__.py",
    f"src/{project_name}/config/configuration.py",
    f"src/{project_name}/pipeline/__init__.py",
    f"src/{project_name}/entity/__init__.py",
    f"src/{project_name}/constants/__init__.py",
    "config/config.yaml",
    "dvc.yaml",
    "params.yaml",
    "requirements.txt",
    "setup.py",
    "research/trials.ipynb",        # jupyter notebook experimentation
    "templates/index.html",         # flask 
]

for filepath in list_of_files:
    filepath = Path(filepath)   # detect OS and converts this path to the specific OS(eg WINDOWS)
    filedir, filename = os.path.split(filepath)     # splitting the path and filename

    if filedir !="":
        os.makedirs(filedir, exist_ok=True)     # create folder, If folder already there, it won't create.
        logging.info(f"Creating directory; {filedir} for the file: {filename}")      

    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):      
        with open(filepath, "w") as f:
            pass
            logging.info(f"Creating empty file: {filepath}")

    else:
        logging.info(f"{filename} is already exists")

