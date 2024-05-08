def is_prime(number):
        prime = False

        if number == 1:
            print(f"{number} is not a prime number")
       
        elif number > 1: 
             for i in range(2, number):
                   if number % i == 0 and i != number:
                         prime = True
                         break
        if prime == True:
              print(f"{number} is not a prime number")
        else:
              print(f"{number} is a prime number")
              
is_prime(2)        
           
