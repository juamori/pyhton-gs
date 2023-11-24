# Função para autenticar o usuário
def autenticar_usuario():
    usuarios_cadastrados = {'usuario1': 'senha123', 'usuario2': 'senha456'}

    while True:
        usuario = input("Digite o nome de usuário: ")
        senha = input("Digite a senha: ")

        if usuario in usuarios_cadastrados and usuarios_cadastrados[usuario] == senha:
            print("Login bem-sucedido!\n")
            return usuario
        else:
            print("Usuário ou senha incorretos. Tente novamente.\n")

# Função que exibe as opções de funcionalidade
def exibir_opcoes(usuario):
    print(f"Bem-vindo, {usuario}!\n")
    while True:
        print("Escolha uma opção:")
        print("1. Funcionalidade 1")
        print("2. Funcionalidade 2")
        print("3. Funcionalidade 3")
        print("0. Sair")

        try:
            escolha = int(input("Digite o número da opção desejada: "))
            if escolha == 0:
                print("Saindo do programa. Até logo!")
                break
            elif escolha == 1:
                print("Executando Funcionalidade 1.\n")
            elif escolha == 2:
                print("Executando Funcionalidade 2.\n")
            elif escolha == 3:
                print("Executando Funcionalidade 3.\n")
            else:
                print("Opção inválida. Tente novamente.\n")
        except ValueError:
            print("Por favor, digite um número válido.\n")

# Programa principal
def main():
    usuario_autenticado = autenticar_usuario()
    exibir_opcoes(usuario_autenticado)

if __name__ == "__main__":
    main()
