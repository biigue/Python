While True:
    entrada = input("")
    entrada=entrada.split()
    contador=0

for x in (entrada):
    resultado=''
    contador+=1
    if contador%2==1:
        var=[]
        var=x.strip().split(' ')
        print (var)
    else:
        numero=[]
        for t in x:
            if t !='\n':
                numero.append(int(t))
                #print (numero)
        for z in range(int(var[1])):
            #print (numero)
            minimo=min(numero)
            numero.remove(minimo)
        for b in numero:
            resultado+=str(b)

        print (resultado +'\n')