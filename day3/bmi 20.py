height = float(input('enter ur height m'))
weight = float(input('enter your weight kg'))
bmi = weight / (height * height)
print(bmi)

#code 2.0
if bmi <= 18.5:
    print("you are underweight")
elif bmi <= 25 and bmi > 18.5:
    print("you are normal weight")
elif bmi <= 30 and bmi > 25:
    print("you are overweight")
elif bmi > 30 and bmi < 35:
    print("you are obese")
else:
    print("you are clinically obese")
