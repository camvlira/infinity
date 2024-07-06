num = int(input("Digite um número para receber seu fatorial: "))

if num < 0:
    print(f"O número {num} é negativo, fatorial não se define para números negativos.")
elif num == 0:
    print(f"O fatorial de {num} é 1.")
else:
    fatorial = 1
    for i in range(1, num +1):
        fatorial = fatorial * i
    print(f"O fatorial de {num} é {fatorial}.")