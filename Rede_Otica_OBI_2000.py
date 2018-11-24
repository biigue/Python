class grafo:
    def __init__(self,vert):
        self.V= vert
        self.grafo = []

    def inserir(self,u,v,w):
        self.grafo.append([u,v,w])

    def find(self, parent, i):
        if parent[i] == i:
            return i
        return self.find(parent, parent[i])

    def union(self, parent, rank, x, y):
        xraiz = self.find(parent, x)
        yraiz = self.find(parent, y)
        if rank[xraiz] < rank[y]:
            parent[xraiz] = yraiz
        elif rank[xraiz] > rank[yraiz]:
            parent[yraiz] = xraiz
        else :
            parent[yraiz] = xraiz
            rank[xraiz] += 1

    def kruskal(self):
        result =[]
        i = 0
        e = 0
        self.grafo=ord_edges(self.grafo)
        parent = []
        rank = []

        for node in range(self.V):
            parent.append(node)
            rank.append(0)

        while e < self.V -1 :
            u,v,w =  self.grafo[i]
            i = i + 1
            x = self.find(parent, u)
            y = self.find(parent, v)

            if x != y:
                e = e + 1
                if u<v:
                    result.append([u, v])
                    self.union(parent, rank, x, y)
                else:
                    result.append([v, u])
                    self.union(parent, rank, x, y)
        ordenado=bubble(result)
        for u,v in ordenado:
            print ("%d %d" % (u+1,v+1))
#        print("")

def bubble(list):
    for j in range(len(list)-1,0,-1):
        for i in range (j):
            if list[i][0] > list[i+1][0]:
                x=list[i]
                list[i] = list[i+1]
                list[i+1] = x
            elif list[i][0] == list[i+1][0]:
                if list[i][1] >list[i+1][1]:
                    x=list[i]
                    list[i]=list[i+1]
                    list[i+1]=x
    return list


def ord_edges(edges):
    smaller = []
    greater = []
    if not edges:
        return []
    pivot = edges.pop(0)
    for (x, y, z) in edges:
        if z <= pivot[2]:
            smaller.append((x, y, z))
        else:
            greater.append((x, y, z))
    smaller = ord_edges(smaller)
    greater = ord_edges(greater)
    return smaller + [pivot] + greater

teste = 1
while True:
    entrada=input()
    if entrada =="0 0":
        break
    else:
        entrada = entrada.split()
        tabas, ramos = int(entrada[0]), int(entrada[1])
        g=grafo(tabas)
        for i in range(ramos):
            rede = input().split()
            g.inserir(int(rede[0])-1,int(rede[1])-1,int(rede[2]))
        if teste==1:
            pass
        else:
            print("")
        print("Teste " + str(teste))
        teste+=1
        g.kruskal()