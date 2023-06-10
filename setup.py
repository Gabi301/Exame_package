from codecs import open
from os.path import join, abspath, dirname
from setuptools import setup, find_packages
import os

requirementPath = 'requirements.txt'
install_requires = [] 

if os.path.isfile(requirementPath):
    with open(requirementPath) as f:
        install_requires = f.read().splitlines()

here = abspath(dirname(__file__))



setup(
    name="Exame_package",
    version="0.1",
    description="Exame_Package mods",
    license='MIT',
    packages=find_packages(exclude=['test']),
    include_package_data=True,
    install_requires=install_requires
)