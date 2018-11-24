class No_Tree:
    def __init__(self,key):
        self.key=key
        self.left=None
        self.right=None
        self.father=None

    def get_father(self):
        return self.father

    def set_father(self, value):
        self.father = value

    def get_key(self):
        return self.key

    def get_left(self):
        return self.left

    def get_right(self):
        return self.right

    def set_key(self, value):
        self.key = value

    def set_left(self, value):
        self.left = value

    def set_right(self, value):
        self.right = value

class AVLTree():
    def __init__(self):
        self.root=None

    def get_root(self):
        return self.root

    def set_root(self, value):
        self.root = value

    def is_left(self,key):
        father_key=key.get_father()
        if father_key==None:
            return False
        if father_key.get_left()==key:
            return True

    def is_right(self,key):
        father_key=key.get_father()
        if father_key==None:
            return False
        if father_key.get_right()==key:
            return True

    def search(self,root, key):
        if (root== None) or (root.get_key() == key):
            return root
        if key < root.get_key():
            return self.search(root.get_left(), key)
        else:
            return self.search(root.get_right(), key)

    def min(self, key):
        if key.get_left() == None:
            return key
        else:
            return self.min(key.get_left())

    def max(self,key):
        if key.get_right() == None:
            return key
        else:
            return self.max(key.get_right())

    def sucessor(self,key_):
        if self.get_root()==None:
            return None
        if key_!=self.get_root().get_key():
            key=self.search(self.get_root(), key_)
        else:
            key=self.get_root()
        if key.get_right()!= None:
            right_son = key.get_right()
            return self.min(right_son)
        local_key = key.get_father()
        while local_key != None and key is local_key.get_right():
            key = local_key
            local_key = local_key.get_father()
        return local_key

    def predecessor(self,key_):
        if self.get_root()==None:
            return None
        if key_!=self.get_root().get_key():
            key=self.search(self.get_root(), key_)
        else:
            key=self.get_root()
        if key.get_left() != None:
            left_son = key.get_left()
            return self.max(left_son)
        local_key = key.get_father()
        while local_key != None and key == local_key.get_left():
            key = local_key
            local_key = local_key.get_father()
        return local_key

    def insert(self,key):
        No = No_Tree(key)
        local_key = None
        root = self.get_root()
        while root != None:
            local_key = root
            if No.get_key() < root.get_key():
                root = root.get_left()
            else:
                root = root.get_right()
        No.set_father(local_key)
        if local_key == None:
            self.set_root(No)
        else:
            if No.get_key() < local_key.get_key():
                local_key.set_left(No)
            else:
                local_key.set_right(No)
        self.balance(No)

    def remove(self,key_):
        if key_!=self.get_root().get_key():
            key=self.search(self.get_root(),key_)
        else:
            key=self.get_root()
        if key.get_right()==None or key.get_left()==None:
            local_key=key
        else:
            local_key=self.sucessor(key.get_key())
        if local_key.get_left() != None:
            other_local_key=local_key.get_left()
        else:
            other_local_key=local_key.get_right()
        if other_local_key != None:
            other_local_key.set_father(local_key.get_father())
        if local_key.get_father() == None:
            self.set_root(other_local_key)
            self.balance(self.get_root())
        else:
            if self.is_left(local_key):
                local_key.get_father().set_left(other_local_key)
                self.balance(local_key)
            else:
                local_key.get_father().set_right(other_local_key)
                self.balance(local_key)
        if local_key != key:
            key.set_key(local_key.get_key())
            self.balance(key.get_father())

    def inOrdem(self,key,lista):
        lista=[]
        if key != None:
            self.inOrdem(key.get_left())
            lista.append(key.get_key())
            self.inOrdem(key.get_right())

    def posOrdem(self,key):
        if key != None:
            self.posOrdem(key.get_left())
            self.posOrdem(key.get_right())
            print(str(key.get_key())+' ')

    def preOrdem(self,key):
        if key != None:
            print(str(key.get_key())+' ')
            self.preOrdem(key.get_left())
            self.preOrdem(key.get_right())

    def Ordem(self, key, lista):
        if key != None:
            self.Ordem(key.get_left(), lista)
            lista.append(int(key.get_key()))
            self.Ordem(key.get_right(), lista)

    def height(self,key):
        if key==None:
            return -1
        hleft=self.height(key.get_left())
        hright=self.height(key.get_right())
        if hleft > hright:
            return hleft+1
        return hright+1

    def Nivel(self,num):
        temporario=self.get_root()
        nivel=1
        while True:
            if temporario==None:
                nivel=-1
                break
            elif temporario.get_key()==num:
                break
            if (num<temporario.get_key()):
                temporario=temporario.get_left()
            else:
                temporario=temporario.get_right()
            nivel+=1
        return nivel


    def factor(self,key):
        return self.height(key.get_right())-self.height(key.get_left())

    def rotation_left(self,key):
        local_key=key.get_right()
        key.set_right(local_key.get_left())
        if local_key.get_left()!=None:
            local_key.get_left().set_father(key)
        local_key.set_father(key.get_father())
        if key.get_father()==None:
            self.set_root(local_key)
        else:
            if key == key.get_father().get_left():
                key.get_father().set_left(local_key)
            else:
                key.get_father().set_right(local_key)
        local_key.set_left(key)
        key.set_father(local_key)

    def rotation_right(self,key):
        local_key=key.get_left()
        key.set_left(local_key.get_right())
        if local_key.get_right()!=None:
            local_key.get_right().set_father(key)
        local_key.set_father(key.get_father())
        if key.get_father()==None:
            self.set_root(local_key)
        else:
            if key == key.get_father().get_left():
                key.get_father().set_left(local_key)
            else:
                key.get_father().set_right(local_key)
        local_key.set_right(key)
        key.set_father(local_key)

    def double_rotation_left(self,key):
        local_key=key.get_right()
        self.rotation_right(local_key)
        self.rotation_left(key)

    def double_rotation_right(self,key):
        local_key=key.get_left()
        self.rotation_left(local_key)
        self.rotation_right(key)

    def balance(self,key):
        local_key=key
        while local_key!=None:
            factor_of_key=self.factor(local_key)
            if factor_of_key<=1 and factor_of_key>=-1:
                local_key=local_key.get_father()
            else:
                left_son=local_key.get_left()
                righgt_son=local_key.get_right()
                if factor_of_key >1:
                    if self.factor(righgt_son) < 0:
                        self.double_rotation_left(local_key)
                    else:
                        self.rotation_left(local_key)
                elif factor_of_key < -1:
                    if self.factor(left_son) > 0:
                        self.double_rotation_right(local_key)
                    else:
                        self.rotation_right(local_key)
        pass

arvore=AVLTree()
f=0
casos=input().split()
casos=int(casos[0])
while f!=casos:
    entrada=input().split()
    if entrada[0]=="I":
        arvore.insert(int(entrada[1]))
    if entrada[0] == "N":
        x = int(entrada[1])
        h = arvore.Nivel(x)
        print(h)
    if entrada[0] == "L":
        temp = ""
        a = int(entrada[1])
        b = int(entrada[2])
        listatemp = []
        arvore.Ordem(arvore.get_root(), listatemp)
        tamanho = len(listatemp)
        for k in range(tamanho):
            if listatemp[k] >= a and listatemp[k] <= b:
                temp += str(listatemp[k]) + " "
        print(temp)

    if entrada[0]=="F":
        arvore=AVLTree()
        f+=1
        if f == casos:
            break
        else:
            print("")