from fastapi import FastAPI
from api.routes import router
from logs import logger
logger.info("Starting the application")
app = FastAPI()
app.include_router(router)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)