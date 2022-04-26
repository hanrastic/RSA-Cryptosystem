# Testing Documentation

## Report
All the core functionality is tested. Such as;
- The generation of prime numbers
- Testing the primality
- Encrypting a message and decrypting a message

The user interface is left out from testing since the focus of the project is on the algorithmic processes.

## Coverage report
Testing coverage report can be found here: [![Codecovista](https://codecov.io/gh/hanrastic/RSA-Cryptosystem/branch/main/graph/badge.svg?token=38QC8NMU4G)](https://codecov.io/gh/hanrastic/RSA-Cryptosystem)

## How to run the tests
Download the .zip file. Move to the root of the directory and run the following bash commands:

```bash
    poetry install;poetry shell
```

```bash
    cd src;coverage run --branch -m pytest; coverage report -m
```
