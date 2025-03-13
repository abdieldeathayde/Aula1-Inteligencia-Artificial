
opcao = int(input("Digite 0 para sair, 1 para soma, 2 para subtração, 3 para multiplicação e 4 para divisão: "))

def soma (a, b):
    return a + b
def subtracao (a, b):
    return a - b
def multiplicacao (a, b):
    return a * b
def divisao (a, b):
    return a / b

while opcao != 0:
    a = int(input("Digite o valor de a: "))
    b = int(input("Digite o valor de b: "))
    if opcao == 1:
        print(soma(a, b))
    elif opcao == 2:
        print(subtracao(a, b))
    elif opcao == 3:
        print(multiplicacao(a, b))
    elif opcao == 4:
        print(divisao(a, b))
    else:
        print("Opção inválida")
        
    opcao = int(input("Digite 0 para sair, 1 para soma, 2 para subtração, 3 para multiplicação e 4 para divisão: "))