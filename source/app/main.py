import imp
from fastapi import FastAPI, status
import json
import os

# Loads configuration variables
# They can be set using following commands:
#heroku config:set IS_HEROKU=True 
# And loaded like this:
#is_prod = os.environ.get('IS_HEROKU', None)

description = """
## Description
TODO (_not implemented_)

### Automatically generated paths
- **/docs**: This documentation file.
- **/redoc**: Alternative documentations.
- **/openapi.json**: OpenAPI schema.
"""

tags_metadata = [
    {
        "name": "root",
        "description": "Main site"
    },
    {
        "name": "health",
        "description": "Web server health status."
    }
]

app = FastAPI(
    title="Documentation of the site",
    version="0.1.0",
    description=description,
    openapi_tags=tags_metadata,
    docs_url="/docs",
    redoc_url="/redoc",
    openapi_url="/openapi.json"
)


@app.get("/", tags=["root"])
async def root():
    return {
        "message": "Hello!",
        "link": "https://www.youtube.com/watch?v=eu2OYcgr4rM"
    }


@app.get("/health", status_code=status.HTTP_200_OK, tags=["health"])
async def health_check():
    return {"healtcheck": "ok"}


# Fetches seat map from configuration files loaded to the environment
@app.get("/seats", status_code=status.HTTP_200_OK, tags=["seatmap"])
async def get_seats():
    return {
        "data": json.load(
            os.environ.get("SEATS", [])
        )
    }