import setuptools

setuptools.setup(
    name="vofotensors",
    version="0.0.1",
    author="Julian Karl Bauer",
    author_email="juliankarlbauer@gmx.de",
    description="V(ariety)O(f)F(iber)O(rientation)TENSORS "
    "contains selected contributions of "
    "Bauer JK, Böhlke T. Variety of fiber orientation tensors. "
    "Mathematics and Mechanics of Solids. December 2021. "
    "doi:10.1177/10812865211057602",
    url="https://github.com/JulianKarlBauer/fiber_orientation_tensors_2021",
    packages=["vofotensors"],
    package_dir={"vofotensors": "vofotensors"},
    install_requires=[
        "numpy",
        "sympy",
        # "mechkit>=0.2.6",
    ],
    # setup_requires=["pybind11>=2.3", "libcgal-dev", "libeigen3-dev"],
    # extras_require={"test": ["pytest", "natsort"]},
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
)
