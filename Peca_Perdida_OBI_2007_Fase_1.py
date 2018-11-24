npecas = (input(""))
pecas = (input(""))
f = pecas.split()
fint = [int(elem) for elem in f]
lista = []
for i in range (int(npecas)+1):
    lista.append(i)
x = sum(lista)
y = sum(fint)
resultado= x-y
print(resultado)

