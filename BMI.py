weight =  float(input("Enter your weight in kg's: "))

height = float(input("Enter your height in meters: "))

a = height * 0.3048 # changing height in feet to meters

BMI = (weight)/ (a*a)

print(round(BMI,2))

'''BMI	Status
≤ 18.4	Underweight
18.5 - 24.9	Normal
25.0 - 39.9	Overweight
≥ 40.0	Obese'''

if(BMI<=18.5):
    print("Underweight")

elif(BMI <=24.9):
    print("Normal")

elif(BMI <= 39.9):
    print("Overweight")

elif(BMI>=40):
    print("Obesity", end="")
    print(" Need to pay more attention")

elif(BMI<=0):
    print("Enter valid input")

