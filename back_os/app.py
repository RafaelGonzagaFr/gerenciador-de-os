from fastapi import FastAPI

from back_os.routers import auth, users, os

app = FastAPI(
  title="OS Manager",
  docs_url="/docs",
  redoc_url=None,
  openapi_url="/openapi.json",
)

app.include_router(users.router)
app.include_router(auth.router)
app.include_router(os.router)
