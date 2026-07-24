
def get_bmi_category(bmi):
    if bmi < 18.5:
        return "Underweight"
    elif bmi < 25.0:
        return "Normal weight"
    elif bmi < 30.0:
        return "Overweight"
    else:
        return "Obese"


def main():
    weight = float(input("Enter your weight (kg): "))
    height = float(input("Enter your height (m): "))

    bmi = weight / (height ** 2)
    category = get_bmi_category(bmi)

    print(f"\nYour BMI is: {bmi:.1f}")
    print(f"Category: {category}")


if __name__ == "__main__":
    main()