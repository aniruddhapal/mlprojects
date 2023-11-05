from setuptools import find_packages,setup
from typing import List

HYPHEN_e_dot='-e .'

def get_requirements(file_path:str)->List[str]:
    '''
    this function will return the list of requirements
    '''
    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace('/n',"") for req in requirements]

        if HYPHEN_e_dot in requirements:
            requirements.remove(HYPHEN_e_dot)
    
    return requirements

setup(
name='mlprojetcs',
version='0.0.1',
author='Aniruddha Pal',
author_email='aniruddhapal@gmail.com',
packages=find_packages(),
install_requires=get_requirements('requirements.txt')
)