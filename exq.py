comodo = []
novo_comodo = 1
soma = 0


while novo_comodo == 1:

    comodo.append(input("Insira o nome do comodo"))
    print(comodo)

    largura = float(input("Insira a LARGURA do comodo: "))
    comprimento = float(input("Insira o COMPRIMENTO do comodo: "))

    area = largura * comprimento
    print(f"Area do comodo: {area}")
    
    soma = soma + area

    novo_comodo = int(input("Deseja adicionar um novo comodo? (Não = 0 / Sim = 1)"))

print(f"A area total dos comodos: \n {comodo} \n Área: {soma}")
    

for i in range(999999999):
    comodo.append(input("Insira o nome do comodo"))
    print(comodo)
    
    largura = float(input("Insira a LARGURA do comodo: "))
    comprimento = float(input("Insira o COMPRIMENTO do comodo: "))

    area = largura * comprimento
    print(f"Area do comodo: {area}")

    soma += area
    novo_comodo = int(input("Deseja adicionar um novo comodo? (Não = 0 / Sim = 1)"))

    if novo_comodo != 1:
        break

print(comodo)
print("Area total = ", soma)
