from fastapi import APIRouter
from app.api.v1.endpoints import health,inference,auth

router = APIRouter()

router.include_router(health.router, tags=["Health"])
router.include_router(inference.router, tags=["Inference"])
router.include_router(auth.router, tags=["Authentication"])