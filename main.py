from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from routers import router

app = FastAPI()

app.add_middleware(CORSMiddleware,
                   allow_origins=["*"],
                   allow_credentials=True,
                   allow_methods=["*"],
                   allow_headers=["*"])
app.include_router(router=router)

app.mount(path=f"/", app=StaticFiles(directory="./views", html=True))
