import imp
from fastapi import FastAPI, status, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
#from fastapi.staticfiles import StaticFiles
import os
import io
import ast
#import PIL
#from PIL import Image
import qrcode
from starlette.responses import StreamingResponse

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

# TODO: Add SSL
# Removed as Heroku tries to obtain CSS via HTTP resulting in insecure connection 
# # static
# app.mount(
#     "/static",
#     StaticFiles(directory="app/static"),
#     name="static"
# )

# templates
templates = Jinja2Templates(directory="app/templates")


# Main page
@app.get("/", tags=["root"])
async def root():
    return {
        "message": "Hello!",
        "link": "https://www.youtube.com/watch?v=eu2OYcgr4rM"
    }


@app.get("/health", status_code=status.HTTP_200_OK, tags=["health"])
async def health_check():
    return {"healtcheck": "ok"}


# Fetches seat map JSON from configuration files loaded to the environment
@app.get("/seats", status_code=status.HTTP_200_OK, tags=["seat", "json", "seatmap"])
async def get_seats():
    return {
        "data": ast.literal_eval(
            os.environ.get("SEATS", [])
        )
    }


# Visualizes the seats
@app.get("/seatmap", response_class=HTMLResponse, tags=["map", "seatmap"])
async def read_seatmap(request: Request):
    full_data = ast.literal_eval(
        os.environ.get("SEATS", [])
    )
    
    # Unique values
    ids = {i["id"] for i in full_data}
    tables = {i["table"] for i in full_data}
    sides = {i["side"] for i in full_data}
    places = {i["place"] for i in full_data}
    places_minus_one = {i for i in range(len(places) - 1)}

    # TODO: after including static files replace styles with this
    # <link href="{{ url_for('static', path='/styles.css') }}" rel="stylesheet">

    return templates.TemplateResponse("seatmap.html", {
        "request": request,
        "data": ast.literal_eval(
            os.environ.get("SEATS", [])
        ),
        "ids": list(ids),
        "tables": list(tables),
        "sides": list(sides),
        "places": list(places),
        "places_minus_one": list(places_minus_one)
    })


# qr code generation
@app.get("/qr")
def generate_qr():
    msg = os.environ.get("QR_MSG", "")
    img = qrcode.make(msg)
    buf = io.BytesIO()
    img.save(buf)
    buf.seek(0)     # important here!
    return StreamingResponse(buf, media_type="image/jpeg")
