deposito = int(input("Qual o valor do deposito: "))
taxa = int(input("Qual a taxa de juros: "))

conta = ((deposito * taxa)/100)
conta2 = (conta * 24)

print("Valor por mes: ",conta )

print("Valor por 24 meses: ",conta2)
