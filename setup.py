import pathlib
from setuptools import setup

# The directory containing this file
HERE = pathlib.Path(__file__).parent

# The text of the README file
README = (HERE / "README.md").read_text()

VERSION = '1.0.0'

# This call to setup() does all the work
setup(
    name="coolab",
    version="1.0.0",
    description="Instantly working cool apps you can use on Google Colab!",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/songlinhou/coolab",
    author="Ray Hou",
    author_email="songlinhou1993@gmail.com",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Operating System :: Linux"
    ],
    packages=["coolab"],
    include_package_data=True,
    install_requires=["pyngrok", "pylint"],
    entry_points={
        # "console_scripts": [
        #     "realpython=reader.__main__:main",
        # ]
    },
)