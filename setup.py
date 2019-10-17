from setuptools import setup, find_packages

setup(
    name="colorium",
    version="0.0.0",
    description="Asset Management Tool for Autodesk Maya",
    author="Anthony Blanchette-Potvin",
    author_email="anthony.blanchette.potvin@gmail.com",
    package_dir={"": "src"},
    packages=find_packages("src")
)