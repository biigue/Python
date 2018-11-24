def criarmatriz(valor):
    matriz=[]
    for i in range(valor):
        linha = (valor)*[0]
        matriz.append(linha)
    return matriz


def dijikstra(grafo,vizinhos):
    resultado=[]
    for x in range(len(grafo)):
        distancia=((len(grafo)))*[999999]
        vertice= (len((grafo)))*[0]
        distancia[x]=0
        while 0 in vertice:
            minimo=999999
            for h in range(len(vertice)):
                #if vertice[i]==False:
                if vertice[h] ==0 and distancia[h] < minimo:
                    minimo=distancia[h]
                    posi=h
            vertice[posi]=True
            for q in range(len(distancia)):
                if vertice[q] != 1:
                    if vizinhos[posi][q]== 1:
                        valor1=distancia[posi] + grafo[posi][q]

                        if valor1 < distancia[q]:
                            distancia[q]=valor1
                            #vertice[q]=True
        maximo=maxim(distancia) #alterar pra pegar o max e não o min
        #resultado.append(max(distancia))
        resultado.append(maximo)
    return (resultado)

def maxim(listaa):
    y=0
    for w in (listaa):
        if w>y:
            y=w
    return y

def minemi(listaa):
    y=999999
    for w in (listaa):
        if w<y:
            y=w
    return y

entrada=input().split()
cidades, voos = int(entrada[0]), int(entrada[1])
grafo=criarmatriz(cidades)
vizinhos=criarmatriz(cidades) #se for vizinho = 1
#preenche a matriz com as distancias da entrada
for j in range(voos):
    dado=input().split()
    c1, c2, p = int(dado[0]), int(dado[1]),(dado[2])
    grafo[c1][c2]=int(p)
    grafo[c2][c1]=int(p)
    vizinhos[c1][c2]=1
    vizinhos[c2][c1]=1
maximos=dijikstra(grafo,vizinhos)
minoo=minemi(maximos)
print(minoo)


#pegar o minimo dos maximos /printar
#for f in (maximos):