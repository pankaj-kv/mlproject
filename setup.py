from setuptools import find_packages, setup

def get_requrements(filename):
    '''
    This function reads the requirements.txt file and returns a list of
    '''
    requirements = []
    with open(filename) as f:
        requirements = (f.readlines())
        requirements = [req.replace("\n", "") for req in requirements]
        if "-e ." in requirements:
            requirements.remove("-e .")
        return requirements
setup(
    name='mlproject',
    version='0.0.1',
    packages=find_packages(),
    author='pankaj',
    author_email='kvpankaj1999@gmail.com',
    install_requires=get_requrements('requirements.txt'),
   
)