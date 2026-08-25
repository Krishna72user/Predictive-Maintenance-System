from passlib.context import CryptContext
import jwt
from app.core.config import settings
from datetime import datetime,timedelta,timezone

# Define the hashing context (uses argon2 by default, falls back to bcrypt if needed)
pwd_context = CryptContext(schemes=["argon2", "bcrypt"], deprecated="auto")


def hash_password(password: str) -> str:
    return pwd_context.hash(password)

def verify_password(plain_password: str, hashed_password: str) -> bool:
    return pwd_context.verify(plain_password, hashed_password)


def get_token(payload):
    payload['exp']= datetime.now(timezone.utc) + timedelta(hours=3)
    encoded = jwt.encode(payload, settings.secret, algorithm=settings.algorithm)
    return encoded


def decode_token(token):
    payload = jwt.decode(token, settings.secret, algorithms=[settings.algorithm])
    return payload


