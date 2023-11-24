# Solicita ao usuário que insira seu nome
nome = input("Digite seu nome: ")

# Solicita ao usuário que insira sua senha (a entrada é convertida para inteiro)
senha = int(input("Digite sua senha: "))

# Exibe uma mensagem com base na entrada do usuário
print("Olá, {}! Você tem {} anos.".format(nome, senha))
