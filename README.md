# python-template
A starting template for a Python project

# Setting up a developer environment

Recommended reading: [Python tooling](https://medium.com/georgian-impact-blog/python-tooling-makes-a-project-tick-181d567eea44)

## Install [pyenv](https://github.com/pyenv/pyenv)
Pyenv is used to install and manage different Python-versions. With the additional plugin pyenv-virtualenv, it also manages virtual environments.

- Make sure to also install the addons
  * [pyenv-virtualenv](https://github.com/pyenv/pyenv-virtualenv)
  * [pyenv-which-ext](https://github.com/pyenv/pyenv-which-ext)
- Install a couple of the latest Python versions, and possibly also `miniconda-latest`

### Create a virtual environment and activate it for this directory
```
pyenv install 3.5.7
pyenv install 3.6.9
pyenv install 3.7.4
pyenv virtualenv 3.7.4 myproject
```

Set the virtual environment as default, make a couple of older Python-versions available.
```
pyenv local myproject 3.6.9 3.5.7
```

## Install [poetry](https://github.com/sdispater/poetry)
Using Poetry replaces setup.py, setpu.cfg, requirements.txt, MANIFEST.IN, etc.

### Install this project into the virtual environment
```
poetry install
```

