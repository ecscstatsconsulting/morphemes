from setuptools import setup
from pathlib import Path

this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()

setup(
    name='morphemes',
    long_description_content_type='text/markdown',
    long_description=long_description,
    version='1.0.1',
    packages=['morphemes', 'morphemes.utilities', 'morphemes.utilities.morpheme_database'],
    url='',
    license='MIT',
    author='Paul Warren',
    author_email='paul0warren3@gmail.com',
    description="""Look up method for identifying morphemes"""
)
