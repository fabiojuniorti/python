# Validação de idade
while True:
    idade = int(input("Digite sua idade: "))
    if idade >= 0:
        break  # Só sai do laço se a idade for válida
    print("Idade inválida. Tente novamente!")
