class Node():
    def __init__(self,val):
        self.value=val
        self.leftchild=None
        self.rightChild=None
    
    def insert(self, data):
        if self.value==data:
            return False
        elif self.value>data:
            if self.leftchild:
                return self.leftchild.insert(data)
            else:
                self.leftchild=Node(data)
                return True
        else:
            if self.rightChild:
                return self.rightChild.insert(data)
            else:
                 self.rightchild=Node(data)
                 return True
    def find(self, data):
        if self.value==data:
            return True
        elif self.value>data:
            if self.leftchild:
                return self.leftChild.insert(data)
            else:
               return False
        else:
            if self.rightChild:
                return self.rightChild.insert(data)
            else:
                 return False
        
    def preorder(self):
        if self:
            print(str(self.value))
        if self.leftchild:
            self.leftchild.preorder()
        if self.rightChild:
            self.rightChild.preorder()
            
    def postorder(self):
        if self:
            if self.leftchild:
                self.leftchild.postorder()
            if self.rightChild:
                self.rightChild.postorder()
            print(str(self.value))
            
    def inorder(self):
        if self:
            if self.leftchild:
                self.leftchild.inorder()
            print(str(self.value))
            if self.rightChild:
                self.rightChild.inorder()
                
##############################################################################  
class Tree():
    def __init__(self):
        self.root=None
        
    def insert(self, data):
        if self.root:
            return self.root.insert(data)
        else:
            self.root=Node(data)
            return True
    def find(self, data):
        if self.root:
            return self.root.find(data)
        else:
            return False
    def  preorder(self):
        print("PreOrder")
        self.root.preorder()
    def  postorder(self):
        print("PostOrder")
        self.root.postorder()
    def  inorder(self):
        print("InOrder")
        self.root.inorder()
        
        
bst=Tree()
bst.insert(15)
print(bst.insert(10))
print(bst.insert(8))
# print(bst.insert(9))
bst.find(10)
bst.preorder()
bst.postorder()
bst.inorder()
    