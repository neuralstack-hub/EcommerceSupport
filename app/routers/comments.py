from datetime import datetime
from uuid import uuid4

from fastapi import APIRouter, Depends, status
from pymongo.collection import Collection

from app.dependencies import get_comments_collection
from app.schemas.comment import CommentCreate, CommentResponse

router = APIRouter(prefix="/comments", tags=["Comments"])


@router.get("", response_model=list[CommentResponse])
def list_comments(
    comments_collection: Collection = Depends(get_comments_collection),
    ticket_id: str | None = None,
):
    """Return all comments, optionally filtered by ticket (?ticket_id=...)."""
    query = {}
    if ticket_id:
        query["ticket_id"] = ticket_id
    return list(comments_collection.find(query))


@router.post("", response_model=CommentResponse, status_code=status.HTTP_201_CREATED)
def create_comment(payload: CommentCreate, comments_collection: Collection = Depends(get_comments_collection)):
    """Add a comment to a ticket."""
    comment_doc = {
        "id": str(uuid4()),
        "ticket_id": payload.ticket_id,
        "author_id": payload.author_id,
        "message": payload.message,
        "created_at": datetime.utcnow(),
    }
    comments_collection.insert_one(comment_doc)
    return comment_doc
