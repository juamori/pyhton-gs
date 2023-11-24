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

class ConsultaMedica:
    def __init__(self, nome, idade, gravidez_anterior, complicacoes_anteriores):
        self.nome = nome
        self.idade = idade
        self.gravidez_anterior = gravidez_anterior
        self.complicacoes_anteriores = complicacoes_anteriores
        self.consultas_prenatais = []

    def exibir_historico(self):
        print(f"\nHistórico Médico de {self.nome}:\nIdade: {self.idade}\nGravidez Anterior: {self.gravidez_anterior}\nComplicações Anteriores: {self.complicacoes_anteriores}\nConsultas Pré-natais:")

        for consulta in self.consultas_prenatais:
            print("Data:", consulta['Data'])
            print("Peso: {} kg".format(consulta['Peso']))
            print("Pressão Arterial: {}/{} mmHg".format(*consulta['Pressao_Arterial']))
            print("Batimentos Cardíacos Fetais: {} bpm".format(consulta['Batimentos_Cardiacos_Fetais']))
            print("\n\n\n---")

    def adicionar_consulta_prenatal(self, data, peso, pressao_arterial, batimentos_cardiacos_fetais):
        consulta = {
            'Data': data,
            'Peso': peso,
            'Pressao_Arterial': pressao_arterial,
            'Batimentos_Cardiacos_Fetais': batimentos_cardiacos_fetais
        }
        self.consultas_prenatais.append(consulta)
        data = input("Digite a data da consulta (formato YYYY-MM-DD): ")
        peso = float(input("Digite o peso (em kg) na consulta: "))
        pressao_arterial = tuple(map(int, input("Digite a pressão arterial (sistólica diastólica, separadas por espaço): ").split()))
        batimentos_cardiacos_fetais = int(input("Digite os batimentos cardíacos fetais: "))
        print("Consulta agendada com sucesso!\n\n\n")

a = ConsultaMedica("Iohanna", 22, "não", "não")

# Função que exibe as opções de funcionalidade
def exibir_opcoes(usuario):
    print(f"Bem-vindo, {usuario}!\n")

    while True:
        print("Escolha uma opção:")
        print("1. Historico do paciente")
        print("2. Agendar consulta")
        print("0. Sair")

        try:
            escolha = int(input("Digite o número da opção desejada: "))
            if escolha == 0:
                print("Saindo do programa. Até logo!")
                break
            elif escolha == 1:
                print(a.exibir_historico())
            elif escolha == 2:
                print(a.adicionar_consulta_prenatal("29/11/2023", 70, 120, 70))
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