import pathlib
from setuptools import setup

# The directory containing this file
HERE = pathlib.Path(__file__).parent

# The text of the README file
README = (HERE / "README.md").read_text()

# This call to setup() does all the work
setup(
    name="docker-lite-python",
    version="1.0.4",
    description="Sandbox running code in Docker.",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/jeff-vincent/docker-lite-python",
    author="Jeff Vincent",
    author_email="jeff.d.vincent@gmail.com",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
    ],
    packages=["docker_lite_python"],
    include_package_data=True,
    install_requires=["docker"]
)