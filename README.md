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

## Dependencies

- Heroku
  - `pip install heroku`
- FastAPI and Uvicorn server
  - `pip install "fastapi[all]"`
  - OR `pip install fastapi; pip install "uvicorn[standard]"`