Pykins
======

Python API and CLI for Jenkins in one package :)

Installation
------------

A virtual environment is recommended for development.
To install the latest version of `pykins`, run the following commands:

    virtualenv .venv && source .venv/bin/activate
    pip install .

To install from PyPi (not necessarily latest version!):

    pip install pykins

Python API Examples
-------------------
```python
>>> import pykins
>>> jenkins = pykins.Jenkins('http://my_jenkins')
>>> print(jenkins.get_jobs())
```
