from setuptools import find_packages, setup

install_requires = [
    "grpcio-tools>=1.58.0",
    "psutil",
    "pynvml",
    "urllib3<1.27,>=1.21.1",
    "deprecated",
]


extra_require = {
    "torch": ["torch"],
}


setup(
    name="sftrain",
    version="0.0.1",
    description="An Automatic Distributed Deep Learning Framework",
    install_requires=install_requires,
    extras_require=extra_require,
    python_requires=">=3.8",
    packages=find_packages(),
)
