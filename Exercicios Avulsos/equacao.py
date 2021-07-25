import math
print("Para calcular a equação de 2º grau:")
print("ax² + bx + c = 0, entre com os seguintes valores:")
a = float(input("Entre com o valor de a: "))
b = float(input("Entre com o valor de b: "))
c = float(input("Entre com o valor de c: "))
delta = (b ** 2) - (4 * a * c)

if delta < 0:
     print("Equação NÃO possui raízes reais.")
else:
     raiz = math.sqrt(delta)
     if delta == 0:
         x = (-1)*b / (2 * c) 
         print("a raiz dupla desta equação é", x)
     else:
         x1 = ((-1)*b + raiz) / (2 * c)
         x2 = ((-1)*b - raiz) / (2 * c)
         print("as raízes da equação são", x1, "e", x2)

