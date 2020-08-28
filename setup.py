import os
import sys
from setuptools import setup
from io import open
from johanna2 import __version__

with open('README.md') as readme_file:
    long_description = readme_file.read()

with open(os.path.join(os.path.dirname(__file__), 'requirements.in')) as f:
    required = f.read().splitlines()

setup(
    name='johanna2',
    version=__version__,
    packages=['johanna2'],
    install_requires=required,
    include_package_data=True,
    license='MIT License',
    description='make client vpn for aws server',
    long_description=long_description,
    long_description_content_type='text/markdown',
    classifiers=[
        'Environment :: Console',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3.8',
        'Framework :: Django :: 3.0',
        'Topic :: Internet :: WWW/HTTP',
    ],
)