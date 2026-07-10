#tset 2
print("4. BMI Calculator:")
print("   - Ask for weight (kg) and height (m)")
print("   - Calculate: BMI = weight / (height ** 2)")
print()


#input
height = float(input("Enter height"))
weight = float(input("Enter weight"))

#process
BMI = weight / height ** 2

#output
print ("BMI:", BMI)