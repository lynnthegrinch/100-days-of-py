def add(n1, n2):
    return n1 + n2
def sub(n1, n2):
    return n1 - n2
def mult(n1, n2):
    return n1 * n2
def div(n1, n2):
    return n1 / n2

operations = {"+": add, "-": sub, "*": mult, "/": div,}
def calc():
    n1= float(int(input("gimme number")))
    for i in operations:
        print(i)
    keep_going = True
    while keep_going:
        choice = input("what operation do you want to do?")
        n2 = float(int(input("gimme number")))
        calc_func = operations[choice]
        answer = calc_func(n1, n2)
        print(f"{n1} {choice} {n2} = {answer}")
        if input(f"type y to keep going with {answer}: ") == "y":
            n1 = answer
        else:
          keep_going = False
          calc()
calc()
