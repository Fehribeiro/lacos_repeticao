soma = 0
num = 0

while num <= 500:

    soma += num

    print("A soma dos números pares ate 500 é: ", soma)

    num += 2 

for i in range(0, 500):
    if i % 2 == 0:
        soma += i
        print(soma)
    