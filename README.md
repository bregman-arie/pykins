## Pykins

Yet another CLI for Jenkins.
Pykins provides you with:

  * The ability to analyze builds

### Installation

A virtual environment is recommended for development.
To install the latest version of `pykins`, run the following commands:

    virtualenv .venv && source .venv/bin/activate
    pip install .

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

### CLI

* Analyze build

```
pykins build analyze https://<jenkins_server>/job/<job_name>/<build_number>
OR
pykins build analyze --build <build_number> --job <job_name>
```

### How to contribute?
Using pull requests
