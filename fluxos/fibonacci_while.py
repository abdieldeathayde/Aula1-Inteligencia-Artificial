class Fibonacci:
    def fibonacci():
        n = int(input("Digite o valor de n: "))
        while (n > -1):
            if n == 0:
                fibo = 1
            if n == 1:
                fibo = 1
            if n == 2:
                fibo = 2
            if n > 2:
                
                fibo = n - 1 + n - 2
                print(f"O {n}º termo da sequência de Fibonacci é {fibo}")
                n = int(input("Digite o valor de n: "))
    fibonacci()