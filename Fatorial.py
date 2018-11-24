entrada = int(input(""))
contador=0
anterior = 0
fat = 1

def fatorial(n):
    if n <= 1:
        return 1
    if n > 1:
        return fatorial(n - 1) * n

while True:
    f=fatorial(fat)
    if f < entrada:
        fat+=1
        anterior=0
        anterior+=f
    if f > entrada:
        contador+=1
        fat=1
        entrada-=anterior
        if entrada <=0:
            break
    if f == entrada:
        contador+=1
        break
print (contador)