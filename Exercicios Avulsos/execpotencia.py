tx = int(input("Digite a potência máxima: "))
i = 0
while i <= tx:
    print(2 ** i)
    i = i + 1
print("Agora digite valores a serem somados. Finalize digitando 0.")
soma = 0
vlr1 = 1
while vlr1 != 0:
    vlr1 = int(input("Digite o valor: "))
    soma = soma + vlr1
print(f"O valor total da sua soma é:{soma}")

