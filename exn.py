contador = 0
numero = 0

while numero >= 0:

    numero = int(input("Digite um valor: "))

    if numero >= 0:
        soma += numero
        contador += 1

if contador > 0:
    media = soma / contador
    print("Somatório:", soma)
    print("Média:", media)
    print("Total de valores lidos:", contador)

else:
    print("Nenhum valor positivo foi digitado.")


soma = 0
contador = 0

for i in range(999999):

    numero = int(input("Digite um valor: "))

    if numero < 0:
        break

    soma += numero
    contador += 1


if contador > 0:

    media = soma / contador

    print("Somatório:", soma)
    print("Média:", media)
    print("Total de valores lidos:", contador)

else:
    print("Nenhum valor positivo foi digitado.")

