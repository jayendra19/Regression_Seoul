from setuptools import find_packages,setup
from typing import List

HYPEN_E_DOT='-e .'
def get_requirements(file_path:str)->List[str]:
    '''
    file_path parameter, which should be the path to a requirements file (typically a file named requirements.txt 
    this function will return the list of requirements
    '''
    requirements=[]
    with open(file_path) as file_obj:
        '''it opens the specified file (file_path) in read mode using a with statement to ensure proper handling of the file.'''
        requirements=file_obj.readlines()
        '''reads all lines from the file using readlines()'''
        requirements=[req.replace("\n","") for req in requirements]
        '''removes newline characters ("\n") from the end of each line in the requirements list using a list comprehension.
        '''

        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)
            '''it checks if the constant HYPEN_E_DOT is in the requirements list. If it is, it removes that specific line from the list.'''
    
    return requirements

setup(
name='Regression_seoul',
version='0.0.1',
author='Jayendra yadav',
author_email='jayendrayadav2016@gmail.com',
packages=find_packages(),
install_requires=get_requirements('requirements.txt')

)