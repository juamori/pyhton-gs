# Função que recebe dois parâmetros e retorna a soma
def somar(a, b):
    resultado = a + b
    return resultado

# Função que recebe um parâmetro e retorna o quadrado
def quadrado(numero):
    return numero ** 2

# Função que não recebe parâmetros, mas imprime uma mensagem
def mensagem():
    print("Esta é uma mensagem da função.")

# Exemplos de uso das funções
soma_resultado = somar(3, 5)
print("Resultado da soma:", soma_resultado)

quadrado_resultado = quadrado(4)
print("Resultado do quadrado:", quadrado_resultado)

mensagem()
