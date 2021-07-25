n = int(input("Digite um número inteiro: "))
teste1 = teste2 = 2
while (not n % teste1 == 0) and teste1 <= 11:
    teste1 += 1
    if teste1 == 11:
        print("primo")
if n % teste2 == 0:
    print("não primo")
