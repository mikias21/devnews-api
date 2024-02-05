from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

# Local imports
from routers.index import router

origins = [
    'http://127.0.0.1:3000', 'http://localhost:3000', 'https://passitt.netlify.app'
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
    app.debug = True
    app.run()