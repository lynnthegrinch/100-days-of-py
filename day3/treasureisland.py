print("welcome to treasure island")
print("your mission is to find the treasure")
left_right = input("left or right?").lower()
if left_right == 'right':
    print("you fall into a hole, game over")
elif left_right == 'left':
    swim_boat = input("will you swim or wait").lower()
    if swim_boat == 'swim':
        print("you were attacked by trout, game over.")
    elif swim_boat == 'wait':
        door = input("which door? Yellow, red or blue").lower()
        if door == 'yellow':
            print("you win")
        elif  door == 'red':
            print("you were burned by fire, game over")
        elif door == 'blue':
            print("you were eaten by beasts, game over")
        else:
            print("game over")
