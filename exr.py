nums = []
numeros_p = int(input("Insira um numero inteiro positivo, ao digitar um valor negativo o programa será encerrado"))

while numeros_p > 0:
    nums.append(numeros_p)
    numeros_p = int(input("Insira outro valor positivo, ao digitar um valor negativo o programa será encerrado"))


print(max(nums), "é o maior valor inserido")
print(min(nums), "é o menor valor inserido")

for i in range(9999999999):
    nums.append(numeros_p)
    numeros_p = int(input("Insira outro valor positivo, ao digitar um valor negativo o programa será encerrado"))

    if i < 0:
        break

print(max(nums), "é o maior valor inserido")
print(min(nums), "é o menor valor inserido")