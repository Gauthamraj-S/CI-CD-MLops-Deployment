from setuptools import find_packages,setup
from typing import List

HYPHEN_E_DOT = '-e .'

def get_requirements(file_path: str) -> List[str]:
    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readline()
        requirements=[req.replace("\n","") for req in requirements]
        if(HYPHEN_E_DOT in requirements):
            requirements.remove(HYPHEN_E_DOT)s
    return requirements

setup(
    name='ML project',
    version = '0.0.1',
    author = 'Gautham Raj S',
    author_email='sgauthamraj4@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')

)