# setup.py
from setuptools import setup, find_packages

setup(
    name="localead_backend",
    version="0.1",
    packages=find_packages(include=["backend", "backend.*"]),
)
