num = 50
soma = 0

while num <=70:
    soma = soma + num
    print(f"{num} + {soma} = {num + soma}")
    num += 1

for i in range(50, 71):
    soma = i + soma
    print(f"{i} + {soma} = {i + soma}")
    