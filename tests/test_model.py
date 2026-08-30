from app.services.model_service import load_model

def test_model_loader():
    model= load_model()
    assert model is not None
    assert hasattr(model,'predict')
    assert hasattr(model,'predict_proba')