num = int(input("Número inteiro: "))
teste3 = num % 3
teste5 = num % 5
if teste3 == 0 and teste5 == 0:
    print("FizzBuzz")
else:
    print(num)
