class Fatorial:
    def n_fatorial(self,num):
        if num == 0 or num ==1:
            print("!%s = 1" % num)
            return
            
        fatorial = num
        i = 1
        while i < num:
            fatorial = fatorial * (num-i)
            i+=1
        
        print("!%s = %s " % (num,fatorial))