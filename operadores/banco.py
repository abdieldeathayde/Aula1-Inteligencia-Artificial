class Banco:
    def __init__(self):
        self.notas = [100, 50, 10, 1]
        self.notas_qtd = [0, 0, 0, 0]
        self.valor = 0

    def calcular_notas(self):
        for i in range(len(self.notas)):
            self.notas_qtd[i] = self.valor // self.notas[i]
            self.valor -= self.notas_qtd[i] * self.notas[i]

    def imprimir_notas(self):
        for i in range(len(self.notas)):
            print(f"{self.notas_qtd[i]} notas de {self.notas[i]}")

    def run(self):
        self.valor = int(input("Digite o valor em reais: "))
        self.calcular_notas()
        self.imprimir_notas()
Banco().run()