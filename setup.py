import setuptools
from os import path

this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, "README.md"), encoding="utf-8") as f:
    long_description = f.read()

setuptools.setup(
    name="vofotensors",
    version="1.0.4",
    author="Julian Karl Bauer",
    author_email="juliankarlbauer@gmx.de",
    description="V(ariety)O(f)F(iber)O(rientation)TENSORS "
    "contains selected contributions of "
    "Bauer JK, Böhlke T. Variety of fiber orientation tensors. "
    "Mathematics and Mechanics of Solids. 2022. "
    "doi:10.1177/10812865211057602",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/JulianKarlBauer/fiber_orientation_tensors_2021",
    packages=["vofotensors"],
    package_dir={"vofotensors": "vofotensors"},
    install_requires=[
        "numpy",
        "sympy",
        "pandas",  # Required for example s003...
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
)
