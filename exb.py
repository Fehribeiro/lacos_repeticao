#pow => expoentes / elevar
#abs => negativo em positivo
#math.sqrt => raiz quadrada
#math.factorial => fatorial
#math.pi => pi
#math.sin => seno

num = int(input("Insira um valor para tabuada"))
mult = 0

while mult < 11:
    print(f"{num} x {mult} = {num*mult}")
    mult += 1

