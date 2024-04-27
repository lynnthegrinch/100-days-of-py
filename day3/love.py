print("welcome to the love calculator")
name1 = input("what is your name? \n").lower()
name2 = input("what is your crush's name? \n").lower()

names = name1 + name2
t = names.count("t")
r = names.count("r")
u = names.count("u")
e = names.count("e")
true = t + u + r + e
l = names.count("l")
o = names.count("o")
v = names.count("v")
E = names.count("e")
love = l + o + v + E
percentage = str(true) + str(love)
print(f"your percentage of true love is {percentage}%")
