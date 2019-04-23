def testare_sortare(l, i):
    '''Functia primeste un parametru l, o lista pe care o va sorta, va masura timpul de executie, va memora rezultatul intr-un .txt  
    i = numarul testului'''
    #import datetime
    import os.path
    import time
    import merge_sort_paralel
    import merge_sort_serie

    #v = datetime.datetime.now().strftime('%m-%d %H:%M') #luna-zi ora:minut
    file_name = "Rezultate_"+str(i)+".txt"
    file_exists = os.path.isfile(file_name) 
    
    l_aux=l #pentru l_aux vom testa Sortarea in serie, pentru l vom testa in paralel
    if not file_exists:#daca nu exista creaza-l
        with open (file_name, 'w') as f:
            pass
    else:#daca exista scrie rezultatele
        with open (file_name, 'a') as f:
            f.write("Dimesiune lista: {}\n".format(len(l)) )

            #calculez timpul de executie a sortarii in paralel:
            start = time.time()#timp de start
            merge_sort_paralel.merge_sort_parallel(l)#sorteaza
            end = time.time()#timp de final
            f.write("Sortare in paralel: {}\n".format(str(end-start)))#scriu rezultatul in secunde
            
            #calculez timpul de executie a sortarii in serie:
            start = time.time()
            merge_sort_serie.merge_sort(l_aux)
            end = time.time()
            f.write("Sortare in serie: {}\n".format(str(end-start)))

            f.write("\n")