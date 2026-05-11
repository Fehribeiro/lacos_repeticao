anterior = 0
atual = 1 
prox = 0

contador = 0

while contador != 20:

    prox = atual + anterior

    print(prox)

    anterior = atual
    atual = prox

    contador += 1