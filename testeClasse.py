from estatistica import estatistica
juros = [2.59, 2.64, 2.60, 2.62, 2.57, 2.55, 2.61, 2.5, 2.63, 2.64]
e = estatistica(juros)

print ('Soma: ' + str(e.soma()))
print ('Media: ' + str(e.media()))
print ('Mediana: ' + str(e.mediana()))
print ('Variancia: ' + str(e.variancia()))
print ('Desvio Padrao:' + str(e.desvioPadrao()))
