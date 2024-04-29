from setuptools import find_packages , setup
from typing import List

def get_req(file_path : str) -> List[str] :  
        requirements=[]
        with open(file_path) as file_obj:
             requirements=file_obj.readlines()
             requirements = [req.replace("\n" , "")for req in requirements]
         
       

        return requirements
    

setup(
    
    name='DPP' ,
    version='0.0.1' ,
    author='kartik' , 
    author_email='kartikpatekar27@gmail.com' , 
    install_requires = get_req('requirements.txt') , 
    packages=find_packages()
    
)
