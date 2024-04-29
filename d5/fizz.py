# Write code below 💖
number = 0
while number <= 100:
  print(number)
  number = number +1
  if  number %3 == 0 and number %5 == 0:
    print("fizzbuzz")
    number = number +1
  elif number %5 == 0:
    print("buzz")
    number = number +1
  elif number %3 == 0:
    print("fizz")
    number = number +1
