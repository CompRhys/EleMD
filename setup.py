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
    install_requires=[
        "numpy",
        "pymatgen",
        "POT",
    ],
    extras_require={
        "test": ["pytest", "ElMD"],
        "examples": ["scikit-learn", "umap-learn"]
    },
    classifiers=[
        "Programming Language :: Python :: 3.6",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
