# General utily functions for HDI data parsing
# Developer: Joshua M. Hess, BSc
# Developed at the Vaccine & Immunotherapy Center, Mass. General Hospital

# Import setuptools
from setuptools import setup

# Extract readme information
with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

# Pip setup
setup(
    name='hdi-utils',
    version='0.1.0',
    description='General utily functions for high-dimensional image data',
    author='Joshua Hess',
    author_email='joshmhess12@gmail.com',
    license='MIT',
    packages=['hdi-utils'],
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/JoshuaHess12/hdi-utils",
    project_urls={
        "Bug Tracker": "https://github.com/JoshuaHess12/hdi-utils/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.6",
)
