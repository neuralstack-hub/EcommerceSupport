from datetime import datetime
from enum import Enum
from typing import Optional

from pydantic import BaseModel


class TicketStatus(str, Enum):
    NEW = "new"
    ASSIGNED = "assigned"
    IN_PROGRESS = "in_progress"
    ON_HOLD = "on_hold"
    RESOLVED = "resolved"
    CLOSED = "closed"


class Ticket(BaseModel):
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
