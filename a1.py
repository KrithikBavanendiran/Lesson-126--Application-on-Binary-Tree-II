class Node:
    def __init__(self, data):
        self.data = data
        self.left=None
        self.right=None

def Node_with_one_child(root):
    if root is None:
        return 0
    else:
        count=0
        if (root.left is None and root.right is not None) or (root.left is not None and root.right is None):
            count+=1
            count+=Node_with_one_child(root.left)
            count+=Node_with_one_child(root.right)
    
    print("Number of nodes with one child:", count)

if __name__ == "__main__":
    root=Node(1)
    root.left=Node(2)
    root.right=Node(3)
    root.left.left=Node(4)
    root.right.right=Node(5)
    Node_with_one_child(root)

    
