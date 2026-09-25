from datetime import datetime

from pydantic import BaseModel


class Category(BaseModel):
    id: str
    name: str
    description: str
    created_at: datetime
