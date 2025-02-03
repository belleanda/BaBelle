class BMICalculator:
    CATEGORIES = [
        (lambda bmi: bmi < 18.5, "Underweight"),
        (lambda bmi: bmi < 25, "Normal weight"),
        (lambda bmi: bmi < 30, "Overweight"),
        (lambda bmi: bmi >= 30, "Obesity")
    ]

    def __init__(self, weight, height):
        self.weight = weight
        self.height = height

    def calculate_bmi(self):
        return self.weight / (self.height ** 2)

    def get_bmi_category(self):
        bmi = self.calculate_bmi()
        category = next(label for condition, label in self.CATEGORIES if condition(bmi))
        return bmi, category

weight = float(input("Enter weight (kg): "))
height = float(input("Enter height (m): "))

bmi_calc = BMICalculator(weight, height)
bmi_value, bmi_status = bmi_calc.get_bmi_category()

print(f"BMI is {bmi_value:.1f}")
print(bmi_status)