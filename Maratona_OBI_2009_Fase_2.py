entrada= (raw_input(""))
entrada=entrada.split()
distanciamaxima=int(entrada[1])
entrada2=(raw_input(""))
entrada2= entrada2.split()
x = 0
contador = 1

for i in (entrada2):
    atual=int(i)
    if atual - x > distanciamaxima:
        contador+=1
        break
    else:
        x=atual
if contador>1:
    print('N')
else:
    print ('S')