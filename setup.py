from setuptools import setup
from pathlib import Path

this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()

setup(
    name='morphemes',
    long_description_content_type='text/markdown',
    long_description=long_description,
    version='1.0.6',
    packages=['morphemes', 'morphemes.utilities', 'morphemes.utilities.morpheme_database'],
    url='',
    license='MIT',
    author='Enkeleda Cuko & Paul Warren',
    author_email='ecsctechdepartment@gmail.com',
    description="""A practical Python Library for identifying morphemes in the english language."""
)
