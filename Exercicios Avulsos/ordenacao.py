num1 = int(input("1º número: "))
num2 = int(input("2º número: "))
num3 = int(input("3º número: "))
if num1 < num2:
    if num2 < num3:
        print("crescente")
    else:
        print("não está em ordem crescente")
else:
    print("não está em ordem crescente")