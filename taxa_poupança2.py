deposito = int(input("Qual o valor do deposito: "))
taxa = int(input("Qual a taxa de juros: "))
mensal = int(input("Qual o valor depositado por mesalmente: "))
q_meses = int(input("Quantos meses de deposito mensal: "))


mes_1 = ((deposito * taxa)/100)

mes_24 = (mes_1 * 24)

mensal_conta = ((mensal * taxa)/100)

mensal_conta = mensal_conta * q_meses



print("Valor rendimento por mes do deposito: ", mes_1)

print("Valor por 24 meses do deposito atual: ",mes_24)

print("Valor de rendimento para os meses apontados: ", mensal_conta)
