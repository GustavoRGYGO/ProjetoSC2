import random

def gerador_primo():
    while(True):
        p =  random.getrandbits(1024)
        if(p%2==0 or p%3==0 or p%5==0):   #testa com primos pequenos para adiantar verificações
            continue
        if miller(p):
            break
    while(True):
        q =  random.getrandbits(1024)
        if(p%2==0 or p%3==0 or p%5==0):
            continue

        if miller(q):
            break
    return (p,q)


def miller(n):
    s= 0
    d= n - 1
    while (d & 1  == 0):
       s += 1  #conta quantas vezes dividiu
       d = d >> 1
    for j in range(6):
       a =  random.randint(2, n-2)   #O randint é inclusivo nas duas pontas
       x = pow(a,d,n)
       if x==1 or x==n-1:   # primeira checagem
        continue

       for i in range(s):
          x  = pow(x,2,n)
          if x == -1 or x == n-1:
             break  # segue o teste
       else:
        return False # composto, chegou no fim do loop de checagem

    return True    #passou todas as iterações
print(gerador_primo())

