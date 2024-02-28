from setuptools import setup, find_packages

setup(
    name='REFinPy',
    version='1.0.0',
    author='Juan Pablo Heusser',
    author_email='juanp.heusser@gmail.com',
    description='A package for real estate financial modeling',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown', 
    url='https://github.com/juanpheusser/REFinPy',  
    license='MIT',
    packages=find_packages(), 
    install_requires=[
        'numpy',
        'pandas',
        'scipy',
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Topic :: Office/Business :: Financial'
    ],
)