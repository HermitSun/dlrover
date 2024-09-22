from setuptools import find_packages, setup

install_requires = [
    "grpcio-tools>=1.58.0",
    "psutil",
    "pynvml",
    "urllib3<1.27,>=1.21.1",
    "deprecated",
]

setup(
    name="sftrain",
    version="0.0.1",
    description="SiFlow Distributed Training Plugin",
    install_requires=install_requires,
    python_requires=">=3.8",
    packages=find_packages(),
)
