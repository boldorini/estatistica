import math

def soma(mtx):
    soma = 0
    for num in mtx:
        soma += num
    return soma


def media(mtx):
    media = soma(mtx) / len(mtx)
    return media


def ordena(mtx):
    mtx.sort()
    return mtx


def mediana(mtx):
    matriz = ordena(mtx)
    metade = len(matriz) / 2
    if (len(matriz) % 2 == 0):
        mediana = (matriz[metade - 1] + matriz[metade]) / 2
    else:
        mediana = matriz[metade - 1]
    return mediana


def variancia(mtx):
    soma = 0
    m = media(mtx)
    for num in mtx:
        soma += (m - num) ** 2
    variancia = soma / len(mtx)
    return variancia


def desvioPadrao(mtx):
    desvioPadrao = math.sqrt(variancia(mtx))
    return desvioPadrao


juros = [2.59, 2.64, 2.60, 2.62, 2.57, 2.55, 2.61, 2.5, 2.63, 2.64]
print ('Media: ' + str(media(juros)))
print ('Mediana: ' + str(mediana(juros)))
print ('Variancia: ' + str(variancia(juros)))
print ('Desvio Padrao:' + str(desvioPadrao(juros)))
