import time
#Module locale
import merge_sort_paralel
import merge_sort_serie
from generator_liste import generare
from Testing import testare_sortare
if __name__ == '__main__':
    print('Start!')

    #Test random
    i="lista_random"

    l=generare(100)
    testare_sortare(l,i)

    l=generare(1000)
    testare_sortare(l,i)

    l=generare(10000)
    testare_sortare(l,i)

    l=generare(100000)
    testare_sortare(l,i)

    l=generare(1000000)
    testare_sortare(l,i)

    l=generare(2000000)
    testare_sortare(l,i)


    
