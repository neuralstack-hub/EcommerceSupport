from datetime import datetime
from uuid import uuid4

from fastapi import APIRouter, Depends, HTTPException, status
from pymongo.collection import Collection

from app.dependencies import get_users_collection
from app.schemas.user import UserCreate, UserResponse

router = APIRouter(prefix="/users", tags=["Users"])


@router.get("", response_model=list[UserResponse])
def list_users(users_collection: Collection = Depends(get_users_collection)):
    """Return all users."""
    return list(users_collection.find())


@router.get("/{user_id}", response_model=UserResponse)
def get_user(user_id: str, users_collection: Collection = Depends(get_users_collection)):
    """Return one user by id."""
    user_doc = users_collection.find_one({"id": user_id})
    if not user_doc:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
    return user_doc


@router.post("", response_model=UserResponse, status_code=status.HTTP_201_CREATED)
def create_user(payload: UserCreate, users_collection: Collection = Depends(get_users_collection)):
    """Create a new user."""
    user_doc = {
        "id": str(uuid4()),
        "name": payload.name,
        "email": payload.email,
        "role": payload.role,
        "created_at": datetime.utcnow(),
    }
    users_collection.insert_one(user_doc)
    return user_doc
