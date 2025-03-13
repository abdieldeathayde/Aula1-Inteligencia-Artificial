t = int(input("Digite a quantidade total de segundos: "))
h = t // 3600
m = (t % 3600) // 60
s = (t % 3600) % 60 
print(f"{t} segundos correspondem a {h} horas, {m} minutos e {s} segundos.")