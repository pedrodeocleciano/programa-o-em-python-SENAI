#1

def comparar(num1, num2): 
    if num1 % 2 == 0:
     print(f"{num1} e par")
    else:
        print(f'{num1} e impar')

    if num2 % 2 == 0:
         print(f'{num2} e par')
    else:
         print(f'{num2} e impar')

n1 = int(input('digite o primeiro numero: '))
n2 = int(input('digite o segundo numero: '))
comparar(n1, n2)

#2

def multiplicar(a, b, c):
    resultado = a * b * c
    print('resultado: ', resultado)

n1 = int(input('digite o primeiro numero: '))
n2 = int(input('digite o segundo numero: '))
n3 = int(input('digite o terceiro numero: '))

multiplicar(n1, n2, n3)

#3

def potencia(base, espoente):
    resultado = base ** expoente
    print('resultado: ', resultado)

base = int(input('digite a base: '))
expoente = int(input('digite o expoente: '))

potencia(base, expoente)

#4

def verificar_idade(idade):
    if idade == 18:
        print('parabens, voce tem 18 anos.')
    else:
        print('idade diferente de 18 anos,')
idade = int(input('digite sua idade: '))
verificar_idade(idade)

#5

def descobrir_idade(ano_nascimento):
    idade = 2026 - ano_nascimento
    print('sua idade e: ', idade)
ano = int(input('digite seu ano de nascimento: '))

descobrir_idade(ano)

#6

def copa(ano):
    if ano == 1999:
        print('Nao. O Brasil nao ganhou a copa do munndo de 1999.')
    else:
        print('digite o ano de 1999.')
ano = int(input('digite um ano: '))
copa(ano)

#7

def cumprimentar():
    print('bem-vindo ao restaurante')
def restaurante():
    cardapio = ['salada', 'macaronada', 'sanduiche', 'sorvete']

    print('\nCardapio: ')
    for i in range(len(cardapio)):
        print(f'{i + 1} - {cardapio[i]}')
opcao = int(input('escolha uma opcao: '))

if opcao >= 1 and opcao <= len(cardapio):
    print('voce escolheu:', cardapio[opcao - 1 ])
else:
    print('opcao invalida')
cumprimentar()
restaurante()

    


