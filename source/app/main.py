from fastapi import FastAPI, status

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
    return {"message": "Hello!"}


@app.get("/health", status_code=status.HTTP_200_OK, tags=["health"])
async def health_check():
    return {"healtcheck": "ok"}
