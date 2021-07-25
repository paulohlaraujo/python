num = input("Digite um número inteiro: ")
tam = len(str(num))
posicao = 0
soma = 0
while posicao < tam:
    parte = int(num[posicao])
    soma = soma + parte
    posicao = posicao + 1
print(soma)
