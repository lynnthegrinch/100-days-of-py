"""program to make coffeeeee"""
MACHINE = True
water_ml = 300
milk_ml = 200
coffee_g = 100
water_need = 0
milk_need = 0
coffee_need = 0
money = 0

def report():
    print("===================")
    print("report: ")
    print(f"water: {water_ml}")
    print(f"milk: {milk_ml}")
    print(f"coffee: {coffee_g}")
    print(f"money: {money}")
    print("===================")

def prep():
    global water_ml
    global milk_ml
    global coffee_g
    print("checking for ingredients\n")
    if water_ml != 0 or coffee_g != 0 or milk_ml != 0:
        if water_ml >= water_need and milk_ml >= milk_need and coffee_g >= coffee_need:
            print("ingredients found\n")
            water_ml -= water_need
            milk_ml -= milk_need
            coffee_g -= coffee_need
            print("your drink is almost ready\n")
            return water_ml, milk_ml, coffee_g
    else:
        return "sorry, cant prepare your coffee, ingredients missing\n"
def cash():
    global money
    global water_ml
    global milk_ml
    global coffee_g
    quarters = float(input("please insert quarters\n"))
    dime = float(input('please insert dimes\n'))
    nickles = float(input('please insert nickles\n'))
    penny = float(input('please insert penny\n'))
    totq = 0.5 * quarters
    totd = 0.1 * dime
    totn = 0.05 * nickles
    totp = 0.01 * penny
    total_cash = totq + totd + totn + totp
    if total_cash >= coins_need:
        change = total_cash - coins_need
        money += total_cash
        if change > 0.0:
            return f"this is your change: {change}"
    else:
        water_ml += water_need
        milk_ml += milk_need
        coffee_g += coffee_need
        print(water_ml, milk_ml, coffee_g)
        return "please try again, not enough coins\n"
def maintenance():
    global MACHINE
    if other_choices == 1:
        report()
    elif other_choices == 2:
        print(MACHINE)
        on_or_off = input("would you like to turn off the machine? y or n\n")
        if on_or_off == 'y':
            MACHINE = False


while MACHINE:
    print("welcome to lynn's coffee")
    choice = int(input("what would you like?\n1. coffee\n2. latte\n3. cappuccino\n4. maintenance\n"))
    if choice == 1:
        print("you have selected coffee")
        water_need = 50
        milk_need = 0
        coffee_need = 18
        coins_need = 1.5
    elif choice == 2:
        print("you have selected latte")
        water_need = 200
        milk_need = 150
        coffee_need = 24
        coins_need = 2.5
    elif choice == 3:
        print("you have selected cappuccino")
        water_need = 250
        milk_need = 100
        coffee_need = 24
        coins_need = 3.0
    elif choice == 4:
        other_choices = int(input("what would u like to do?\n 1. report\n 2. status\n "))
        maintenance()
    else:
        print("no valid choice found")
        print("please try again")
        continue
    if choice in [1, 2, 3]:
        result = prep()
        mon = cash()
        print(result)
        print(mon)
    if water_ml == 0 or coffee_g == 0 or milk_ml == 0:
        on_or_off = input("would you like to turn off the machine? y or n \n")
        if on_or_off == 'y':
            MACHINE = False
