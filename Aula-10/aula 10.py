#1

n = 0
while n <= 1000:
    print(n)
    n += 1

#2

    senha_correta = "1234"

tentativas = 0

while tentativas < 3:

    senha = input("Digite a senha: ")

    if senha == senha_correta:

        print("Acesso permitido!")

        notas = []

        quantidade = int(input("Quantas notas deseja inserir? "))

        for i in range(quantidade):

            nota = float(input(f"Digite a {i+1}ª nota: "))

            notas.append(nota)

        soma = 0

        for nota in notas:

            soma += nota

        media = soma / len(notas)

        print("\nNotas:", notas)

        print("Média:", media)

        if media >= 7:

            print("Situação: Aprovado")

        elif media >= 5:

            print("Situação: Recuperação")

        else:

            print("Situação: Reprovado")

        break

    else:

        tentativas += 1

        print("Senha incorreta!")

        print("Tentativas restantes:", 3 - tentativas)

if tentativas == 3:

    print("Conta bloqueada! Você errou a senha 3 vezes.")

input("Digite enter para sair")





