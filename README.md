[![Open in Codespaces](https://classroom.github.com/assets/launch-codespace-f4981d0f882b2a3f0472912d15f9806d57e124e0fc890972558857b51b24a6f9.svg)](https://classroom.github.com/open-in-codespaces?assignment_repo_id=10236209)
# Questboard

This web application is an implementation of the Questboard using Django and PostgreSQL that served as the final requirement for CSCI 40: Software Tools and Development Frameworks. Lifted from the project specifications, the Questboard can be described as follows:

*The Questboard is a gamified project selection mechanism implemented by Neithan Casano in his classes. The idea is simple: the teacher creates quests (i.e. project options) that students can choose from. The students can call dibs on the quest/s that they would like to take on.*

## Getting Started

These instructions will get you a copy of the project up and running on your local **Windows** machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

**Important Note**: Instructions are currently specific to Windows machines.

### Prerequisites

* Install Python from the respective site.
  * Python: https://www.python.org/downloads/
* After installation, add Python to the PATH variable.
  * Adding Python to PATH: https://www.educative.io/answers/how-to-add-python-to-path-variable-in-windows
* In case the Python tool ```virtualenv``` is not included by default, install it by typing ```pip install virtualenv``` on a local terminal.

### Setting Up Virtual Environment

1. Open a terminal in a local directory and clone the project with ```git clone https://github.com/admu-zaavedra/containerize-your-application-project-group-2-abangan-camaro-serrano.git```.
2. Change to the project folder with ```cd containerize-your-application-project-group-2-abangan-camaro-serrano```.
3. Create a virtual environment with ```virtualenv questboardenv```.
4. Activate the created virtual environment with ```questboardenv\Scripts\activate```.
5. Install necessary dependencies using ```pip install -r requirements.txt```.

## Running on Local Machine
1. Change to the application folder with ```cd questboardsite```.
2. Run the following commands to create models in the database.
```
python manage.py makemigrations
python manage.py migrate
```
3. Run the server on localhost with ```python manage.py runserver```.
4. Open ```localhost:8000``` on local web browser to access web application.

## Deployment

[To be added]

## Built With

* [Django](https://www.djangoproject.com/) - Python web framework used
* [PostgreSQL](https://www.postgresql.org/) - Relational database system used

## Versioning

[Copied from template] We use [SemVer](http://semver.org/) for versioning. For the versions available, see the [tags on this repository](https://github.com/your/project/tags). 

