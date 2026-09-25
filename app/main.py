from fastapi import FastAPI

from app.config import settings
from app.database import client
from app.routers import attachments, categories, comments, tickets, users

app = FastAPI(title=settings.APP_NAME)

app.include_router(users.router)
app.include_router(categories.router)
app.include_router(tickets.router)
app.include_router(comments.router)
app.include_router(attachments.router)


@app.on_event("startup")
def on_startup():
    # Simple check that MongoDB is reachable at startup
    client.admin.command("ping")
    print(f"[startup] Connected to MongoDB. App: {settings.APP_NAME}")


@app.get("/")
def root():
    return {"message": f"{settings.APP_NAME} is running"}


@app.get("/health")
def health():
    return {"status": "ok"}
