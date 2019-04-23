#Implementarea se bazeaza pe solutia propusa de Skiena -> adaptat pentru python 
import multiprocessing
import math

def merge(l1, l2):
    '''Functia 'imbina' cele doua liste prin sortate'''
    f=[]#lista sortata returnata
    l1_index=0;#index de iterare in lista l1
    l2_index=0;#index de iterare in lista l2

    #compar 1 -la- 1 elementele din liste si memorez pe cel mai mic
    while l1_index<len(l1) and l2_index<len(l2):
        if l1[l1_index] < l2[l2_index]:
            f.append(l1[l1_index])
            l1_index+=1#incrementez iteratorul
        else: # l1[l1_index] > l2[l2_index]
            f.append(l2[l2_index])
            l2_index+=1
    #memorez eventualele elemente nememorate:
    while l1_index <= (len(l1)-1):#exista in l1 elemente necititie  print("".format()) 
        f.append(l1[l1_index])
        l1_index+=1

    while l2_index <= (len(l2)-1):
        f.append(l2[l2_index])
        l2_index+=1
    return f


def merge_sort(l):
    '''Functia  se bazazea pe algoritmul lui John von Neumann 
    1)Divide lista in subliste de dimensiune 1
    2)Apleleaza merge() pentru a le imbina intr-o lista sortata'''
    if len(l)<=1:
        return l

    l_stanga = merge_sort(l[:len(l)//2])#l_stanga = l[0...mijloc]
    l_dreapta = merge_sort(l[len(l)//2:])#l_dreapta = l[mijloc...final]
    return merge(l_stanga, l_dreapta)#imbina listele

def mergeWrap(A_B):
    '''Functia este corecta doar in contextul pool.map(), data fiind natura functiei map() a obiectului Pool'''
    a,b = A_B #imparte un iterabil de forma [(1),(2)] in doua entitati: a=(1) si b=(2)
    return merge(a,b) #retruneaza lista 'imbinata': [(1)(2)]

def merge_sort_parallel(l):
    '''Creeaza un pool de procese, egal cu nr. de nuclee
    Separa lista in partitii, de marimi egale, pentru fiecare worker\proces din pool, 
    apoi executa un merge_sort pentru fiecare partitie
    La final se 'imbina' partitiile astefel sortate'''

    np=multiprocessing.cpu_count()#np =  numarul de procesoare/nuclee 
    size = int(math.ceil(float(len(l)) / np )) # dimensiunea fiecarei partitii aproximate superior
    l_partitii=[l[i * size:(i + 1) * size] for i in range(np)]#impartirea in partitii a listei l

    pool = multiprocessing.Pool(processes=np) #creem un obiect pool de fire de executie
    l_partitii = pool.map(merge_sort, l_partitii)#sortam prin fiecare partitie 
   #trebuie sa imbinam partitiile obtinute  
    while len(l_partitii) > 1:
        pereche = [(l_partitii[i], l_partitii[i+1]) for i in range(0, len(l_partitii), 2)]#formez perechi de cate 2 partitii
        l_partitii = pool.map(mergeWrap, pereche)
    return l_partitii[0]#l_partitii = [ [unica partitie] ], deci voi returna [0]

  
