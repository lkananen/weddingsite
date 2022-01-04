from fastapi import FastAPI, status

app = FastAPI()
# Note! Automatically defines paths /docs and /redoc

@app.get("/")
async def root():
    return {"message": "Hello!"}


@app.get("/health", status_code=status.HTTP_200_OK)
async def health_check():
    return {"healtcheck": "ok"}
