soma = 0

for i in range(15):

    numero = int(input("Digite um número inteiro: "))

    fatorial = 1

    for x in range(1, numero + 1):
        fatorial *= x

    soma += fatorial


print("Somatório dos fatoriais:", soma)

contador = 0
soma = 0

while contador < 15:

    numero = int(input("Digite um número inteiro: "))

    fatorial = 1
    auxiliar = 1

    while auxiliar <= numero:

        fatorial *= auxiliar
        auxiliar += 1

    soma += fatorial
    contador += 1


print("Somatório dos fatoriais:", soma)