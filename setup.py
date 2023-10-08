from setuptools import setup
from typing import List

#Declaring variables for setup functions

PROJECT_NAME="housing-predictor"
VERSION= "0.0.1"
AUTHOR= "Piush Sharma"
DESCRIPTION= "This is a project for housing price prediction"
PACKAGES= ["housing"]
REQUIREMENT_FILE_NAME= "requirements.txt"

def get_requirements_list()->List[str]:
    """
    Desscription: This function is going to return list of requirement
    mention in requirement.txt file

    return This function is going to return a list which contain the name of libreries mentioned in requirements.txt
    """
    with open(REQUIREMENT_FILE_NAME) as requirement_file:
        return requirement_file.readlines()

setup(
    name= PROJECT_NAME,
    version= VERSION,
    author= AUTHOR,
    description= DESCRIPTION,
    packages= PACKAGES,
    install_requires= get_requirements_list()
)
