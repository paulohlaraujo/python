# Programa - Simulação de uma fila
ultimo = 10
fila = list(range(1, ultimo +1))
while True:
    print(f"Existem {len(fila)} clientes na fila")
    print(f"\nFila atual: {fila}")
    print("Digitte F para adicionar um cliente ao final da fila,")
    print("ou A para realizar o atendimento. S para sair.")
    operacao = input("Operação (F, A ou S):")
    if operacao == "A":
        if len(fila) > 0:
            atendido = fila.pop(0)
            print(f"Cliente {atendido} atendido")
        else:
            print("Fila vazia! Ninguém para atender")
    elif operacao == "F":
        ultimo += 1 #incrementa ao final da fila
        fila.append(ultimo)
    elif operacao == "S":
        break
    else:
        print("Operação inválida! Digite apenas A, F ou S.")
    
