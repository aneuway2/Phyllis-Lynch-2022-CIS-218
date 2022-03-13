"""bmi checker phyllis lynch"""


def calculate_bmi(height, weight):
    """calculate bmi from inout"""
    bmi = round(weight / height / height * 703, 1)
    print(f"the bmi is", bmi, "which is ", category)
    return bmi


def test_calculate_bmi(bmi):
    assert calculate_bmi(59, 143), 28.9
    assert calculate_bmi(63, 200), 35.4
    assert calculate_bmi(50, 215), 60.5
    assert calculate_bmi(48, 95), 29.0


def bmi_to_category(bmi):
    if bmi < 18.5:
        return "underweight"
    if bmi > 18.5 < 24.9:
        return "healthy"
    if bmi > 24.9 < 29.9:
        return "unhealthy"
    if bmi > 29.9:
        return "Obese"


def test_bmi_to_category(category):
    assert bmi_to_category(10) == "underweight"
    assert bmi_to_category(23) == "healthy"
    assert bmi_to_category(26) == "unhealthy"
    assert bmi_to_category(60) == "obese"


height = float(input("Enter your height in inches please. "))
weight = float(input("Enter your weight in pounds please. "))
bmi = round(weight / height / height * 703, 1)
if bmi:
    if bmi < 18.5:
        category = "underweight"
    if bmi > 18.5 < 24.9:
        category = "healthy"
    if bmi > 24.9 < 29.9:
        category = "unhealthy"
    if bmi > 29.9:
        category = "Obese"
    bmi_to_category(bmi)
bmi = calculate_bmi(height, weight)
cat = bmi_to_category(bmi)
test_calculate_bmi(height, weight)
test_bmi_to_category(category)
