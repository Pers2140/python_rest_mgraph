
# Python MSgraph

This python module uses Microsoft graph API REST capabilities to create, upload and modify 
files in a chosen Sharepoint site

### Useful Resources

- https://learn.microsoft.com/en-us/graph/use-the-api
## [How Python Virtual Enviroment Works](https://docs.python.org/3/library/venv.html)

```mermaid
graph TD
  A[Operating System] --> B{Python Interpreter}
  B --> C[Global Site Packages]
  B --> D[Local Virtual Environment]
  D --> E[Local Site Packages]
  D --> F[Scripts]
  G[Project Folder] --> D
  H[Dependencies] --> E

  ```

## PIP Packages

- See [requirements.txt](requirements.txt) </br>
- This package uses python-dotenv see: [Git-hub python-dotenv](https://github.com/theskumar/python-dotenv)


## Why should you use Python virtual environments

A virtual environment (venv) is a tool that helps you isolate Python projects from each other. This is useful because it prevents different projects from interfering with each other's dependencies.

Virtualenv is a tool to set up your Python environments. Since Python 3.3, a subset of it has been integrated into the standard library under the venv module. You can install venv to your host Python by running this command in your terminal:

create your own .env file in the root of your project folder - see [Example](Example_ENV.txt)

```

  pip install virtualenv

```
## Basic setup 

### 1. Create a new python virtual environment

- Linux/Windows:
```
    python3 -m venv {your_env_name}
```

### 2. Activate environment

- Linux:

```
source {your_env_name}/bin/activate
({your_env_name}) $
```
- Windows:

```

PS> {your_env_name}\Scripts\activate
({your_env_name}) PS>

```

### 3. Installing required packages from requirements.txt

- Linux / Windows:

```

({your_env_name}) $ pip install -r path/to/requirements.txt

```

# Other useful commands

### Installing individual packages into env

- Linux / Windows:

```

({your_env_name}) $ python -m pip install <package-name>

```
### Exporting list of all install packages 

```
  pip freeze > requirements.txt
```
### Listing installed packages

```
  pip list
```
## TODO 
