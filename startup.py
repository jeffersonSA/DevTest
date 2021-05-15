from config import Config
from Projeto1.votos import Votos
from Projeto2.sort import Sort
from Projeto3.fatorial import Fatorial
from Projeto4.multiplos import Multiplos
class Startup():
    def __init__(self):
        try:
            while True:
                opcao = int(input('[1] - Rodar programa votos em relação ao total de eleitores\n'+
                '[2] - Rodar programa Bubble Sort\n'+
                '[3] - Rodar programa Fatorial\n'+
                '[4] - Rodar programa soma de multiplos de 3 e 5\n'
                '[5] - Sair [S/n]\n'))

                if opcao == 1:
                    self.projeto1()
                if opcao == 2:
                    self.projeto2()
                if opcao == 3:
                    self.projeto3()
                if opcao == 4:
                    self.projeto4()
                if opcao == 5:
                    break
                elif opcao < 1 and opcao > 5:
                    print('Comando inválido, programa continuará executando...')

    
        except Exception as e:
            print(e)

    def projeto1(self):
        #Projeto 1
        configuration = Config()
        self.general_config_projeto1 = configuration.get_general_config('Projeto1')
            
        #Totais
        total_eleitores = self.general_config_projeto1['total_eleitores']
        votos_validos = self.general_config_projeto1['votos_validos']
        votos_brancos = self.general_config_projeto1['votos_brancos']
        votos_nulos = self.general_config_projeto1['votos_nulos']

        #Calcula percentuais de votos
        votos = Votos(total_eleitores)
        votos.percentual_validos(votos_validos)
        votos.percentual_brancos(votos_brancos)
        votos.percentual_nulos(votos_nulos)

    def projeto2(self):
        sort = Sort()
        vetor = [5,3,2,4,7,1,0,6]
        sort.bubble_sort(vetor)

    def projeto3(self):
        fatorial = Fatorial()
        
        while True:
            numero = input('Digite um número para calcular o fatorial: ')
            
            if numero.isdigit() == False:
                print('Valor digitado não é um número')
                continue

            fatorial.n_fatorial(int(numero))
            parar = input('Gostaria de parar a execução? [S/n] ')

            if parar in ['S', 's', '']:
                break
            elif parar not in ['N', 'n', 'S', 's', '']:
                print('Comando inválido, programa continuará executando...')

    def projeto4(self):
        multiplos = Multiplos()
        while True:
            numero = input('Entre com um número para calculo do multiplos de 3 e 5: ')
            
            if numero.isdigit() == False:
                print('Valor digitado não é um número')
                continue

            multiplos.soma_multiplos(int(numero))
            parar = input('Gostaria de parar a execução? [S/n] ')

            if parar in ['S', 's', '']:
                break
            elif parar not in ['N', 'n', 'S', 's', '']:
                print('Comando inválido, programa continuará executando...')
     
st = Startup()