# weddingsite


## Setup

Local setup

```
git clone https://github.com/lkananen/weddingsite.git

pip install -r requirements.txt

heroku login
heroku local -f Procfile web
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
heroku open
heroku logs --tail
```
