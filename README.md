# FastAPI demo

Docker containered FastAPI server running on Heroku.

Build status:   
[![CI](https://github.com/lkananen/fastapi_demosite/actions/workflows/github-actions.yml/badge.svg)](https://github.com/lkananen/fastapi_demosite/actions/workflows/github-actions.yml)

Direct link to the site:   
[link](https://laurijatiia.herokuapp.com/)


## Setup

### Local deployment
Running following commands sets up local server.

```
git clone https://github.com/lkananen/fastapi_demosite.git

pip install -r source/requirements.txt

#heroku login                       # Not completely neccessary
heroku local -f Procfile            # Starts the server
heroku open
```

### First time deployment
Heroku application creation is required on the first time.    

Following commands create _example-app-name_ Heroku application. After creation GitHub Actions can be attached to the application in the Heroku portal for [automated deployments](https://devcenter.heroku.com/articles/github-integration).

```
git clone https://github.com/lkananen/fastapi_demosite.git

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

![Deployment pipeline](/source/docs/FastAPI_Heroku.png)
Deployment pipeline architecture.

### Secrets

**Note!** *Required by GitHub Actions.*   

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