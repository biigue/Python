def quicksort(v):
  if len(v)<=1:
    return v
  menor,igual,maior=[],[],[]
  pivot=v[0]
  for x in v:
    if x<pivot:
      menor.append(x)
    elif x==pivot:
      igual.append(x)
    else:
      maior.append(x)
  return quicksort(menor)+igual+quicksort(maior)

saida=[]
entrada= input("").split()
p, m = int(entrada[0]), int(entrada[1])
c=0
ganhadores=[]
for j in range(p):
    c-=1
    ganhadores.append([0]*3+[c])

for i in range(m):
    modalidade=input("").split()
    ouro=int(modalidade[0])
    prata=int(modalidade[1])
    bronze=int(modalidade[2])
    ganhadores[ouro-1][0]+=1
    ganhadores[prata-1][1]+=1
    ganhadores[bronze-1][2] += 1
ganhadores = quicksort(ganhadores)
for i in ganhadores:
    saida.append(-(ganhadores[ganhadores.index(i)][3]))
for i in saida[::-1]:
    print(i,end=" ")

