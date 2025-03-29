# 📁 app/clients/service/model_registry.py

import os
import pickle
from sklearn.base import BaseEstimator

# All available models (you can expand this)
MODEL_REGISTRY = {
    "random_forest": "model_rf.pkl",
    "linear_regression": "model_lr.pkl",
    "svm": "model_svm.pkl"
}

# Holds the currently active model (default: random_forest)
CURRENT_MODEL_NAME = "random_forest"
CURRENT_MODEL = None


def load_model(model_name: str) -> BaseEstimator:
    if model_name not in MODEL_REGISTRY:
        raise ValueError(f"Model '{model_name}' not registered.")
    model_path = os.path.join(os.path.dirname(__file__), MODEL_REGISTRY[model_name])
    with open(model_path, "rb") as f:
        return pickle.load(f)


def set_current_model(model_name: str):
    global CURRENT_MODEL_NAME, CURRENT_MODEL
    CURRENT_MODEL = load_model(model_name)
    CURRENT_MODEL_NAME = model_name


def get_current_model():
    return CURRENT_MODEL


def get_current_model_name():
    return CURRENT_MODEL_NAME


def get_available_models():
    return list(MODEL_REGISTRY.keys())


# Load default model on import
set_current_model(CURRENT_MODEL_NAME)
