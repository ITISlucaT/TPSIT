#Trovo il fattoriale di un numero inserito in input

# user_input = int(input("Inserisci numero di cui calcolare il fattoriale: "))

# factorial = 1
# for i in range(1, user_input+1):
#     factorial *= i
# print(factorial)


#TOR modo più pythonico con libreria math

import math

user_input = int(input("Inserisci numero di cui calcolare il fattoriale: "))
print(math.factorial(user_input))
