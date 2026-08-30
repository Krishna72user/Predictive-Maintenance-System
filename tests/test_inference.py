from app.services.model_service import load_model
import pandas as pd


def test_prediction():
    model= load_model()

    demo_input =pd.DataFrame([['L',300.5,309.8,1345,62.7,153,9.3011]],
            columns=['Type','Air temperature [K]',
            'Process temperature [K]',
            'Rotational speed [rpm]',
            'Torque [Nm]',
            'Tool wear [min]',
            'Temperature Difference'])
    pred= model.predict(demo_input)
    assert pred.shape == (1,)
    assert pred[0]  in [0,1]

        