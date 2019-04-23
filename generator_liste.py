import random
def generare(n):
    '''Funcția returnează o lista de 'n' numere (intre 0 si 'n'), ordonate la întâmplare'''
    l = []#lista returnată
    for i in range(0, n):
        l.append(i)
    random.shuffle(l)
    return l

def generare_sortate(n):
    '''Functia genereaza o lista de 'n' elemente(de la 0 la n) gata sortata '''
    l=[]
    for i in range(0, n):
        l.append(i)
    return l

def generare_ordine_inversa(n):
    '''Functia genereaza o lista de 'n' elemente(de la n la 0) '''
    l=[]
    for i in range(0, n):
        l.insert(0,i)#insereaza mereu la inceput
    return l