class Multiplos:
    def soma_multiplos(self, num_x):
        '''Multiplos de 3 e 5'''
        n1 = 3
        n2 = 5
        soma = 0
        i =1
        while i < num_x:
            if i % n1 == 0 or i % n2 == 0:
                soma += i
            i+=1
        print("A Soma dos multimos de 3 e 5 menor que %s é = %s " %(num_x,soma))

