from setuptools import setup, find_packages

setup(
    name="UIProject",          # Name of your project/package
    version="0.1",             # Version
    packages=find_packages(),  # Automatically find all packages
    install_requires=[
        "selenium",
        "pytest",
        "pytest-rerunfailures",
        "python-dotenv",
        "webdriver-manager"
    ],
)