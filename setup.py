from setuptools import setup, find_packages

with open("README.md","r") as f:
    description=f.read()
setup(
    name='peccipy',
    version='0.0.2', 
    packages=find_packages(),  
    install_requires=[ 
        'pandas',
        'numpy',
    ],
    entry_points={  
        'console_scripts': [
            'peccipy_hello = peccipy.main:hello',
        ],
    },
    author='Ashik Nazar',
    author_email='datas293@gmail.com',
    description='A package for data preprocessing tasks.',
    long_description=description,
    long_description_content_type='text/markdown',
    url='https://github.com/ashiknazar/peccipy',  
)












from setuptools import setup, find_packages

setup(
    name='peccipy',
    version='0.0.1',
    packages=find_packages(),
    install_requires=[
        'pandas',
        'numpy',
    ],
    entry_points={
        'console_scripts': [
            'peccipy_hello = peccipy.main:hello',
        ],
    },
    author='Ashik Nazar',
    author_email='datas293@gmail.com',
    description='A package for data preprocessing tasks.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/ashiknazar/peccipy',
)
