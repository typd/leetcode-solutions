# Definition for a binary tree node.
class N(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def maxPathSum(self, r):
        if not r:
            return 0
        self.r = r.val
        self.p_value(r)
        return self.r

    def p_value(self, n):
        if n == None:
            return None
        l = self.p_value(n.left)
        r = self.p_value(n.right)
        now = n.val
        if l:
            now = max(now, l, n.val+l)
        if r:
            now = max(now, r, n.val+r)
        if l and r:
            now = max(now, n.val+l+r)
        self.r=max(self.r, now)
        now = n.val
        if l:
            now = max(now, l+n.val)
        if r:
            now = max(now, r+n.val)
        return now

def test():
    ss = Solution()
    n = N(-10)
    nl = N(9)
    n.left = nl
    nr = N(20)
    n.right = nr
    nrl = N(15)
    nrr = N(7)
    nr.left = nrl
    nr.right = nrr
    #n = N(-4)
    r = ss.maxPathSum(n)
    print(r)


test()
