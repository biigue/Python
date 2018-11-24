import sys
entrada= open(sys.argv[1],"r")
n= int(entrada.readline())
saida=open(sys.argv[2],"w")
lista=entrada.readlines()
matriz=[]
diag1=0
diag2=0
verif="V"

for i in (lista):
    matriz.append(i.strip().split(" "))
    
for x in range(n):
    for y in range(n):
        matriz[x][y]=int(matriz[x][y])
soma=sum(matriz[0])

for x in range(n):
    var=0
    if sum(matriz[x]) != (soma):
        verif="F"
    for y in range(n):
        var+=matriz[x][y]
        if x==y:
            diag1+=matriz[x][y]

        if (x+y+2)==(n+1):
            diag2+=matriz[x][y]

    if var != soma:
            verif="F"
if diag1!=soma:
    verif="F"
if diag2!=soma:
    verif="F"
                
if verif=="F":
    saida.write("-1")
elif verif=="V":
    saida.write(str(soma))
entrada.close()
saida.close()
