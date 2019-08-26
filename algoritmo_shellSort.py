from random import shuffle
from random import randint
import timeit
import matplotlib as mpl
import matplotlib.pyplot as plt
  
  
def desenhaGrafico(x,y, xl = "Entradas", yl = "Saídas"):
    fig = plt.figure(figsize=(10, 8))
    ax = fig.add_subplot(111)
    ax.plot(x,y, label = "Tempo")
    ax.legend(bbox_to_anchor=(1, 1),bbox_transform=plt.gcf().transFigure)
    plt.ylabel(yl)
    plt.xlabel(xl)
    plt.show()


def geraLista(tam):
    
    lista = list(range(1, tam + 1))
    shuffle(lista)
    return lista
    
    
x2 = [100000,200000,300000,400000,500000,1000000,2000000]
y = []


def shellSort(nums):
    h = 1
    n = len(nums)
    while h > 0:
            for i in range(h, n):
                c = nums[i]
                j = i
                while j >= h and c < nums[j - h]:
                    nums[j] = nums[j - h]
                    j = j - h
                    nums[j] = c
            h = int(h / 2.2)
    return nums
    
       
    
for a in range(len(x2)):
 
    array = geraLista(x2[a])
    
    inicio = timeit.default_timer()
    shellSort(array)
    fim = timeit.default_timer()
    
    y.append('%f' %(fim - inicio))

   
    print(y)
 
 
desenhaGrafico(x2,y)
