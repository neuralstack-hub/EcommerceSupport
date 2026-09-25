from datetime import datetime
from typing import Optional
from uuid import uuid4

from fastapi import APIRouter, Depends, HTTPException, status
from pymongo.collection import Collection

from app.dependencies import get_tickets_collection, get_users_collection
from app.schemas.ticket import TicketCreate, TicketDetailResponse, TicketResponse, TicketUpdate

router = APIRouter(prefix="/tickets", tags=["Tickets"])


@router.get("", response_model=list[TicketResponse])
def list_tickets(
    tickets_collection: Collection = Depends(get_tickets_collection),
    status_filter: Optional[str] = None,
):
    """Return all tickets, optionally filtered by status (?status_filter=new)."""
    query = {}
    if status_filter:
        query["status"] = status_filter
    return list(tickets_collection.find(query))


@router.post("", response_model=TicketResponse, status_code=status.HTTP_201_CREATED)
def create_ticket(
    payload: TicketCreate,
    tickets_collection: Collection = Depends(get_tickets_collection),
):
    """Create a new support ticket."""
    now = datetime.utcnow()
    ticket_doc = {
        "id": str(uuid4()),
        "title": payload.title,
        "description": payload.description,
        "category_id": payload.category_id,
        "order_id": payload.order_id,
        "status": "new",
        "created_by": payload.created_by,
        "assigned_to": None,
        "created_at": now,
        "updated_at": now,
    }
    tickets_collection.insert_one(ticket_doc)
    return ticket_doc


@router.get("/{ticket_id}", response_model=TicketDetailResponse)
def get_ticket(
    ticket_id: str,
    tickets_collection: Collection = Depends(get_tickets_collection),
    users_collection: Collection = Depends(get_users_collection),
):
    """Return one ticket together with the customer and assigned support agent."""
    ticket_doc = tickets_collection.find_one({"id": ticket_id})
    if not ticket_doc:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Ticket not found")

    customer = users_collection.find_one({"id": ticket_doc["created_by"]})
    if not customer:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Ticket customer not found")

    assigned_agent = None
    if ticket_doc.get("assigned_to"):
        assigned_agent = users_collection.find_one({"id": ticket_doc["assigned_to"]})

    return {
        **ticket_doc,
        "customer": customer,
        "assigned_agent": assigned_agent,
    }


@router.patch("/{ticket_id}", response_model=TicketResponse)
def update_ticket(
    ticket_id: str,
    payload: TicketUpdate,
    tickets_collection: Collection = Depends(get_tickets_collection),
):
    """Update a ticket's status and/or assigned support agent."""
    ticket_doc = tickets_collection.find_one({"id": ticket_id})
    if not ticket_doc:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Ticket not found")

    updates = {k: v for k, v in payload.model_dump(exclude_unset=True).items()}
    updates["updated_at"] = datetime.utcnow()

    tickets_collection.update_one({"id": ticket_id}, {"$set": updates})
    return tickets_collection.find_one({"id": ticket_id})
