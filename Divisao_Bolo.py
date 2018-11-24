import sys
entrada= open(sys.argv[1],"r")
saida=open(sys.argv[2],"w")
fatias= int(entrada.readline())
quantidade_de_bolos= int(entrada.readline())
bolos= entrada.readline()

bolos=bolos.strip().split()
bolos=[int(i) for i in bolos]
total=sum(bolos)
maior= total//quantidade_de_bolos
for i in range (maior+1, 1, -1):
    x=0
    for j in (bolos):
        y=j//i
        x+=y
    if x==fatias:
        print(i)
        break
    
saida.write(str(i)+"\n") 
entrada.close()
saida.close()
