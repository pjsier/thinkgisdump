from setuptools import find_packages, setup

from thinkgisdump import __version__

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()


setup(
    name="thinkgisdump",
    version=__version__,
    license="MIT",
    author="Pat Sier",
    author_email="pjsier@gmail.com",
    description="Command line tool for scraping GeoJSON from ThinkGIS sites",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/pjsier/thinkgisdump",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    packages=find_packages(exclude=("tests",)),
    install_requires=["requests", "lxml", "geojson-rewind"],
    tests_requires=["black", "flake8", "isort", "pytest"],
    python_requires=">=3.6, <4.0",
    entry_points={"console_scripts": ["thinkgis2geojson=thinkgisdump.cli:main"]},
)
