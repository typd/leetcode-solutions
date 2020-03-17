# Definition for a binary tree node.
class N(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def recoverTree(self, root):
        """
        :type root: TreeNode
        :rtype: None Do not return anything, modify root in-place instead.
        """
        mid=self.to_mid(root)
        p1 = -1
        p2 = -1
        for i in range(len(mid) -1):
            if mid[i] > mid[i+1]:
                if p2==-1:
                    p2 = i
                p1 = i+1
        v1 = mid[p1]
        v2 = mid[p2]
        print("change", v1, v2)
        self.replace(root, v1, v2)

    def replace(self,root,v1,v2):
        #print("checking", root.val, v1, v2)
        #print("  ", (root.val == v1), root.val, v1)
        #print("  ", (root.val == v2), root.val, v2)
        if root.val == v1:
            #print("found", v1)
            root.val = v2
        elif root.val == v2:
            #print("found", v2)
            root.val = v1
        if root.left:
            self.replace(root.left, v1,v2)
        if root.right:
            self.replace(root.right,v1,v2)
        
    def to_mid(self,root):
        if root == None:
            return []
        return self.to_mid(root.left) + [root.val] + self.to_mid(root.right)

def test():
    ss=Solution()
    n = N(3)
    n.left=N(1)
    n.right=N(4)
    n.right.left=N(2)
    print(ss.to_mid(n))
    ss.recoverTree(n)
    print(ss.to_mid(n))

    pass

test()

