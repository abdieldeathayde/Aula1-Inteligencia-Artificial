import numpy as np

graus = float(input("Digite o valor em graus: "))
np.deg2rad(graus)
seno = np.sin(graus)
cosseno = np.cos(graus)
tangente = np.tan(graus)
print(f"O seno de {graus}° é {seno:.2f}")
print(f"O cosseno de {graus}° é {cosseno:.2f}")
print(f"A tangente de {graus}° é {tangente:.2f}")