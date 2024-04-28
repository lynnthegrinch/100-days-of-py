row1 = ['1', '2', '3']
row2 = ['1', '2', '3']
row3 = ['1', '2', '3']

map_ = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("where do you want to hide the treasure?")
if position == "11":
    row1[0] = 'x'

elif position == "12":
    row1[1] = 'x'

elif position == "13":
    row1[2] = 'x'

elif position == "21":
    row2[0] = 'x'

elif position == "22":
    row2[1] = 'x'

elif position == "23":
    row2[2] = 'x'

elif position == "31":
    row3[0] = 'x'

elif position == "32":
    row3[1] = 'x'

elif position == "33":
    row3[2] = 'x'

print(map_)
