from datetime import datetime

from pydantic import BaseModel


class CommentCreate(BaseModel):
    ticket_id: str
    author_id: str
    message: str


class CommentResponse(BaseModel):
    id: str
    ticket_id: str
    author_id: str
    message: str
    created_at: datetime
