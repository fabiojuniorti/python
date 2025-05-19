# Laço while com controle de fluxo
soma = 0
while soma < 10:  # A repetição vai ocorrer enquanto a soma for menor que 10
    numero = int(input("Digite um número: "))  # Entrada do usuário
    soma += numero  # Adiciona o número à soma
    print(f"Soma até agora: {soma}")
