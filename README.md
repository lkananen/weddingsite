# weddingsite


## Setup

```
# Git commands
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