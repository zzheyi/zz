#!/usr/bin/env python

"""The setup script."""

from setuptools import setup, find_packages

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

requirements = [ ]

test_requirements = [ ]

setup(
    author="Zheyi Zeng",
    author_email='zz3155@columbia.edu',
    python_requires='>=3.6',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
    description="The Allergy-Safe Recipe Explorer is a Python package designed to facilitate easy access to recipes and nutritional information, specifically catering to individuals with food allergies. This package will utilize the Spoonacular API to provide users with recipes that are safe for their specific dietary needs, offering advanced filtering, nutritional breakdowns, cost estimations, and more.",
    entry_points={
        'console_scripts': [
            'recipes_search=recipes_search.cli:main',
        ],
    },
    install_requires=requirements,
    license="MIT license",
    long_description=readme + '\n\n' + history,
    include_package_data=True,
    keywords='recipes_search',
    name='recipes_search',
    packages=find_packages(include=['recipes_search', 'recipes_search.*']),
    test_suite='tests',
    tests_require=test_requirements,
    url='https://github.com/zzheyi/recipes_search',
    version='0.1.0',
    zip_safe=False,
)
