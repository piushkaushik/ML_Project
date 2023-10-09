from setuptools import find_packages, setup
from typing import List


HYPHEN_E_DOT= "-e ."
def get_requirements(file_path:str)->List[str]:
    """
    Desscription: This function is going to return list of requirement
    mention in requirement.txt file

    return This function is going to return a list which contain the name of libreries mentioned in requirements.txt
    """
    requirements=[]
    with open(file_path) as file_obj:
        requirements= file_obj.readlines()
        requirements= [req.replace("\n","") for req in requirements]

        if HYPHEN_E_DOT in requirements:
            requirements.remove(HYPHEN_E_DOT)

    return requirements
        

setup(
    name= "ML Project",
    version= '0.0.1',
    author= 'Piush',
    author_email= "piushsharma92@gmail.com",
    packages= find_packages(),
    install_requires= get_requirements('requirements.txt')
)

