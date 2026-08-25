from app.services.model_service import prediction
from app.schemas.inference import InferenceModel
from fastapi import HTTPException
from app.models.pred import Prediction


def inference(query:InferenceModel,model,payload,db):
    try:   
        probs = prediction(query,model).flatten()
        pred =int(probs[1]>=.53)
        print(payload)
        db_prediction = Prediction(
            user_id=payload['id'],
            type=query.type,
            air_temperature=query.air_temp,
            process_temperature=query.process_temp,
            rotational_speed=query.rot_speed,
            torque=query.torque,
            tool_wear=query.tool_wear,
            prediction=pred
        )
        db.add(db_prediction)
        db.commit()
        db.refresh(db_prediction)
        
        if pred:
            output = {
            "status": "success",
            'prediction':'failure',
            'failure_probability':round(probs[1], 4),
            "maintenance_required": True,
            "message": "Equipment failure risk detected. Maintenance is recommended."
            }
        else:
            output = {
                    "status": "success",
                    'prediction':'working',
                    'failure_probability':round((probs[1]), 4),
                    "maintenance_required": False,
                    "message": "Equipment is operating normally. No maintenance required."
                    }
        return output
    except ValueError as e:
        raise HTTPException(
            status_code=400,
            detail=f"Invalid input: {str(e)}"
        )

    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"An unexpected error occurred while making the prediction.",
        )