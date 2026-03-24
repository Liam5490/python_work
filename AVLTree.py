class TreeNode(object):
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        self.height = 1

class AVLTree(object):

    # Function to insert a node
    def insert_node(self, root, data):
        if not root:
            return TreeNode(data)
        elif data < root.data:
            root.left = self.insert_node(root.left, data)
        else:
            root.right = self.insert_node(root.right, data)

        root.height = 1 + max(self.getHeight(root.left),
                              self.getHeight(root.right))

        balanceFactor = self.getBalance(root)

        # LL
        if balanceFactor > 1 and data < root.left.data:
            return self.rightRotate(root)
        # LR
        if balanceFactor > 1 and data > root.left.data:
            root.left = self.leftRotate(root.left)
            return self.rightRotate(root)
        # RR
        if balanceFactor < -1 and data > root.right.data:
            return self.leftRotate(root)
        # RL
        if balanceFactor < -1 and data < root.right.data:
            root.right = self.rightRotate(root.right)
            return self.leftRotate(root)

        return root

    # Function to delete a node
    def delete_node(self, root, data):
        if not root:
            return root
        elif data < root.data:
            root.left = self.delete_node(root.left, data)
        elif data > root.data:
            root.right = self.delete_node(root.right, data)
        else:
            # node with one child or no child
            if root.left is None:
                temp = root.right
                root = None
                return temp
            elif root.right is None:
                temp = root.left
                root = None
                return temp
            # node with two children: get inorder successor
            temp = self.getMinValueNode(root.right)
            root.data = temp.data
            root.right = self.delete_node(root.right, temp.data)

        if root is None:
            return root

        # update height
        root.height = 1 + max(self.getHeight(root.left),
                              self.getHeight(root.right))

        # rebalance
        balanceFactor = self.getBalance(root)

        # LL
        if balanceFactor > 1 and self.getBalance(root.left) >= 0:
            return self.rightRotate(root)
        # LR
        if balanceFactor > 1 and self.getBalance(root.left) < 0:
            root.left = self.leftRotate(root.left)
            return self.rightRotate(root)
        # RR
        if balanceFactor < -1 and self.getBalance(root.right) <= 0:
            return self.leftRotate(root)
        # RL
        if balanceFactor < -1 and self.getBalance(root.right) > 0:
            root.right = self.rightRotate(root.right)
            return self.leftRotate(root)

        return root

    # Rotations
    def leftRotate(self, z):
        y = z.right
        T2 = y.left

        y.left = z
        z.right = T2

        z.height = 1 + max(self.getHeight(z.left), self.getHeight(z.right))
        y.height = 1 + max(self.getHeight(y.left), self.getHeight(y.right))
        return y

    def rightRotate(self, z):
        y = z.left
        T3 = y.right

        y.right = z
        z.left = T3

        z.height = 1 + max(self.getHeight(z.left), self.getHeight(z.right))
        y.height = 1 + max(self.getHeight(y.left), self.getHeight(y.right))
        return y

    # Helpers
    def getHeight(self, root):
        return 0 if root is None else root.height

    def getBalance(self, root):
        return 0 if root is None else self.getHeight(root.left) - self.getHeight(root.right)

    def getMinValueNode(self, root):
        if root is None or root.left is None:
            return root
        return self.getMinValueNode(root.left)

    def getMaxValueNode(self, root):
        if root is None or root.right is None:
            return root
        return self.getMaxValueNode(root.right)

    def Numberyayornay(self, root, data): #tells you if a number is there in the tree, hence yay or nay
        curr = root
        while curr:
            if data == curr.data:
                return True
            curr = curr.left if data < curr.data else curr.right
        return False

 
    def printPreOrder(self, root):
        if not root:
            return
        print(root.data, end=" ")
        self.printPreOrder(root.left)
        self.printPreOrder(root.right)

    def printInOrder(self, root):
        if not root:
            return
        self.printInOrder(root.left)
        print(root.data, end=" ")
        self.printInOrder(root.right)

    def printHelper(self, currPtr, indent, last):
        if currPtr is not None:
            print(indent, end="")
            if last:
                print("R----", end="")
                indent += "     "
            else:
                print("L----", end="")
                indent += "|    "
            print(f"{currPtr.data} (h={currPtr.height})")
            self.printHelper(currPtr.left, indent, False)
            self.printHelper(currPtr.right, indent, True)


def interactiveAVL():

    tree = AVLTree()
    root = None

    print("Enter positive integers to insert or delete (just enter the same number twice to delete).") #guidelines of what to do 
    print("Enter 0 or a negative to quit.\n")

    while True:
        raw = input("Number: ")

     
        try:
            x = int(raw)
        except ValueError:
            print("Please enter a valid number") #boundary incase the input is incorrect
            continue

     
        if x <= 0:
            print("\nExiting. Final tree:") #final iteration of the tree
            tree.printHelper(root, "", True)
            # Optional: print sorted order to verify BST invariant
            print("\nIn-order:", end=" ")
            tree.printInOrder(root)
            print()
            break

       
        if tree.Numberyayornay(root, x): #if the the number is/isn't there
            print(f"{x} is in the tree. Deleting now") #deletes if it is there
            root = tree.delete_node(root, x)
        else:
            print(f"{x} is not in the tree. Inserting now") #adds if it isn't there
            root = tree.insert_node(root, x)

    
        print("Current AVL tree:") #prints the constant status of the tree
        tree.printHelper(root, "", True)
        print() 


if __name__ == "__main__":
    interactiveAVL()



