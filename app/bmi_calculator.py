import math


class BMICalculator:
    # range is in [a, b)
    underweight_range = [0, 18.5]
    normal_range = [18.5, 25]
    overweight_range = [25, 2 ** 32 - 1]

    def __init__(self, weight_in_kg: float, height_in_m: float):
        if weight_in_kg <= 0:
            raise ValueError("Invalid weight value")

        if height_in_m <= 0:
            raise ValueError("Invalid height value")

        self.weight = weight_in_kg
        self.height = height_in_m

    def get_bmi_value(self) -> float:
        if self.height <= 0:
            raise ValueError("Invalid height value")

        bmi_value = self.weight / (self.height ** 2)
        # round to 2 decimal places
        bmi_value = int(bmi_value * 100) / 100

        return bmi_value

    def get_bmi_label(self) -> str:
        bmi_value = self.get_bmi_value()

        if (
            self.underweight_range[0] <= bmi_value
            and bmi_value < self.underweight_range[1]
        ):
            return "underweight"
        elif self.normal_range[0] <= bmi_value and bmi_value < self.normal_range[1]:
            return "normal"
        elif (
            self.overweight_range[0] <= bmi_value
            and bmi_value < self.overweight_range[1]
        ):
            return "overweight"
        else:
            raise ValueError("Invalid BMI value")
