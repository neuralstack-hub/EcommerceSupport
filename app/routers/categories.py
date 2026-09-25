from datetime import datetime
from uuid import uuid4

from fastapi import APIRouter, Depends, HTTPException, status
from pymongo.collection import Collection

from app.dependencies import get_categories_collection
from app.schemas.category import CategoryCreate, CategoryResponse

router = APIRouter(prefix="/categories", tags=["Categories"])


@router.get("", response_model=list[CategoryResponse])
def list_categories(categories_collection: Collection = Depends(get_categories_collection)):
    """Return all categories."""
    return list(categories_collection.find())


@router.get("/{category_id}", response_model=CategoryResponse)
def get_category(category_id: str, categories_collection: Collection = Depends(get_categories_collection)):
    """Return one category by id."""
    category_doc = categories_collection.find_one({"id": category_id})
    if not category_doc:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Category not found")
    return category_doc


@router.post("", response_model=CategoryResponse, status_code=status.HTTP_201_CREATED)
def create_category(payload: CategoryCreate, categories_collection: Collection = Depends(get_categories_collection)):
    """Create a new category."""
    category_doc = {
        "id": str(uuid4()),
        "name": payload.name,
        "description": payload.description,
        "created_at": datetime.utcnow(),
    }
    categories_collection.insert_one(category_doc)
    return category_doc
