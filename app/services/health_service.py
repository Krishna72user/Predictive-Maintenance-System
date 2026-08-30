from app.services.model_service import load_model

def model_health():
    model = load_model()
    if model is None:
        return {
            "status": "unhealthy",
            "model": "not loaded",
            "api": "up",
        }

    return {
        "status": "healthy",
        "model": "loaded",
        "api": "down",
    }

