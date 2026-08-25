from app.schemas.user import UserCreate,LoginUser
from app.core.security import hash_password,verify_password,get_token,decode_token
from app.models.user import User
from fastapi import HTTPException


def create_user(user_data:UserCreate,db):
    existing_user = (
        db.query(User)
        .filter(User.email == user_data.email)
        .first()
    )
    if existing_user:
        raise HTTPException(
            status_code=400,
            detail="Username already exists"
        )
    hash_pass  = hash_password(user_data.password)
    user = User(username=user_data.username,
                password=hash_pass,
                email=user_data.email   )
    db.add(user)
    db.commit()
    db.refresh(user)
    token = get_token({'id':user.id,'email':user.email})
    return token



def login_user(user_data:LoginUser,db):
    existing_user = (
        db.query(User)
        .filter(User.email == user_data.email)
        .first()
    )
    if not existing_user:
        raise HTTPException(
            status_code=401,
            detail="Invalid Credentials"
        )
    status  = verify_password(user_data.password,existing_user.password)
    if not status:
        raise HTTPException(
            status_code=401,
            detail="Invalid Credentials"
        )
    token = get_token({'id':existing_user.id,'email':existing_user.email})

    return token


def get_user(token):
    payload = decode_token(token)
    return payload