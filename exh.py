b = int(input(""))
e = int(input(""))
resultado = 1
cont = 0

while e != cont:

    resultado = resultado * b

    cont += 1

print("O resultado é: ", resultado)

for i in range(0, e):
    resultado *= b

print(resultado)