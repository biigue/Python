
entrada=input().split(' ')
Nlinha,Ncoluna=int(entrada[0]),int(entrada[1])
matriz=[]

def turnGlobal(x):
    global forPass
   
for i in range(Nlinha):
    linha=input()
    linha = [x for x in linha]
    matriz.append(linha)

  
forPass={}
turnGlobal(forPass)

for i in range(Nlinha) :
    for j in range(Ncoluna):
        pixel=matriz[i][j]
        if pixel != '#':
            forPass[(i,j)]=pixel

def verificarPontinho(pontinho):
    v,k=0,0
    if pontinho in forPass:
        if forPass[pontinho]=='k':
            k+=1
        elif forPass[pontinho]=='v':
            v+=1
        del forPass[pontinho]
        p1,p2=pontinho[0],pontinho[1]
        l,o=verificarPontinho((p1-1,p2))
        v+=l
        k+=o
        l,o=verificarPontinho((p1+1,p2))
        v+=l
        k+=o
        l,o=verificarPontinho((p1,p2-1))
        v+=l
        k+=o
        l,o=verificarPontinho((p1,p2+1))
        v+=l
        k+=o
        return v,k
    else:
        return  v,k

lobosVivos=0
ovelhasVivas=0
    
while len(forPass) != 0  :
    pontinho=[x for x in forPass.keys()][0]
    v,k=verificarPontinho(pontinho)
    if v >= k:
        lobosVivos+=v
    else:
        ovelhasVivas+=k
print(ovelhasVivas, lobosVivos)
        
    
    
    
    


