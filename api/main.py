from fastapi import FastAPI
from api.routes import router

app = FastAPI(title="Netmapper-Z API", version="1.0.0", description="Enterprise Reconnaissance REST Interface")

app.include_router(router, prefix="/api/v1")

@app.get("/")
def health_check():
    return {"status": "online", "framework": "Netmapper-Z"}
