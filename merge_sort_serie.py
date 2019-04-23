def merge(l1=[], l2=[]):
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
    while l1_index <= len(l1)-1:#exista in l1 elemente necititie  
        f.append(l1[l1_index])
        l1_index+=1

    while l2_index <= len(l2)-1:
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

