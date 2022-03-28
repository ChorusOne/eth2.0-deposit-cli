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
    install_requires=[
        'py_ecc>=5>,<6',
        'pycryptodome>=3>,<4',
        'click>=7>,<8',
        'ssz>=0.2,<0.3',
        'eth-typing>=2>,<3',
        'eth-utils>=1>,<2',
        'mypy-extensions>=0.4,<0.5',
        'lru-dict>=1>,<2',
        'pyrsistent>=0.16,<0.17',
        'eth-hash>=0.2,<0.3',
        'cytoolz>=0.11,<0.12',
        'toolz>=0.10,<0.11',
        'six>=1>,<2',
        'cached-property>=1>,<2',
    ]
)
