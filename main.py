from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

#model for the request body
class BMIInput(BaseModel):
    height: float  #height (meter)
    weight: float  #weight (kilogram)

@app.post("/calculate_bmi")
def calculate_bmi(data: BMIInput):
    #Validate input
    if data.height <= 0 or data.weight <= 0:
        raise HTTPException(
            status_code=400, 
            detail="Height and weight must be positive numbers."
        )
    
    #calculate BMI
    bmi = data.weight / (data.height ** 2)
    bmi = round(bmi, 2)

    #Classify
    if bmi < 18.5:
        classification = "Underweight"
    elif 18.5 <= bmi <= 24.9:
        classification = "Normal weight"
    elif 25 <= bmi <= 29.9:
        classification = "Overweight"
    else:
        classification = "Obesity"

    return {"bmi": bmi, "classification": classification}
