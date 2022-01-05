# Wedding site

Docker containered FastAPI server running on Heroku.

Build status:   
[![CI](https://github.com/lkananen/weddingsite/actions/workflows/github-actions.yml/badge.svg)](https://github.com/lkananen/weddingsite/actions/workflows/github-actions.yml)


## Table of Contents
- [Wedding site](#wedding-site)
  - [Table of Contents](#table-of-contents)
  - [Directory structure](#directory-structure)
  - [Example website](#example-website)
  - [Architecture](#architecture)
  - [Setup](#setup)
    - [Local deployment](#local-deployment)
    - [First time deployment](#first-time-deployment)
    - [Automatic deployment](#automatic-deployment)
      - [Secrets](#secrets)
  - [Dependencies](#dependencies)
  - [Additional details](#additional-details)
    - [Always on application](#always-on-application)
    - [Heroku debug commands](#heroku-debug-commands)


## Directory structure

- `/.github/workflows` Deployment pipeline used by GitHub Actions.
- `/docs` Documentation files.
- `/source` Source files and environment configurations for the web server.
  - `/source/app` Web server application. FastAPI docs and URIs.
  - `/source/docker-compose.yml` Wer server Docker container compose definition.
  - `/source/Dockerfile` Web server Docker container definition.
  - `/source/entry.sh` Web server startup script run in the Docker container.
  - `/source/requirements.txt` Web server required packages.
- `Procfile` Heroku process type declaration for the web server startup.
- `heroku.yml` Heroku process type declaration for the web server startup.



## Example website
Direct link to the site:   
[link](https://laurijatiia.herokuapp.com/)


## Architecture
Deployment pipeline architecture:
![Deployment pipeline](/docs/FastAPI_Heroku.png)
Commits trigger GitHub actions to push changes to Heroku. Changes to Heroku trigger a Docker Compose build that creates a new version of the containerized FastAPI.


## Setup
Following instructions setup the demo and there are multiple ways to do it.
1. [Local deployment](#local-deployment): relies on [Python environment](source/requirements.txt) and a [Procfile](/Procfile), sets up everything from this repository as [a local web server](source/app/main.py).
2. [Manual Heroku deployment](#first-time-deployment): First time setup requires a Heroku application creation. The webserver stack can be defined in two ways: As a Python application through the [Procfile](/Procfile) or as an containerized application through [Docker Compose definition](source/docker-compose.yml). The compose application requires a stack configuration change [described below in the commands](#first-time-deployment).
3. [Automatic Heroku deployment](#automatic-deployment): Requires first manual setup first time and setting up the required [secrets](#secrets). Configures an automatic deployment pipeline that runs Git commits through GitHub repository's GitHub Actions. The pipeline workflow pushes the changes to Heroku application repository and initiates a reload of the web server application. The application is built using a [Docker Compose definition](source/docker-compose.yml) running a [FastAPI application in a](source/app/main.py) [Docker container](source/Dockerfile).


### Local deployment
Running following commands sets up local server.

```
git clone https://github.com/lkananen/weddingsite.git

pip install -r source/requirements.txt

#heroku login                       # Not completely neccessary
heroku local -f Procfile            # Starts the server
heroku open
```


### First time deployment
Heroku application creation is required on the first time.    

Following commands create _example-app-name_ Heroku application. After creation GitHub Actions can be attached to the application in the Heroku portal for [automated deployments](https://devcenter.heroku.com/articles/github-integration).

```
git clone https://github.com/lkananen/weddingsite.git

# Heroku setup
heroku login
heroku apps:create example-app-name --region eu

# Heroku build requirements
heroku buildpacks:set heroku/python --app example-app-name

# Heroku needs to know that app is in a Docker container
heroku stack:set container --app example-app-name

# Manual Heroku deployment
git push heroku main
heroku ps:scale web=1           # sets dynos
```


### Automatic deployment
Based on [GitHub Actions](./.github/workflows/github-actions.yml) and [Heroku deployment configuration](heroku.yml) files. Commit triggers dependency check and deployment to Heroku. See secrets on the required setup on Heroku secrets.   
Also optionally, Heroku can be configured to connect to GitHub to allow manual and automatic deployments based on the commits. Heroku deployment pipeline does not support build checks or other actions on the [free tier](https://www.heroku.com/pricing).


#### Secrets
[**Note!** *Required by GitHub Actions.*](#automatic-deployment)   

GitHub Action uses secrets to push changes to Heroku. Following secrets are required to be added to repository's secrets in the repository settings:
1. HEROKU_API_KEY
   - Can be found in:   
     `Heroku -> Profile -> Account settings -> API key`
2. HEROKU_APP_NAME
   - Name of the Heroku application.
   - Must be unique.
3. HEROKU_EMAIL
   - Email that you use with Heroku.


## Dependencies
Local install is based on the following installations:
- Heroku
  - `pip install heroku`
- FastAPI and Uvicorn server
  - `pip install "fastapi[all]"`
  - OR `pip install fastapi; pip install "uvicorn[standard]"`


## Additional details
Relevant details for further development, debugging and interaction with the application.


### Always on application
Heroku application goes to sleep after 30 minutes of inactivity. For example, Kaffeine application can be used to pings the app so that it stays active:  
http://kaffeine.herokuapp.com/

Deactivation link to Kaffeine:  
http://kaffeine.herokuapp.com/#decaf


### Heroku debug commands
Useful command for Heroku debugging:
```
heroku open                     # Open the default app in browser
heroku logs --tail              # Recent logs, Heroku stores 1500 lines
heroku run bash                 # Connect to dyno
heroku ps:exec                  # SSH to dyno
heroku ps                       # Info on dyno
```
