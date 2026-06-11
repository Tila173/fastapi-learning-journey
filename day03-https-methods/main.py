from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def hello():
    return {'message':'Hello World'}

import json

app = FastAPI()

# Helper function to load data
def load_patients():
    with open("patients.json", "r") as file:
        return json.load(file)


# Root route
@app.get("/")
def hello():
    return {"message": "Hello World"}


# Get all patients
@app.get("/patients")
def get_patients():
    return load_patients()


# Get patient by ID
@app.get("/patients/{patient_id}")
def get_patient(patient_id: int):
    patients = load_patients()

    for patient in patients:
        if patient["id"] == patient_id:
            return patient

    return {"error": "Patient not found"}