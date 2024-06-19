class node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
    
def preorder(root):
    if root == None:
        return
    print(root.data)
    preorder(root.left)
    preorder(root.right)
    
def inorder(root):
    if root == None:
        return
    print(root.data)
    inorder(root.left)
    inorder(root.right)

def postorder(root):
    if root == None:
        return
    print(root.data)
    postorder(root.left)
    postorder(root.right)

if __name__=="__main__":
    root = node(1)
    root.left = node(2)
    root.right = node(3)
    root.left.left = node(4)
    root.left.right = node(5)
    root.right.right = node(7)
    root.right.left = node(6)
    root.left.right.left = node(9)
    root.left.right.left.left = node(12)
    root.left.right.left.right = node(13)
    root.right.right.right = node(11)
    print("Preorder")
    preorder(root) 
    print("Inorder")
    inorder(root)
    print("Postorder")
    postorder(root)