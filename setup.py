import os
from setuptools import setup, find_packages

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name = "dupremove",
    version = "1.0",
    author = "Devansh Raghav",
    author_email = "indiananonymous75@gmail.com",
    description = ("Remove duplicates"),
    license = "MIT",
    keywords = ["dupremove", "Bug Bounty", "pentesting", "security", "hacking"],
    url = "https://github.com/DevanshRaghav75/dupremove",
    packages=find_packages(),
    long_description=read('README.md'),
    classifiers=[
        "Intended Audience :: Developers",
        "Intended Audience :: Information Technology",
        "Topic :: Security",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python",
    ],
    entry_points={
        'console_scripts': [
            'dupremove = dupremove.dupremove:main'
        ]
    },
)
