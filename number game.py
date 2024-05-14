import random
random_number = 0 #setting up the basics
attempts_left = 0
art = """
 ____ ____ ____ ____ ____ _________ ____ ____ ____ _________ ____ ____ ____ ____ ____ ____ ____ 
||G |||u |||e |||s |||s |||       |||t |||h |||e |||       |||n |||u |||m |||b |||e |||r |||! ||
||__|||__|||__|||__|||__|||_______|||__|||__|||__|||_______|||__|||__|||__|||__|||__|||__|||__||
|/__\|/__\|/__\|/__\|/__\|/_______\|/__\|/__\|/__\|/_______\|/__\|/__\|/__\|/__\|/__\|/__\|/__\|
"""
def difficulty(diff): #setting difficulty 
    if diff == 'hard': #attempts_hard  5
        print("you have 5 attemps")
        return 5

    elif diff == 'easy': #attempts_easy  10
        print("you have 10 attempts")
        return 10
def numb(): #to determine random number
    rand = random.randint(1, 100)
    return rand
def left(n1, n2): #to calculate difference
     left = n1 + 1 - n2
     return left
print(art)
print("Guess the number between 1 and 100")     
game = True #preparing the loop
while game == True:
    diffy = input("select your difficulty: easy or hard?\n")
    attempts_left = difficulty(diffy)
    attempts = 0
    random_number = numb()

    while attempts <= attempts_left: #loop for the tries
            guess = int(input("please guess the number\n"))
            if guess == random_number:
                print("you win")
                break
            elif guess < random_number:
                print("too low")
                attempts += 1
                att_left = left(attempts_left, attempts)
                print(f"you have {att_left} attempts left")
                continue
            elif guess > random_number:
                print("too high")
                attempts += 1
                att_left = left(attempts_left, attempts)
                print(f"you have {att_left} attempts left")
                continue
            else:
                 print("please try with a number between 1 and 100")
    print(f"the number was: {random_number}")
    try_again = input("wanna try again?y or\n")
    if try_again == "n":
            print("goodbye")
            game = False
    elif try_again == "y":
            continue
    else:
         break
