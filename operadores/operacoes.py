def soma(a, b):
    return a + b
    menu()
def subtracao(a, b):
    return a - b
    menu()
def multiplicacao(a, b):
    return a * b
    menu()
def divisao(a, b):
    return a / b
    menu()

def menu():
    opcao = int(input("Digite 0 para sair, 1 para soma, 2 para subtração, 3 para multiplicação e 4 para divisão: "))
    
    match opcao:
        case 0:
            print("Saindo...")
        case 1:
            a = int(input("Digite o valor de a: "))
            b = int(input("Digite o valor de b: "))
            print(soma(a, b))
        case 2:
            a = int(input("Digite o valor de a: "))
            b = int(input("Digite o valor de b: "))
            print(subtracao(a, b))
        case 3:
            a = int(input("Digite o valor de a: "))
            b = int(input("Digite o valor de b: "))
            print(multiplicacao(a, b))
        case 4:
            a = int(input("Digite o valor de a: "))
            b = int(input("Digite o valor de b: "))
            print(divisao(a, b))
            
menu()