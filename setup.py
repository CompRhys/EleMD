import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="EleMD",
    version="0.0.1",
    author="Rhys Goodall",
    author_email="reag2@cam.ac.uk",
    description="EleMD",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/comprhys/EleMD",
    packages=['EleMD'],
    package_dir={'EleMD': 'EleMD'},
    classifiers=[
        "Programming Language :: Python :: 3.6",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)