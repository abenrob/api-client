API-CLIENT
=======

A Flask App for exploring the APIs.

Requires Python 2.7, Flask, Requests, virtual environment

Installation
--------------
Install relies on pip and virtualenv

1. ```easy_install pip``` (if not installed)
2. ```pip install virtualenv```
3. ```cd <location of local API-CLIENT github repo>```
4. ```virtualenv venv```
5. activate the virtual environment: ```source venv/bin/activate``` (osx/*nix) -OR- ```venv\scripts\activate``` (windows)
6. ```pip install -r requirements.txt``` (this installs all the dependencies)
7. ```deactivate```


Basic Instructions
----------------------
1. Open a command line with administrative permissions and enter the following commands:

```cd <location of local API-CLIENT github repo>```

```source venv/bin/activate``` (osx/*nix) -OR- ```venv\scripts\activate``` (windows)

```gunicorn run-api:app``` (gunicorn used in lieu of dev server for multi-thread capability)

2. Open browser http://localhost:8000/get_dat_json
3. Enter URI: ```http://my.api.v01/resource```
4. Enter Params: ```{"ids":"771,496"}```
5. Play with your data
6. ```deactivate``` (when finished)
