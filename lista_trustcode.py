lista = [x for x in range(300)]

n = int(input("Digite um numero aleatorio: "))

if n in lista:
    print(lista.index(n) +1)
else:
    print("Nao existe na lista")
    
