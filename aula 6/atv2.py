soma = 0
quant = 0

while True:
    num = int(input("Digite um número [negativo para finalizar]: "))
    if num < 0:
        break
    soma += num
    quant += 1
    

media = soma / quant
print(f"A média é {media}")