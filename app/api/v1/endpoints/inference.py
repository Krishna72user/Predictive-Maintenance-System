from fastapi import APIRouter,Depends,Cookie,HTTPException
from app.schemas.inference import InferenceModel
from app.services.model_service import load_model
from app.services.inference_service import inference
from typing import Annotated
from app.services.user_service import get_user
from app.db.session import get_db


router = APIRouter()

@router.post("/predict")
def predict(query:InferenceModel,session_token: Annotated[str | None, Cookie()] = None,model=Depends(load_model),db=Depends(get_db)):
    if not session_token:
        raise HTTPException(
            status_code=401,
            detail='Unauthorized Access'
        )
    payload = get_user(session_token)
    if payload:
        output = inference(query,model,payload,db)
        return output
    else :
        raise HTTPException(
            status_code=401,
            detail='Unauthorized Access'
        )
    