# 📁 app/clients/service/model_router.py

from fastapi import APIRouter, HTTPException
from app.clients.service.logic import interpret_and_calculate
from app.clients.schema import PredictionInput

from app.clients.service import model_registry

router = APIRouter(prefix="/models", tags=["models"])


@router.get("/", summary="List all available ML models")
def list_models():
    return {"available_models": model_registry.get_available_models()}


@router.get("/current", summary="Get the current model in use")
def get_current_model():
    return {"current_model": model_registry.get_current_model_name()}


@router.post("/switch/{model_name}", summary="Switch to a different ML model")
def switch_model(model_name: str):
    try:
        model_registry.set_current_model(model_name)
        return {"message": f"Switched to model: {model_name}"}
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.post("/predictions")
async def predict(data: PredictionInput):
    return interpret_and_calculate(data.model_dump())