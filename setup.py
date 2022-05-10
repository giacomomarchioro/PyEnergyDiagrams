import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="pyenergydiagram",
    version="0.1.8",
    author="Giacomo Marchioro",
    author_email="giacomomarchioro@outlook.com",
    description="A tool for plotting Energy Diagrams using Matplotlib.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/giacomomarchioro/PyEnergyDiagrams",
    packages=setuptools.find_packages(),
    install_requires=open("requirements.txt", "r").readlines(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
