import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

# Local imports
from routers.index import router
from utils.constants import General

origins = [
    '*',
]


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["POST", "GET", "PUT", "DELETE", "OPTIONS"],
    allow_headers=["*"],
    max_age=3600,
)

app.include_router(router)

if __name__ == "__main__":
    if General.PRODUCTION.value == True:
        uvicorn.run(app, host="0.0.0.0", port=8000)
    else:
        app.debug = True
        uvicorn.run(app, host="127.0.0.1", port=8000)