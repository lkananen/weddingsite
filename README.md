# weddingsite


## Setup

Local setup

```
git clone https://github.com/lkananen/weddingsite.git

pip install -r requirements.txt

heroku login
heroku local -f Procfile            # Starts the server
heroku open
```

Manual deployment

```
git clone https://github.com/lkananen/weddingsite.git

# Heroku setup
heroku login
heroku apps:create example-app --region eu

# Heroku requirements
heroku buildpacks:set heroku/python

# Manual Heroku deployment
git push heroku main
heroku ps:scale web=1

# Heroku debug commands
heroku open                     # Open the default app in browser
heroku logs --tail              # Recent logs, Heroku stores 1500 lines
heroku run bash                 # Connect to dyno
```

Secrets

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

- Heroku
  - `pip install heroku`
- FastAPI and Uvicorn server
  - `pip install "fastapi[all]"`
  - OR `pip install fastapi; pip install "uvicorn[standard]"`