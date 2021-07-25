num = input("Digite um número inteiro: ")
tam = len(str(num))
tam = tam - 1
posicao = 0
numanterior = int(num[posicao])
check = False
while posicao < tam:
    numposterior = int(num[posicao + 1])
    if numposterior == numanterior:
        print(f"Os números {numanterior} e {numposterior} são sequenciais.")
        check = True
        break
    else:
        numanterior = numposterior
        posicao = posicao + 1
if not check:
    print(f"A sequencia não tem números duplos.")
