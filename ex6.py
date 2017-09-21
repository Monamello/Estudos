n1 = int(input("Digite o um numero: "))
n2 = int(input("Digite outro numero: "))
operacao = input("Qual operaçao realizar: ")


soma = (n1 + n2)
subtracao = (n1 - n2)
multiplicacao= (n1 * n2)
divisao= (n1 + n2)
 
if operacao ==  soma:
    print(n1 + n2)

elif operacao == subtracao:
    print(n1 - n2)

else:
    print(n1 * n2)
