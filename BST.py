class Node:
    def __init__(self,key):
        self.key = key
        self.right = self.left = None

class BST:
    def __init__(self):
        self.root = None

    def insert(self,root,key):
        
        if root is None:
            return Node(key)

        if key > root.key:
            root.right = self.insert(root.right, key)

        if key < root.key:
            root.left = self.insert(root.left, key)
        
        return root
    def inorder(self,root):

        if root:
            self.inorder(root.left)
            print(root.key)
            self.inorder(root.right)

    def preorder(self,root):

        if root:
            print(root.key)
            self.preorder(root.left)
            self.preorder(root.right)

    def postorder(self,root):
        
        if root:
            self.postorder(root.left)
            self.postorder(root.right)
            print(root.key)

if __name__ == "__main__":

    bst = BST()
    root = None
    while True:
        print("Enter 1 to insert ")
        print("Enter 2 to Display inorder ")
        print("Enter 3 to Display preorder ")
        print("Enter 4 to Display postorder ")
        print("Enter 5 to exit ")

        option = int(input("Enter choice :"))

        if option == 1:
            print("Enter keys :")
            result = input()
            keys = result.split()
            for key in keys:
                root = bst.insert(root,key)
        
        if option == 2:
            bst.inorder(root)
        
        if option == 3:
            bst.preorder(root)
        
        if option == 4:
            bst.postorder(root)

        if option == 5:
            break
