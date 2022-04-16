from setuptools import setup, find_packages
import os 
here = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(here, "README.md"), encoding="utf-8") as f:
    long_description = f.read()

setup(
    name='bankingapp',
    version="0.0.1",
    description="A sample banking app",
    long_description=long_description,
    url="https://github.com/AlexBowmanCoding/Sample-Banking-App",
    author="Alex Bowman",
    author_email="alex@itsabox.net",
    packages=["bankingapp"]
)