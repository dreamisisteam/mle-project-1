#! /usr/bin/env python

from setuptools import setup, find_packages

with open('requirements/requirements.txt') as f:
    reqs = f.readlines()

setup(
    name='model-detection',
    version='0.0.1',
    description='Extension for object detection',
    url='https://github.com/dreamisisteam/mle-project-1',
    author='A. Korchevsky, A. Kozhukhov',
    packages=find_packages(),
    python_requires='>=3.9, <4',
    install_requires=reqs,
    license='proprietary and confidential',
    package_data={
        'model_detection': ['models/*.pt'],
    },
)
