**THIS IS A CLONE OF A PRIVATE REPOSITORY. A CLONE IS MADE SO THAT IT CAN BE CLONES IN GOOGLE CLOUD SERVICES WITHOUT PROBLEMS.**

# Questboard

This web application is an implementation of the Questboard using Django and SQLite that is a modified version of the final requirement for CSCI 40: Software Tools and Development Frameworks. Lifted from the project specifications, the Questboard can be described as follows:

*The Questboard is a gamified project selection mechanism implemented by Neithan Casano in his classes. The idea is simple: the teacher creates quests (i.e. project options) that students can choose from. The students can call dibs on the quest/s that they would like to take on.*

This application can be tested on Google Cloud using a Google Cloud Account for containerization and deployment. Further details in the Prerequisites and Deployment (on CloudRun).

## Getting Started

These instructions will get you a copy of the project up and running on your local **Windows** machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

**Important Note**: Instructions are currently specific to Windows machines.

### Prerequisites

#### For Testing on Host Machine

* Install Python from the respective site -
  * Python: https://www.python.org/downloads/
  * After installation, add Python to the PATH variable.
  * Adding Python to PATH: https://www.educative.io/answers/how-to-add-python-to-path-variable-in-windows
  * In case the Python tool ```virtualenv``` is not included by default, install it by typing ```pip install virtualenv``` on a local terminal.

#### For Cloud Deployment

* Google Cloud Account - [Create a Google Cloud Account and Connect to a Billing Service](https://cloud.google.com/free?utm_source=bing&utm_medium=cpc&utm_campaign=japac-PH-all-en-dr-bkws-all-all-trial-e-dr-1009882&utm_content=text-ad-none-none-DEV_c-CRE_-ADGP_Hybrid%20%7C%20BKWS%20-%20EXA%20%7C%20Txt%20~%20GCP%20~%20General_%20Core%20Brand-KWID_43700071941772138-kwd-74354743788022%3Aloc-149-userloc_145635&utm_term=KW_google%20cloud-ST_google%20cloud&gclid=5a620601f22613efedad65f95fbaf308&gclsrc=3p.ds&) 

* Google Cloud Project - On your Google Cloud Account create a project for setting up Docker (Deployment further elaborated in the "Deploying on CloudRun" section of the README). 

### Setting Up Virtual Environment

1. Open a terminal in a local directory and clone the project with ```git clone https://github.com/CaelebC/qb_cloudrun_iscs```.
2. Change to the project folder with ```cd qb_cloudrun_iscs```.
3. Create a virtual environment with ```virtualenv questboardenv```.
4. Activate the created virtual environment with ```questboardenv\Scripts\activate```.
5. Change to the application folder with ```cd questboardsite```.
5. Install necessary dependencies using ```pip install -r requirements.txt```.

## Running on Local Machine
1. Run the following commands to create models in the database.
```
python manage.py makemigrations
python manage.py migrate
```
2. Run the server on localhost with ```python manage.py runserver```.
3. Open ```localhost:8000``` on local web browser to access web application.

## Deploying on CloudRun

Deploying this web application will require a Google Cloud account, and a Google Cloud project. Once that prerequisite has been completed, the following steps can be done to deploy this application on CloudRun.

1. Open the Cloud Shell on Google Cloud homepage.
2. Enable the Cloud Run API, and set the compute region with 
```
gcloud services enable run.googleapis.com
gcloud config set compute/region us-central1
```
3. Create an environment variable for LOCATION and port using the commands. 
```
export LOCATION="us-central1"
export PORT=8080
```
To check if the environment variables work, use `echo $LOCATION` and `echo $PORT`.

4. Change directory to the project folder using `cd qb_cloudrun_iscs/questboardsite`.
5. Build the container image using `gcloud builds submit --tag gcr.io/$GOOGLE_CLOUD_PROJECT/qb_cloudrun_iscs/questboardsite`. A success message should appear that contains the image name *gcr.io/[PROJECT-ID]/helloworld*. To test the project, use the command `curl localhost:8080`
6. Deploy the containerized application to CloudRun using the command `gcloud run deploy --image gcr.io/$GOOGLE_CLOUD_PROJECT/helloworld --allow-unauthenticated --region=$LOCATION`. A prompt will appear to set a service name, press **Enter** when this happens.
7. Once the deployment is completed, a URL should appear in the commandline which could be used to access the web application.

## Built With

* [Django](https://www.djangoproject.com/) - Python web framework used
* [SQLite](https://www.sqlite.org/index.html) - Database engine used

## Versioning

[Copied from template] We use [SemVer](http://semver.org/) for versioning. For the versions available, see the [tags on this repository](https://github.com/your/project/tags). 

