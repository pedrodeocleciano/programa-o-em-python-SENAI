#1

import random

numero = random.randint(5, 10)
print(numero)

#2

import random

numeros = [random.randint(1, 100) for _ in range(3)]
print(numeros)

#3

import random

numero_range = random.choice(range(10, 31))
print(numero_range)

#4

for i in range(10, 0, -1):
    print(i)
print("Fogo!")

#5

limite = int(input("Insira um número inteiro positivo: "))
soma = 0

# Loop de 2 até o número inserido (inclusive)
for i in range(2, limite + 1):
    # Verifica se o número é par usando o módulo %
    if i % 2 == 0:
        soma += i

print(f"A soma dos números pares é: {soma}")


#6

num = int(input("Insira um número para ver a tabuada: "))

for i in range(1, 11):
    resultado = num * i
    print(f"{num} x {i} = {resultado}")

#7

for i in range(99, 0, -2):
    print(i)
