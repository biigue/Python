class No():
    def __init__(self, valor = None):
        self._valor = valor
        self._proximo = None
        self._anterior = None

    def setAnterior(self,anterior):
        self._anterior = anterior
    def setValor(self,valor):
        self._valor = valor
    def setProximo(self,proximo):
        self._proximo = proximo

    def getValor(self):
        return self._valor
    def getProximo(self):
        return self._proximo
    def getAnterior(self):
        return self._anterior

class ListaEncadeada():
    def __init__(self):
        self._inicio = None
        self._fim = None
        self._quantidade = 0

    def __str__(self):
        temp=self._inicio
        out= ''
        while temp is not None:
            a = temp.getValor()
            out+= str(a) + ' '
            temp = temp.getProximo()
        return out[:-1]

    def setInicio(self,inicio):
        self._inicio = inicio
    def setFim(self,fim):
        self._fim = fim
    def setQuantidade(self,valor):
        self._quantidade += valor

    def getQuantidade(self):
        return self._quantidade
    def getInicio(self):
        return self._inicio
    def getFim(self):
        return self._fim

    def vazio(self):
        return((self._inicio==None) and (self._fim==None))


    def pesquisar(self,valor):
        x=self._inicio
    #        if x.getValor()==valor:
    #           return
        while (x!=None):
            if x.getValor()==valor:
                return x
            x=x.getProximo()
        return None

    def remover(self,valor):
        aux= self.pesquisar(valor)
        if aux is not None:
            anterior, proximo = aux.getAnterior(), aux.getProximo()
            if anterior is None:
                self._inicio = proximo
                aux.setProximo(None)
            elif proximo is None:
                self.RemoverFim()
            else:
                anterior.setProximo(proximo)
                proximo.setAnterior(anterior)
                aux.setProximo(None)
                aux.setAnterior(None)

    def removerPeloNo(self, aux):
        if aux is not None:
            anterior, proximo = aux.getAnterior(), aux.getProximo()
            if anterior is None:
                self._inicio = proximo
                aux.setProximo(None)
            elif proximo is None:
                self.RemoverFim()
            else:
                anterior.setProximo(proximo)
                proximo.setAnterior(anterior)
                aux.setProximo(None)
                aux.setAnterior(None)

    def inserirInicio(self,valor):
        novono= No(valor)
        if self._inicio == None and self._fim == None:
            self.setInicio(novono)
            self.setFim(novono)
        else:
            novono.setProximo(self._inicio)
            self._inicio.setAnterior(novono)
            self.setInicio(novono)
        self.setQuantidade(1)

    def inserirFim(self, valor):
        novono = No(valor)
        if self._inicio == None:
            self.setInicio(novono)
            self.setFim(novono)
        else:
            novono.setAnterior(self._fim)
            self._fim.setProximo(novono)
            self.setFim(novono)
        self.setQuantidade(1)

    def RemoverFim(self):
        currentNode, currentNodeValue = self._fim, self.getFim()
        anterior, proximo = currentNode.getAnterior(), currentNode.getProximo()
        if currentNode.getAnterior() == None and currentNode.getProximo() == None:
            self._inicio = self._fim = None
        else:
            anterior.setProximo(None)
            self.setFim(anterior)
            currentNode.setAnterior(None) and currentNode.setProximo(None)
        return currentNodeValue

    def removerInicio(self):
        currentNode, currentNodeValue = self._inicio, self.getInicio()
        anterior, proximo = currentNode.getAnterior(), currentNode.getProximo()
        if currentNode.getAnterior() == None and currentNode.getProximo() == None:
            self._inicio = self._fim = None
        else:
            proximo.setAnterior(None)
            self.setInicio(proximo)
            currentNode.setAnterior(None) and currentNode.setProximo(None)
        return currentNodeValue

class Fila(ListaEncadeada):
    def entrada(self, valor):
        self.inserirFim(valor)
    def saida(self):
        valor = self.removerInicio()
        return valor.getValor()

festas=int(input(""))

for i in range((festas)-1):
    mesa=input("").split()
    mesinha=Fila()
    mesinha.entrada(mesa)
    gamers= Fila()
    while True:
        try:
            pessoas=input().split()
            if pessoas[0] == '-1':
                juvenal=0
                listas = gamers.getQuantidade()
                for j in range(1000):
                    b=mesinha.saida()
                    for k in range(listas):
                        a=gamers.saida()
                        if a[0] == b[0]:
                            del(a[0])
                            gamers.entrada(a)
                            if len(a) == 0:
                                print(k + 1)
                                juvenal = 1
                                break
                        else:
                            g = a[0]
                            del (a[0])
                            a.append(g)
                            gamers.entrada(a)
                    x=b[0]
                    del(b[0])
                    b.append(x)
                    mesinha.entrada(b)
                if juvenal == 0:
                    print('0')
                    break
            else:
                gamers.entrada(pessoas)
        except:
            break

