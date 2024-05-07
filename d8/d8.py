def greet(): #creating function recap
    print('hello')
    print('whats it like today?')
    print('isnt the weather nice today?')
greet()

def greet1(name): #adding variables
    print(f'hello {name}')
    print(f'whats it like today?')
    print('isnt the weather nice today?')
greet1('Valentina')

def greet2(name, location):
    print(f'hello {name}')
    print(f'whats it like in {location} today?')
    print('isnt the weather nice today?')
greet('Valentina', 'rome') #positional assignment

greet(location='rome', name= "valentina") #keyword assignment
