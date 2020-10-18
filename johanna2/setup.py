import os
import sys
from setuptools import setup
from io import open
from johanna2 import __version__

with open('README.md') as readme_file:
    long_description = readme_file.read()

with open(os.path.join(os.path.dirname(__file__), 'requirements.in')) as f:
    required = f.read().splitlines()

with open(os.path.join(os.path.dirname(__file__), 'test_requirements.in')) as f:
    test_required = f.read().splitlines()

setup(
    name='johanna2',
    version=__version__,
    packages=['johanna2'],
    install_requires=required,
    tests_require=test_required,
    test_suite='nose.collector',
    include_package_data=True,
    license='MIT License',
    description='Python Web Services for VPC',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/JoosJuliet/johanna2',
    author='Joos',
    author_email='saven7788@gmail.com',
    entry_points={
        'console_scripts': [
            'johanna=johanna.cli:handle',
            'j=johanna.cli:handle',
        ]
    },
    classifiers=[
        'Environment :: Console',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Framework :: Django',
        'Framework :: Django :: 1.11',
        'Framework :: Django :: 2.0',
        'Framework :: Django :: 3.0',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    ],
)