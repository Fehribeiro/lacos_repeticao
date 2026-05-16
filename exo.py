import math

num = 0

while num <= 10:
    print(num, " fatorial = ", math.factorial(num))
    num += 1

for i in range(1, 11):
    print(f"{i}! = {math.factorial(i)}")