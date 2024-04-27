year = int(input("give me a year"))
if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print("this is a leap year")
        else:
            print("this is not a leap year anymore")
    else:
        print("this is not a leap year anymore")
else:
    print("this is not a leap year")
