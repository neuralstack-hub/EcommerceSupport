from datetime import datetime

from pydantic import BaseModel


class AttachmentCreate(BaseModel):
    ticket_id: str
    filename: str
    uploaded_by: str


class AttachmentResponse(BaseModel):
    id: str
    ticket_id: str
    filename: str
    uploaded_by: str
    uploaded_at: datetime
