class node:
    def __init__(self,data):
        self.value=data
        self.left=None
        self.right=None
def height(root):
    if root == None:
        return 0
    lh=height(root.left)
    rh=height(root.right)
    return max(lh,rh)+1
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
print(height(root))