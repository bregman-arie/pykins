## Pykins

Yet another CLI for Jenkins.
Pykins provides you with:

  * The ability to analyze builds

### Installation

A virtual environment is recommended for development.
To install the latest version of `pykins`, run the following commands:

    virtualenv .venv && source .venv/bin/activate
    pip install .

If you prefer, you can use `pipenv` for installing latest vesion:

    pipenv shell

To install from PyPi (not necessarily latest version!):

    pip install pykins

#### Set up configuration

Create the file `/etc/pykins/pykins.yaml` with the following content:

```
jenkins:
   url: https://<jenkins_instance> 
   user: <jenkins_username>
   password: <jenkins_API_token>
```

### CLI Usage

#### Job Operations

* List jobs: `pykins job list`
* List jobs with substring 'neutron': `pykins job list neutron`
* Show job inforamtion(description, builds): `pykins job show <job_name>`

### API Usage

Work in progress

### How to contribute?
Using pull requests
