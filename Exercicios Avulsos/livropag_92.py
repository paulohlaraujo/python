# Programa Livro Página 92
valor = int(input("Digite um valor: "))
cedulas = 0
notas = 50
apagar = valor
while True:
    if notas <= apagar:
        apagar -= notas
        cedulas += 1
    else:
        print(f"{cedulas} cédula(s) de R${notas}")
        if apagar == 0:
            break
        if apagar < 50 and apagar >= 20:
            notas = 20
        elif apagar < 20 and apagar >= 10:
            notas = 10
        elif apagar < 10 and apagar >= 5:
            notas = 5
        elif apagar < 5 and apagar >= 1:
            notas = 1
        cedulas = 0
