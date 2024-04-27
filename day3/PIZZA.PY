print("welcome to pizza place")
size = input("what size? S M or L")
pepperoni = input("want pepperoni? Y N")
cheese = input("want extra cheese? Y N")

price = 0
if size == "S":
    price += 15             
elif size == "M":
    price += 20
else:
    price += 25

if pepperoni == "Y" and size == "s":
    price += 2
elif pepperoni == "Y":
    price += 3

if cheese == "Y":
    price += 1

print(f"your bill is {price}$")
