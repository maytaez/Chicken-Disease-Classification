import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO,format='[%(asctime)s]:%(message)s:')

project_name="cnnClassifier"

#%% Project folders
list_of_files=[
    '.github/workflows/.gitkeep',
    f'src/{project_name}/__init__.py',
    f'src/{project_name}/components/__init__.py',
    f'src/{project_name}/utlis/__init__.py',
    f'src/{project_name}/config/__init__.py',
    f'src/{project_name}/config/components/__init__.py',
    f'src/{project_name}/pipeline/__init__.py',
    f'src/{project_name}/entity/__init__.py',
    f'src/{project_name}/constants/__init__.py',
    "config/config.yaml",
    "dvc.yaml",
    "params.yaml",
    "requirements.txt",
    "setup.py",
    "research/trails.ipynb"
    ]

for filepath in list_of_files:
    filepath = Path(filepath)

    #saparate folder and filename
    filedir,filename=os.path.split(filepath)

    # if directory is already created
    if filedir!="":
        os.makedirs(filedir,exist_ok=True)
        logging.info(f'Creating directory:{filedir} for the file {filename}')

    # There are also some files inside the directory
    if (not os.path.exists(filepath)) or (os.path.getsize(filepath)==0):
        # if this file exists then we won't create it and also checking if the file is empty or not
        #file isn't there
        with open(filepath,"w") as f:
            pass
            
            logging.info(f"Creating empty file :{filepath}")

    else: #if file already exist
        logging.info(f'{filename} already exists')



