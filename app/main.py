from fastapi import FastAPI
from fastapi.exceptions import HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from .bmi_calculator import BMICalculator

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# Data structure for response
class BMIResult(BaseModel):
    bmi: float
    label: str


@app.get("/", summary="calculate and label bmi")
def calculate_bmi(weight: float, height: float) -> BMIResult:
    if weight <= 0:
        raise HTTPException(400, "Weight should be > 0 kg")
    if height <= 0:
        raise HTTPException(400, "Height should be > 0 m")

    bmi_calc = BMICalculator(weight, height)

    return BMIResult(bmi=bmi_calc.get_bmi_value(), label=bmi_calc.get_bmi_label())
