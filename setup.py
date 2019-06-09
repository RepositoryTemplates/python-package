from setuptools import setup, find_packages
from codecs import open

with open("README.rst", "r", "utf-8") as f:
    readme = f.read()

with open("requirements.txt", "r", "utf-8") as f:
    requirements = f.readlines()

setup(
    name="python-package",
    version="1.0.0",
    description="A Python package library template.",
    long_description=readme,
    url="https://github.com/RepositoryTemplates/python-package",
    author="k3rn31p4nic",
    license="MIT",
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "License :: OSI Approved :: MIT License",
        "Intended Audience :: Developers",
        "Natural Language :: English",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Topic :: Internet",
        "Topic :: Software Development :: Libraries",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Utilities",
    ],
    keywords="api wrapper library",
    packages=find_packages(),
    install_requires=requirements,
    python_requires=">=2.7, !=3.0.*, !=3.1.*, !=3.2.*, !=3.3.*, !=3.4.*, <4",
)
