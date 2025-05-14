app = FastAPI (
  title = "OS Manager",
  docs_url="/docs",
  redoc_url=None,
  openapi_url="/openapi.json",
)

app.include_router(users.router)