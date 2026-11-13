IMIN=-2147483648
IMAX=2147483647


def largest_bst(root):
    if root is None:
        return IMAX, IMIN, 0
    if(root.left==None and root.right==None):
        return root.data, root.data,1
    
    left=largest_bst(root.left)
    right=largest_bst(root.right)
    ans=[0,0,0]

    if left[1]<root.data and right[0]>root.data:
        ans[0]=min(left[0], right[0], root.data)
        ans[1]=max(right[1], left[1], root.data)
        ans[2]=1+left[2]+right[2]
        return ans
    
    ans[0]=IMIN
    ans[1]=IMAX
    ans[2]=max(left[2],right[2])
    return ans

def largest_bst_util(root):
    return largest_bst(root)[2]

import sys
sys.setrecursionlimit(10000000)
from collections import deque

class newNode:
    def __init__(self, val):
        self.right=None
        self.data=val
        self.left=None

if __name__=="__main__":
    root=newNode(50)
    root.left=newNode(75)
    root.right=newNode(45)
    root.left.left=newNode(40)

    print("Size of the largest BST is:", largest_bst_util(root))