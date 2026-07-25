c1 = input('digite seu nome e seua idade')
c2 = input('digite seu nome e seua idade')
c3 = input('digite seu nome e seua idade')

q1 = 'simples'
q2 = 'duplo'
q3 = 'luxo'

simples = 100
duplo = 150
luxo = 250

dias = []
valores2= 0
valores = [100, 150, 250]
quartos = ['simples', 'duplo', 'luxo']

print('quartos disponiveis')
print('1. simples - 100')
print('2. duplo - 150')
print('3. luxo - 250')

escolha1 = input('escolha o quarto e quantos dias voce quer ficar ')

if escolha1 == "1":
    dias.append(quartos[0])
    valores2 += valores[0]
elif escolha1 == '2':
    dias.append(quartos[1])
    valores2 += valores [1]
elif escolha1 == '3':
    dias.append(quartos[2])
    valores2 += valores [2]
elif escolha1 == '2':
    dias.append(quartos[1])
    valores2 += valores [1]


