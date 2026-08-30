from fastapi import APIRouter
from app.services.health_service import model_health
router = APIRouter()

@router.get("/health")
def health_check():
    status = model_health()
    return status