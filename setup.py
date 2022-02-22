from setuptools import setup
from pathlib import Path

with open('requirements.txt') as f:
    required = f.read().splitlines()

this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()

setup(
    name='morphemes',
    long_description_content_type='text/markdown',
    long_description=long_description,
    keywords="morpheme, morphology, nlp",
    version='1.0.9',
    install_requires=required,
    packages=['morphemes', 'morphemes.utilities', 'morphemes.utilities.morpheme_database'],
    url='https://github.com/ecscstatsconsulting/morphemes',
    license='MIT',
    author='Enkeleda Cuko & Paul Warren',
    author_email='ecsctechdepartment@gmail.com',
    description="""A practical Python Library for identifying morphemes in the english language.""",
    project_urls={
        'Documentation': 'https://github.com/ecscstatsconsulting/morphemes#readme',
        'Source': 'https://github.com/ecscstatsconsulting/morphemes',
        'Tracker': 'https://github.com/ecscstatsconsulting/morphemes/issues',
    }
)
