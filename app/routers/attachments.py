from datetime import datetime
from uuid import uuid4

from fastapi import APIRouter, Depends, status
from pymongo.collection import Collection

from app.dependencies import get_attachments_collection
from app.schemas.attachment import AttachmentCreate, AttachmentResponse

router = APIRouter(prefix="/attachments", tags=["Attachments"])


@router.get("", response_model=list[AttachmentResponse])
def list_attachments(
    attachments_collection: Collection = Depends(get_attachments_collection),
    ticket_id: str | None = None,
):
    """Return all attachments, optionally filtered by ticket (?ticket_id=...)."""
    query = {}
    if ticket_id:
        query["ticket_id"] = ticket_id
    return list(attachments_collection.find(query))


@router.post("", response_model=AttachmentResponse, status_code=status.HTTP_201_CREATED)
def create_attachment(payload: AttachmentCreate, attachments_collection: Collection = Depends(get_attachments_collection)):
    """Record a new attachment on a ticket."""
    attachment_doc = {
        "id": str(uuid4()),
        "ticket_id": payload.ticket_id,
        "filename": payload.filename,
        "uploaded_by": payload.uploaded_by,
        "uploaded_at": datetime.utcnow(),
    }
    attachments_collection.insert_one(attachment_doc)
    return attachment_doc
