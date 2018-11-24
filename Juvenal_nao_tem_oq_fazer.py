ncasos = int(input(""))
maior=0
for i in range(ncasos):
    x=input("")
    x=x.split()
    a=int(x[0])
    b=int(x[1])
    for z in range(a,b+1):
        contador=1
        while z!=1:
            if z%2==0:
                z=z/2
                contador+=1
            elif z%2!=0:
                z=(3*z)+1
                contador+=1
            if maior < contador:
                maior=contador
    caso=str(i+1)
    print ("Caso "+caso+": "+str(maior))
    maior=0