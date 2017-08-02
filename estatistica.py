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
        print soma([1,2,3])
        #print (self.mtx)
        #s = self.soma(self.mtx)
        #media = soma(self.mtx) / len(self.mtx)
        #return media
        #return s


    def ordena(self):
        self.mtx.sort()
        return self.mtx


    def mediana(self):
        matriz = ordena(self.mtx)
        metade = len(matriz) / 2
        if (len(matriz) % 2 == 0):
            mediana = (matriz[metade - 1] + matriz[metade]) / 2
        else:
            mediana = matriz[metade - 1]
        return mediana


    def variancia(self):
        soma = 0
        m = media(self.mtx)
        for num in self.mtx:
            soma += (m - num) ** 2
        variancia = soma / len(self.mtx)
        return variancia


    def desvioPadrao(self):
        desvioPadrao = sqrt(variancia(self.mtx))
        return desvioPadrao