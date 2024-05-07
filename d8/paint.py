import math
def paint_calc(height, width, cover):
    calc = math.ceil((height * width)/ cover)
    print(f"you will need {calc} cans of paint")
#how i did it
# calc = (height * width)/ cover
#calc_r = round(calc)
#though it rounds down thats why i had to import math 
#yeah yeah ikik
#write above

test_h = int(input("height of wall: "))
test_w = int(input("width of wall: "))
coverage = 5
paint_calc(height=test_h, width=test_w, cover=coverage)
