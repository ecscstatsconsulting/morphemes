from setuptools import setup
from pathlib import Path

this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()

setup(
    name='morphemes',
    long_description_content_type='text/markdown',
    long_description=long_description,
    keywords="morpheme, morphology, nlp",
    version='1.1.01',
    install_requires=[
        "pandas>=1.4.1",
        "requests>=2.27.1",
        "tinydb>=4.7.0",
        "openpyxl>=3.0.9",
    ],
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
