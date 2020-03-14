# Definition for singly-linked list.
class Node(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def reverseKGroup(self, head, k):
        if k == 1:
            return head
        pre_head = Node(0)
        pre_head.next = head
        
        new_pre_head, new_head,next_head = self.reverse(pre_head, head,k)

        while next_head != None:
            new_pre_head, new_head,next_head = self.reverse(new_pre_head,next_head,k)
        return pre_head.next

    def reverse(self,pre_head, head,k):
        s = head 
        t = head
        for i in range(k -1):
            if t.next != None:
                t = t.next
            else:
                # finised
                return [None,None,None]
        new_head = t
        next_head = t.next
        print("reverse from", s.val, t.val)

        last = t.next
        s_next = s.next
        new_pre_head = head
        for i in range(k):
            #print("change ", s.val, " -> ", last.val)
            s.next = last
            #prepare for next time
            last = s
            s = s_next
            if s!=None:
                s_next = s.next
            else:
                s_next = None
        pre_head.next = new_head
        return [new_pre_head,new_head,next_head]

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
    n13 = Node(3)
    n14 = Node(4)
    n15 = Node(5)
    n16 = Node(6)
    n17 = Node(7)
    n11.next = n12
    n12.next = n13
    n12.next = None
    n13.next = n14
    n14.next = n15
    n15.next = n16
    n16.next = n17
    show(n11)
    r=ss.reverseKGroup(n11, 2)
    show(r)

test()
