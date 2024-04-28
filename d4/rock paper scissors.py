import random
print("type 0 for rock, type 1 for paper, type 2 for scissors")
user = int(input('rock, paper, scissors?'))
pc = random.randint(0, 2)

if pc == 0 and user == 0:
   print('user has picked rock, pc has picked rock')
   print("it's a tie")
elif pc == 0 and user == 1:
    print('user has picked rock, pc has picked paper')
    print("pc wins")
elif pc == 0 and user == 2:
    print('user has picked rock, pc has picked scissors')
    print("user wins")
elif pc == 1 and user == 0:
    print('user has picked paper, pc has picked rock')
    print("user wins")
elif pc == 1 and user == 1:
    print('user has picked paper, pc has picked paper')
    print("it's a tie")
elif pc == 1 and user == 2:
    print('user has picked paper, pc has picked scissors')
    print("pc wins")
elif pc == 2 and user == 0:
    print('user has picked scissors, pc has picked rock')
    print("pc wins")
elif pc == 2 and user == 1:
    print('user has picked scissors, pc has picked paper')
    print("user wins")
elif pc == 2 and user == 2:
    print('user has picked scissors, pc has picked scissors')
    print("it's a tie")
