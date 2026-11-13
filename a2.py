class Node:
    def __init__(self, data):
        self.data=data
        self.left=None
        self.right=None
    
def traverse(root, tilt):
    if root is None:
        return 0
    left_sum= traverse(root.left, tilt)
    right_sum= traverse(root.right, tilt)
    tilt[0]+=abs(left_sum-right_sum)
    return left_sum+right_sum+root.data

def find_tilt(root):
    tilt=[0]
    traverse(root, tilt)
    return tilt[0]

if __name__=="__main__":
    root=Node(1)
    root.left=Node(2)
    root.right=Node(3)
    root.left.left=Node(4)
    root.left.right=Node(5)
    root.right.right=Node(6)
    print("Tilt of the binary tree is:", find_tilt(root))
    