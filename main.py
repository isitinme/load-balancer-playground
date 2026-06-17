import os, logging
from fastapi import FastAPI
from fastapi.responses import JSONResponse
from dotenv import load_dotenv

# environment
load_dotenv()

# logging
log_level = os.environ.get('LOG_LEVEL', 'INFO').upper()
app_name = os.environ.get('APP_NAME', 'N/A')
logging.basicConfig(level=log_level)
logger = logging.getLogger(__name__)

# app
app = FastAPI()
headers = {"served_by": app_name}

# routes
@app.get("/")
async def root():
    logger.info('root(): /')
    content = {"message": "Hello from FastAPI!"}
    return JSONResponse(content=content, headers=headers)

@app.get("/api/health")
async def health():
    logger.info('health(): /api/health')
    content = {"status": "healthy"}
    return JSONResponse(content=content, headers=headers)

@app.get("/api/items/{item_id}")
async def read_item(item_id: int):
    logger.info('read_item(): /api/items/$id')
    content = {"item_id": item_id, "name": f"Item {item_id}"}
    return JSONResponse(content=content, headers=headers)