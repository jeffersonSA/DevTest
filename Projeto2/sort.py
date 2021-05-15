class Sort:
    
    def bubble_sort(self,vetor):
        tamanho_vetor = len(vetor)-1
        ordenado = True

        while ordenado:
            ordenado = False
            
            for i in range(tamanho_vetor):
                if vetor[i] > vetor[i+1]:
                    vetor[i], vetor[i+1] = vetor[i+1], vetor[i]
                    ordenado = True
            print(str(vetor))