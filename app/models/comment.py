from datetime import datetime

from pydantic import BaseModel


class Comment(BaseModel):
    id: str
    ticket_id: str
    author_id: str
    message: str
    created_at: datetime
