from fastapi import APIRouter,Cookie, Response,Depends
from typing import Annotated
from app.schemas.user import UserCreate,LoginUser
from app.services.user_service import login_user,create_user,get_user
from app.db.session import get_db

router = APIRouter(prefix='/auth')

@router.post('/register')
def register(user:UserCreate,response:Response,db = Depends(get_db)):
    token = create_user(user,db)
    response.set_cookie(
        key="session_token",
        value=token,
        httponly=True,     # Prevents JavaScript XSS access
        secure=True,       # Transmit over HTTPS only
        samesite="lax",    # CSRF protection ("lax", "strict", or "none")
        max_age=3600      
    )
    return {"message": "User created successfully"}

@router.post('/login')
def login(user:LoginUser,response:Response,db = Depends(get_db)):
    token = login_user(user,db)
    response.set_cookie(
            key="session_token",
            value=token,
            httponly=True,     # Prevents JavaScript XSS access
            secure=True,       # Transmit over HTTPS only
            samesite="lax",    # CSRF protection ("lax", "strict", or "none")
            max_age=3600      
        )
    return {"message": "User logged in successfully"}

@router.post('/logout')
def logout(response:Response):
    response.delete_cookie(key="session_token")
    return {"message": "Successfully logged out"}

@router.post('/get_user')
def get_user_profile(session_token: Annotated[str | None, Cookie()] = None):
    if not session_token:
        return {"error": "Unauthorized: No session cookie provided"}
    payload = get_user(session_token)
    return {'payload':payload}