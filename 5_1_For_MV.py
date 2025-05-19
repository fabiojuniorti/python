# Cálculo da média
soma = 0
for i in range(3):  # Pergunta 3 vezes
    nota = float(input("Digite uma nota: "))
    soma += nota  # Acumula as notas
media = soma / 3  # Calcula a média
print(f"Média: {media}")
