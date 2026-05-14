anterior = 0
atual = 1 
prox = 0

contador = 0

while contador != 15:

    prox = atual + anterior

    print(prox)

    anterior = atual
    atual = prox

    contador += 1

anterior = 0
atual = 1

for contador in range(15):

    prox = atual + anterior

    print(prox)

    anterior = atual
    atual = prox