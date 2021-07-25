import math
x1 = int(input("1º ponto x: "))
y1 = int(input("1º ponto y: "))
x2 = int(input("2º ponto x: "))
y2 = int(input("2º ponto y: "))
reta = math.sqrt(((x1 - x2)**2) + ((y1 - y2)**2))

if reta >= 10:
    print("longe")
else:
    print("perto")