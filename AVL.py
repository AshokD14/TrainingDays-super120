#AVL tree
class node:
    def _init_(self,data):
        self.value=data
        self.left=None
        self.right=None
        self.height=1

def inorder(root):#print the data in inorder format
    if not root:
        return
    inorder(root.left)
    print(root.value,end=" ")
    inorder(root.right)

def insert(root,Super):
    if not root:
        return node(Super)
    if Super<root.value:
        root.left=insert(root.left,Super)
    else:
        root.right=insert(root.right,Super)
   
    root.height=1+max(ght(root.left),ght(root.right))
    
    BF=getBF(root)
    
    #RR rotation
    if BF>1 and Super < root.left.value:
        return rightRotate(root)
    
    #RL rotation
    if BF>1 and Super > root.left.value:
        root.left=leftRotate(root.left)
        return rightRotate(root)
    
    #LL rotation   
    if BF<-1 and Super>root.right.value:
         return leftRotate(root)
     
    #LR rotation   
    if BF<-1 and Super<root.right.value:
        root.right=rightRotate(root.right)
        return leftRotate(root)
    
    return root

def ght(root):
    if not root:
        return 0
    return root.height

def getBF(root):
    if not root:
        return 0
    return ght(root.left)-ght(root.right)
       
def leftRotate(A):
    B=A.right
    temp=B.left
    B.left=A
    A.right=temp
    
    A.height=1+max(ght(A.left),ght(A.right))
    B.height=1+max(ght(B.left),ght(B.right))
    return B

def rightRotate(A):
    B=A.left
    temp=B.right
    B.right=A
    A.left=temp
    
    A.height=1+max(ght(A.left),ght(A.right))
    B.height=1+max(ght(B.left),ght(B.right))
    return B



if __name__=="main_":
    root=None
    vl=[19,99,75,7,21,34,38,27,134,100,29,0,12,17,143]
    for i in vl:
        root=insert(root,i)
    inorder(root)