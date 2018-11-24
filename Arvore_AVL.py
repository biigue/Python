class Galho():
    def __init__(self, chave=None, dado = None):
        self._chave = chave
        self._esquerdo = None
        self._direito = None
        self._pai = None
        self._dado = dado
    def getChave(self):
        return self._chave
    def setChave(self,chave):
        self._chave = chave

    def getEsquerdo(self):
        return self._esquerdo
    def setEsquerdo(self,esquerdo):
        self._esquerdo = esquerdo

    def getDireito(self):
        return self._direito
    def setDireito(self,direito):
        self._direito = direito

    def getPai(self):
        return self._pai
    def setPai(self,pai):
        self._pai = pai

    def getDado(self):
        return self._dado
    def setDado(self, dado):
        self._dado = dado

    def __str__(self):
        return "Chave"+ str(self._chave)+"Dado"+str(self._dado)

class ArvoreBinaria():
    def __init__(self):
        self._raiz = None
    def vazia(self):
        return self._raiz is None
    def getRaiz(self):
        return self._raiz
    def setRaiz(self, valor):
        self._raiz = valor

    def esquerdo(self,chave):
        pai_chave = chave.get_pai()
        if pai_chave==None:
            return False
        if pai_chave.get_esquerdo()==chave:
            return True

    def direito(self, chave):
        pai_chave = chave.get_pai()
        if pai_chave == None:
            return False
        if pai_chave.get_direito() == chave:
            return True

    def inserir(self,chave,dado):
        z = Galho(chave, dado)
        y = None
        raiz = self.getRaiz()
        while raiz!=None:
            y=raiz
            if chave<raiz.getChave():
                raiz = raiz.getEsquerdo()
            else:
                raiz = raiz.getDireito()
        z.setPai(y)
        if y == None:
            self.setRaiz(z)
        else:
            if chave<y.getChave():
                y.setEsquerdo(z)
            else:
                y.setDireito(z)
        self.balancear(z)

    def balancear(self,chave):
        chave=chave
        while chave != None:
            fator_chave = self.fator(chave)
            if fator_chave <=1 and fator_chave >=-1:
                chave= chave.get_pai()
            else:
                pass
    def altura(self,chave):
        if chave == None:
            return -1
        alturaesq=self.altura(chave.get_esquerdo())
        alturadir=self.altura(chave.get_direito())
        if alturaesq > alturadir:
            return alturaesq+1
        return alturadir+1

    def fator(self,chave):
        return self.altura(chave.get_direito())-self.altura(chave.get_esquerdo())

    def rota_esquerda(self,chave):
        chaves = chave.get.direito()
        chaves.set_direito(chaves.get_esquerdo())
        if chaves.get_esquerdo() != None:
            chaves.get_esquerdo().set_pai(chave)
        chaves.set_pai(chaves.get_pai())
        if chave.get_pai() == None:
            self.set_raiz(chaves)
        else:
            if chave == chaves.get_pai().get_esquerdo():
                chave.get_pai().set_esquerdo(chaves)
            else:
                chaves.get_pai().set_direito(chaves)
        chaves.set_esquerdo(chave)
        chave.set_pai(chaves)

    def pesquisar(self,x,chave):
        if x == None or chave == x.getChave():
            return x
        if chave < x.getChave():
            return self.pesquisar(x.getEsquerdo(),chave)
        else:
            return self.pesquisar(x.getDireito(),chave)

    def minimo(self,x):
        while x.getEsquerdo()!=None:
            x = x.getEsquerdo()
        return x

    def maximo(self, x):
        while x.getDireito()!=None:
            x = x.getDireito()
        return x

    def sucessor(self, x):
        if x == None:
            return None
        if x.getDireito()!= None:
            return self.minimo(x.getDireito())
        else:
            y = x.getPai()
            while y!= None and x == y.getDireito():
                x=y
                y=y.getPai()
            return y

    def antessesor(self, x):
        if x == None:
            return None
        if x.getEsquerdo()!= None:
            return self.maximo(x.getEsquerdo())
        else:
            y = x.getPai()
            while y != None and x==y.getEsquerdo():
                x = y
                y = y.getPai()
            return y

    def preOrdem(self,x, lista):
        if x != None:
            lista.append(str(x))
            self.preOrdem(x.getEsquerdo(),lista)
            self.preOrdem(x.getDireito(), lista)

    def emOrdem(self,x, lista):
        if x != None:
            self.emOrdem(x.getEsquerdo(), lista)
            lista.append(str(x))
            self.emOrdem(x.getDireito(),lista)

    def posOrdem(self,x, lista):
        if x != None:
            self.posOrdem(x.getEsquerdo(),lista)
            self.posOrdem(x.getDireito(),lista)
            lista.apend(str(x))

    def deletar(self,z):
        if z.getEsquerdo is None and z.getDireito() is None:
            y = z
        else:
            y = self.sucessor(z)
        if y.getEsquerdo() is not None:
            x = y.getEsquerdo()
        else:
            x = y.getDireito()
        if x is not None:
            x.setPai(y.getPai())
        if y.getPai() is None:
            self.setRaiz(x)
        elif y == y.getPai().getEsquerdo():
            y.getPai().setDireito(x)
        else:
            y.getPai().setDireito(x)
        if y != z:
            z.setChave(y.getChave())
        return y

    def removerprof(self, z):
        if z.getEsquerdo == None or z.getDireito() ==None:
            y = z
        else:
            y = self.sucessor(z)
        if y.getEsquerdo()!= None:
            x = y.getEsquerdo()
        else:
            x=y.getDireito()
        if x != None:
            x.setPai(y.getPai())
        if y.getPai()== None:
            self.setRaiz(x)
        else: #elif
            if y == y.getPai().getEsquerdo():
                y.getDireito().getPai()
            if y != z:
                z.setChave(y.getChave())
        return y

