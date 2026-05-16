dividendo = int(input("Digite o dividendo: "))
divisor = int(input("Digite o divisor: "))

quociente = 0
soma = divisor

while soma <= dividendo:

    quociente += 1
    soma += divisor

print("Resultado inteiro da divisão:", quociente)


dividendo = int(input("Digite o dividendo: "))
divisor = int(input("Digite o divisor: "))

quociente = 0

for i in range(divisor, dividendo + 1, divisor):
    quociente += 1

print("Resultado inteiro da divisão:", quociente)