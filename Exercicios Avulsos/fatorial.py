n = int(input("Digite o valor de n: "))
fatorial = n
while True:
    if n == 1 or n == 0:
        break
    fatorial = fatorial * (n - 1)
    n -= 1
if n == 0:
    fatorial = 1
print(fatorial)
