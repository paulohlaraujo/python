def maximo(x, y):
    if x == y:
        return print("Os números são iguais")
    elif x > y:
        return print(f"O maior número é {x}")
    else:
        return print(f"O maior número é {y}")

x = int(input("Digite o 1º número: "))
y = int(input("Digite o 2º número: "))

print(maximo(x, y))
