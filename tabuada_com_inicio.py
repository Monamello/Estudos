n = int(input("Tabuada: "))
inicio = int(input("Onde começar? "))
fim = int(input("Onde terminar? "))

x = inicio
while x <= fim:
    print(n*x)
    x = x + 1
