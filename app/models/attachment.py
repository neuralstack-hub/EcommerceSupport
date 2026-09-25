from datetime import datetime

from pydantic import BaseModel


class Attachment(BaseModel):
    id: str
    ticket_id: str
    filename: str
    uploaded_by: str
    uploaded_at: datetime
