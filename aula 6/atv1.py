cont = 0
quant = 1
soma = 0

while cont < 4:
    nota = float(input(f"Digite sua {quant}° nota: "))
    quant += 1
    cont += 1
    soma += nota

media = soma / 4
print(f"Sua média é {media}.")