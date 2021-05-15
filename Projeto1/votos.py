class Votos:

    def __init__(self, total_eleitores):
        self.total_eleitores = total_eleitores

    def percentual_validos(self, votos_validos):
        percentual = (votos_validos/self.total_eleitores)*100
        print('Percentual de votos válidos em relação ao total de eleitores é: %s%%' %percentual)
    
    def percentual_brancos(self, votos_brancos):
        percentual = (votos_brancos/self.total_eleitores)*100
        print('Percentual de votos em branco em relação ao total de eleitores é: %s%%' %percentual)

    def percentual_nulos(self, votos_nulos):
        percentual = (votos_nulos/self.total_eleitores)*100
        print('Percentual de votos nulos em relação ao total de eleitores é: %s%%' %percentual)
        