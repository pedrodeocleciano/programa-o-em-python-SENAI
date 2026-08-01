#1

import statistics
def calcular_media(notas):

    return statistics.mean(notas)
def calcular_moda(notas):

    try:

        return statistics.mode(notas)

    except statistics.StatisticsError:

        return "Não há moda."
def calcular_desvio(notas):

    return statistics.stdev(notas)
def menor_nota(notas):

    return min(notas)

def maior_nota(notas):

    return max(notas)

notas = []
quantidade = int(input("Quantos alunos deseja cadastrar? "))
for i in range(quantidade):

    nota = float(input(f"Digite a nota do aluno {i + 1}: "))

    notas.append(nota)
print("\n===== ESTATÍSTICAS DAS NOTAS =====")
print(f"Notas: {notas}")
print(f"Média: {calcular_media(notas):.2f}")
print(f"Moda: {calcular_moda(notas)}")
print(f"Desvio padrão: {calcular_desvio(notas):.2f}")
print(f"Menor nota: {menor_nota(notas)}")
print(f"Maior nota: {maior_nota(notas)}")

#2

import statistics

empresa1 = [1000, 6000, 1200, 8000, 1400]
empresa2 = [5000, 4000, 3000, 2000, 7000]
empresa3 = [1200, 1300, 8000, 3000, 15000]
empresa4 = [1400, 1750, 2000, 4500, 5900]

def mostrar_estatisticas(nome, salarios):
    print(f"\n{nome}")
    print(f"Salários: {salarios}")
    print(f"Média: {statistics.mean(salarios):.2f}")
    print(f"Moda: {statistics.multimode(salarios)}")
    print(f"Mediana: {statistics.median(salarios)}")
    print(f"Desvio padrão: {statistics.stdev(salarios):.2f}")

mostrar_estatisticas("Empresa 1", empresa1)
mostrar_estatisticas("Empresa 2", empresa2)
mostrar_estatisticas("Empresa 3", empresa3)
mostrar_estatisticas("Empresa 4", empresa4)

print("\nMinha escolha: Empresa 2")
print("Justificativa:")
print("- Possui uma média salarial alta.")
print("- A mediana é de R$ 4.000, mostrando salários equilibrados.")
print("- O desvio padrão é menor que o das empresas 1 e 3, indicando menor variação entre os salários.")
print("- Assim, oferece um bom equilíbrio entre bons salários e estabilidade.")