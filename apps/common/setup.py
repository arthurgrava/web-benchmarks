import os.path
from setuptools import setup, find_packages

requirements = open("requirements.txt").read().split()
version = "0.0.1"

setup(
    name="bechmark_common",
    version=version,
    url="https://github.com/arthurgrava/web-benchmarks",
    license="None",
    author="Arthur Grava",
    author_email="arthur.grava@gmail.com",
    description="Common packages for my benchmarks",
    packages=find_packages(),
    install_requires=requirements,
)
