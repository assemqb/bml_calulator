from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

# Input model for the request body
class BMIInput(BaseModel):
    height: float  # Height in meters
    weight: float  # Weight in kilograms

@app.post("/calculate_bmi")
def calculate_bmi(data: BMIInput):
    # Validate input
    if data.height <= 0 or data.weight <= 0:
        raise HTTPException(
            status_code=400, 
            detail="Height and weight must be positive numbers."
        )
    
    # Calculate BMI
    bmi = data.weight / (data.height ** 2)
    bmi = round(bmi, 2)

    # Classify BMI
    if bmi < 18.5:
        classification = "Underweight"
    elif 18.5 <= bmi <= 24.9:
        classification = "Normal weight"
    elif 25 <= bmi <= 29.9:
        classification = "Overweight"
    else:
        classification = "Obesity"

    return {"bmi": bmi, "classification": classification}
