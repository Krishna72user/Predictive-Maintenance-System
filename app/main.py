from fastapi import FastAPI,Request,Depends
from fastapi.responses import JSONResponse
from app.api.v1.router import router
from fastapi.middleware.cors import CORSMiddleware
from app.db.session import Base,engine


app = FastAPI()

Base.metadata.create_all(bind=engine) # Creates the database tables


app.add_middleware(
    CORSMiddleware,
    # allow_origins=["https://notegen-nine.vercel.app"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.exception_handler(Exception) # Universal Error handler
async def universal_exception_handler(
    request: Request,
    exc: Exception
):
    return JSONResponse(
        status_code=500,
        content={
            "success": False,
            "message": "Internal Server Error",
            "error": str(exc)
        }
    )

@app.get("/")
async def root():
    return {"status": "ok"}

app.include_router(router,prefix='/api/v1')

