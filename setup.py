from setuptools import setup, find_packages

# Load the README file as the long description
with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

setup(
    name= "kitikiplot",
    version= "0.1.7",
    author="Boddu Sri Pavan",
    author_email="boddusripavan111@gmail.com",
    description="A Python library to visualize categorical sliding window data.",
    long_description=long_description,
    long_description_content_type= "text/markdown",
    url="https://github.com/BodduSriPavan-111/kitikiplot",
    packages= find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",  # License type
        "Operating System :: OS Independent",
        "Topic :: Scientific/Engineering :: Visualization",
    ],
    project_urls={
        "Bug Tracker": "https://github.com/BodduSriPavan-111/kitikiplot/issues",
        "Documentation": "https://github.com/BodduSriPavan-111/kitikiplot/wiki",
        "Source Code": "https://github.com/BodduSriPavan-111/kitikiplot",
    },
    keywords=[ 
        "sliding window", 
        "sequential",
        "time-series",
        "genome", 
        "categorical data",
    ],
    license="LICENSE",
)