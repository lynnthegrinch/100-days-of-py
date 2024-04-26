print("welcome to the tip calculator")
#ask how much money spent
money_spent = int(input("how much money have you spent?"))
tip_perc = int(input("what percentage tip you wanna give? 10, 12, 15?"))
people = int(input("how many people split the bill?"))
to_pay = money_spent // people
tip_to_pay = to_pay * tip_perc / 100
print(f"you should pay {round(tip_to_pay, 2)} in tip each")
