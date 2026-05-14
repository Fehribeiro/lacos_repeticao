soma = 0
num = 1

while num <= 64:

    soma += num 
    print (f"A soma dos grãos de trigo no tabuleiro de xadrez atualmente é: \n {num}ª posição, com {soma} grãos")
    
    num += 1 
    
for i in range(1, 65):
    print (f"A soma dos grãos de trigo no tabuleiro de xadrez atualmente é: \n {num}ª posição, com {soma} grãos")
    soma += i
    num += 1