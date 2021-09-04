from setuptools import setup, find_packages

setup(
    name="pynix",
    version='0.0.1',
    packages=find_packages(include=['pynix',
                                    'pynix.*'])
)
