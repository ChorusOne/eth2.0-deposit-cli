from setuptools import find_packages, setup

"""
THIS IS A STUB FOR RUNNING THE APP
"""

setup(
    name="staking_deposit",
    version='2.0.0',
    py_modules=["staking_deposit", "staking_deposit.deposit"],
    packages=find_packages(exclude=('tests', 'docs')),
    python_requires=">=3.7,<4",
)
