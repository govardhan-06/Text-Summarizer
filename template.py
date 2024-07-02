import os
from pathlib import Path
import logging

project_name='text-Summarizer'

logging.basicConfig(level=logging.INFO,format='%(asctime)s - %(message)s',datefmt='%d-%b-%y %H:%M:%S')

# Path to the project directory
file_paths=[
    "src/__init__.py",
    "src/components/__init__.py",
    "src/utils/__init__.py",
    "src/utils/common.py",
    "src/logging/__init__.py",
    "src/config/__init__.py",
    "src/config/configuration.py",
    "src/pipeline/__init__.py",
    "src/entity/__init__.py",
    "src/constants/__init__.py",
    "config/config.yaml",
    "params.yaml",
    "app.py",
    "main.py",
    "Dockerfile",
    "requirements.txt",
    "setup.py",
    "research/trial.ipynb"
] 

for filepath in file_paths:
    filepath=Path(filepath)
    filedir,filename=os.path.split(filepath)

    if filedir!="":
        os.makedirs(f"{filedir}",exist_ok=True)
        logging.info(f"Created directory: {filedir} for file {filename}")
    
    if not os.path.exists(filepath) or os.path.getsize(filepath)==0:
        with open(filepath,"w") as f:
            f.write("")
            logging.info(f"Created empty file: {filename}")
        f.close()
    
    else:
        logging.info(f"File {filename} already exists")