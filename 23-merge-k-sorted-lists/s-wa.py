# Definition for singly-linked list.
class Node(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def mergeKLists(self, lists):
        # find start node
        pendings = []
        start = None
        for list in lists:
            show(list)
            if list != None and (start == None or list.val < start.val):
                start = list
        for n in lists:
            if n != start and n != None:
                pendings.append(n)
            else:
                if n!=None and n.next != None:
                    pendings.append(n.next)
        p=start
        while len(pendings)>0:
            next = None
            for n in pendings:
                if n==None:
                    continue
                if next==None or next.val > n.val:
                    next = n
            p.next = next    
            p=p.next
            next_pendings = []
            for n in pendings:
                if n!=next:
                    next_pendings.append(n)
                else:
                    if n.next != None:
                        next_pendings.append(n.next)
            pendings = next_pendings
        return start

def show(n):
    s = ""
    while n != None:
        s += str(n.val) + "->"
        n = n.next
    print(s)

def test():
    ss = Solution()
    n11 = Node(1)
    n12 = Node(2)
    n11.next = n12
    n21 = Node(1)
    n22 = Node(3)
    n21.next = n22
    r=ss.mergeKLists([n11,n21,None])
    show(r)

test()


