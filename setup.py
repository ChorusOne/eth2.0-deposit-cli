from setuptools import find_packages, setup

"""
THIS IS A STUB FOR RUNNING THE APP
"""

setup(
    name="staking_deposit",
    version='2.0.0',
    py_modules=["staking_deposit", "staking_deposit.deposit"],
    packages=find_packages(exclude=('tests', 'docs')),
    include_package_data=True,
    package_data={'': ['intl/*/*', 'intl/*/cli/*', 'intl/*/utils/*', 'key_handling/key_derivation/word_lists/*']},
    python_requires=">=3.7,<4",
    # pin exact versions to prevent supply-chain attacks
    install_requires=[
        'py_ecc==5.1.0',
        'pycryptodome==3.9.8',
        'click==7.1.2',
        'ssz==0.2.4',
        'eth-typing==2.2.2',
        'eth-utils==1.9.5',
        'mypy-extensions==0.4.3',
        'lru-dict==1.1.6',
        'pyrsistent==0.16.1',
        'eth-hash==0.2.0',
        'cytoolz==0.11.2',
        'toolz==0.10.0',
        'six==1.15.0',
        'cached-property==1.5.2',
        'setuptools'
    ]
)
