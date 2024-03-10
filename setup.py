from setuptools import find_packages,setup

 

setup(
    name='ML project',
    version = '0.0.1',
    author = 'Gautham Raj S',
    author_email='sgauthamraj4@gmail.com',
    packages=find_packages(),
    install_requires=['pandas','numpy','seaborn']

)