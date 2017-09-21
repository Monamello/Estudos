cigarros_dia = int(input("Quantos cigarros fuma por dia? "))
cigarros_ano = int(input("Quantos anos fumando? "))

minutos_do_dia = (cigarros_dia * 10)
minutos_no_mes = (minutos_do_dia * 30)
minutos_no_ano = (minutos_no_mes * 12)
minutos_ano_fumado = (minutos_no_ano * cigarros_ano)
# O 1440 ajuda a transformar minutos em dias
total_dias_perdidos = (minutos_ano_fumado / 1440) 
print("Total de dias perdidos: {:.2f}".format(
    total_dias_perdidos))
