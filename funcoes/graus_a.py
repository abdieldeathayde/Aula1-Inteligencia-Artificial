import math

graus = float(input("Digite o valor em graus: "))
radianos = math.radians(graus)
seno = math.sin(radianos)
cosseno = math.cos(radianos)
tangente = math.tan(radianos)
print(f"O seno de {graus}° é {seno:.2f}")
print(f"O cosseno de {graus}° é {cosseno:.2f}")
print(f"A tangente de {graus}° é {tangente:.2f}")