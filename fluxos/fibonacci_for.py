class Fibonacci:
    def fibonacci():
        n = int(input("Digite o valor de n: "))
        for i in range(n):
            if i == 0:
                fibo = 1
            if i == 1:
                fibo = 1
            if i == 2:
                fibo = 2
            if i > 2:
                fibo = i - 1 + i - 2
            print(f"O {i}º termo da sequência de Fibonacci é {fibo}")
    fibonacci()