#1

n = int(input('digite um numero: '))
if n >=1:
    print('positivo')
elif n >= 0:
    print('zero')
else: 
    print('negativo')  

#2

idade = int(input("digite sua idade: "))
if idade >=18:
    print('pode votar')
else:
    print('nao pode votar')

    #3

var = 7
if var % 2 == 0:
    print("O número não é par.")
else:
    print("O número impar.")

#4

us1 = int(input("digite 1 numero: "))
us2 = int(input("digite o numero 2: "))
us3 = int(input("digite o numero 3: "))
if us1 == us2 == us3:
 print("equilatero")
elif us1 == us2 != us3:
    print('isoceles')
else:
    print('escaleno')

    #5 

mult = int(input('escolha um numero: '))
if mult % 5 == 0 and mult % 7 == 0: 
    print(' e multiplos dos 2')
else:
    print(" nao e multiplo")

    #6

n2 = int(input('digite um numero: '))
if n2 >=1: 
    print("e positivo e menor que 10")
elif n2 >10:
    print('e positivo e maior que 10')
else:
    print('nao e positivo e nem maior que 10')

    #7

numero = int(input('digite um numero: '))
if numero % 3 == 0 and numero % 5 == 0:
    print("o numero e divisivel por 3 ou 5")
else:
    print("nao e divisivel por 3 nem por 5")






