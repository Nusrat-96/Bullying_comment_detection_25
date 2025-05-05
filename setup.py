#initially that I require in the setup file

from setuptools import find_packages, setup

from typing import List

#constant creation
HYPEN_E_DOT = '-e .'


def get_requirements(file_path:str) -> List[str]:

    """
        This function will return the list of requirements
    """

    requirements = []

    with open (file_path) as file_obj:
        requirements = file_obj.readlines()
        print(requirements)
        requirements = [req.replace("\n", " ") for req in requirements]    
        #list comprehension to remove \n in the requrements.text file in the end of each line with " "

        #to automatically connect when in the requirement text file see -e . it connect with the setup.py file 
        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)
    
    return requirements




setup(
name = 'Bullying_detection',
version= '0.0.1',
author = "Nusrat",
author_email= "nusratadiba88@gmail.com",
packages=find_packages(),
#install_requires = ['pandas', 'numpy', 'seaborn']
install_requires = get_requirements("requirements.txt")

)