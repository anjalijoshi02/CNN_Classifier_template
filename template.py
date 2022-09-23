import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO,format='[%(asctime)s]:%(message)s:')


package_name="deepClassifier"

list_of_files=[ 
    "github/worlflows/.gitkeep",
    f"src/{package_name}/__init__.py",
    f"src/{package_name}/components/__init__.py",
    f"src/{package_name}/constants/__init__.py",
    f"src/{package_name}/utils/__init__.py",
    f"src/{package_name}/config/__init__.py",
    f"src/{package_name}/pipeline/__init__.py",
    f"src/{package_name}/entity/__init__.py",
    "tests/__init__.py",
    "tests/unit/__init__.py",  # if you have created any class and you want to test that single unit , then it is called unit test
    "tests/integration/__init__.py",  ## suppose you have created a pipeline, so to check if that pipeline will work all together , that will be checked with the help of integration testing
    "configs.config.yaml",
    "dvc.yaml",
    "params.yaml",
    "init_setup.sh",
    "requirements.txt",
    "requirements_dev.txt",
    "setup.py",
    "setup.cfg",
    "pyproject.toml",
    "tox.ini",   # it is used for testing of the files locally
    "reseach/trials.ipynb"

]

for filepath in list_of_files:
    filepath=Path(filepath)
    filedir,filename=os.path.split(filepath)

    # some of the filenames contain name of the directory also, so we use os.path.split function to 
    # get the directory name and the file name separately

    if filedir !="":
        os.makedirs(filedir,exist_ok=True)
        logging.info(f"Creating directory :{filedir} for file {filename}")

    if ( not os.path.exists(filepath)) or (os.path.getsize(filepath)==0):
        with open(filepath,"w") as f:
            pass # create an empty file
            logging.info(f"Creating empty file:{filepath}")
    else:
        logging.info(f"{filename} already exists")

