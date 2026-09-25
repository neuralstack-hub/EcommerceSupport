from datetime import datetime
from enum import Enum

from pydantic import BaseModel, EmailStr


class UserRole(str, Enum):
    CUSTOMER = "customer"
    SUPPORT_AGENT = "support_agent"
    ADMIN = "admin"


class User(BaseModel):
    id: str
    name: str
    email: EmailStr
    role: UserRole
    created_at: datetime
