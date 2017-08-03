from math import sqrt

class estatistica(object):

    def __init__(self, mtx):
        self.mtx = mtx


    def soma(self):
        soma = 0
        for num in self.mtx:
            soma += num
        return soma


    def media(self):
        s = self.soma()
        media = s / len(self.mtx)
        return media
        
        
    def ordena(self):
        self.mtx.sort()
        return self.mtx


    def mediana(self):
        matriz = self.ordena()
        metade = len(matriz) / 2
        if (len(matriz) % 2 == 0):
            mediana = (matriz[metade - 1] + matriz[metade]) / 2
        else:
            mediana = matriz[metade - 1]
        return mediana


    def variancia(self):
        soma = 0
        m = self.media()
        for num in self.mtx:
            soma += (m - num) ** 2
        variancia = soma / len(self.mtx)
        return variancia


    def desvioPadrao(self):
        desvioPadrao = sqrt(self.variancia())
        return desvioPadrao