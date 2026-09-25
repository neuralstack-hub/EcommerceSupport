from datetime import datetime
from typing import Optional

from pydantic import BaseModel

from app.models.ticket import TicketStatus
from app.schemas.user import UserResponse


class TicketCreate(BaseModel):
    title: str
    description: str
    category_id: str
    order_id: Optional[str] = None
    created_by: str


class TicketUpdate(BaseModel):
    status: Optional[TicketStatus] = None
    assigned_to: Optional[str] = None


class TicketResponse(BaseModel):
    id: str
    title: str
    description: str
    category_id: str
    order_id: Optional[str] = None
    status: TicketStatus
    created_by: str
    assigned_to: Optional[str] = None
    created_at: datetime
    updated_at: datetime


class TicketDetailResponse(TicketResponse):
    """Ticket response including the customer and assigned support agent."""

    customer: UserResponse
    assigned_agent: Optional[UserResponse] = None
