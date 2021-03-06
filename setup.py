# -*- coding: utf-8 -*-

# DO NOT EDIT THIS FILE!
# This file has been autogenerated by dephell <3
# https://github.com/dephell/dephell

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

import os.path

readme = ''
here = os.path.abspath(os.path.dirname(__file__))
readme_path = os.path.join(here, 'README.rst')
if os.path.exists(readme_path):
    with open(readme_path, 'rb') as stream:
        readme = stream.read().decode('utf8')

setup(
    long_description=readme,
    name='git-name',
    version='0.1.0',
    description='a cli and python package for naming hashes',
    python_requires='==3.*,>=3.5.0',
    project_urls={
        "homepage": "https://github.com/CircArgs/git-name",
        "repository": "https://github.com/CircArgs/git-name"
    },
    author='CircArgs',
    author_email='quebecname@gmail.com',
    license='GPL-3.0',
    keywords='git commit hash naming',
    entry_points={"console_scripts": ["git-name = git_name.cli:main"]},
    packages=['git_name', 'git_name.git_name'],
    package_dir={"": "."},
    package_data={"git_name.git_name": ["*.csv", "*.txt"]},
    install_requires=['inflect==4.*,>=4.1.0'],
    extras_require={
        "dev": [
            "black==19.*,>=19.10.0.b0", "dephell==0.*,>=0.8.3",
            "pytest==6.*,>=6.0.1"
        ]
    },
)
