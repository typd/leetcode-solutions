# Definition for singly-linked list.
class Node(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def mergeKLists(self, lists):
        all = []
        for l in lists:
            while l != None:
                all.append(l.val)
                l = l.next
        # sort all
        quick_sort(all, 0, len(all)-1)
        start = None
        last = None
        for i in all:
            n = Node(i)
            if start == None:
                start = n
            if last != None:
                last.next = n
            last = n
        return start

def quick_sort(array, start, end):
    if start >= end:
        return
    p = partition(array, start, end)
    quick_sort(array, start, p-1)
    quick_sort(array, p+1, end)

def partition(array, start, end):
    pivot = array[start]
    low = start + 1
    high = end
    while True:
        # If the current value we're looking at is larger than the pivot
        # it's in the right place (right side of pivot) and we can move left,
        # to the next element.
        # We also need to make sure we haven't surpassed the low pointer, since that
        # indicates we have already moved all the elements to their correct side of the pivot
        while low <= high and array[high] >= pivot:
            high = high - 1
        # Opposite process of the one above
        while low <= high and array[low] <= pivot:
            low = low + 1
        # We either found a value for both high and low that is out of order
        # or low is higher than high, in which case we exit the loop
        if low <= high:
            array[low], array[high] = array[high], array[low]
            # The loop continues
        else:
            # We exit out of the loop
            break
    array[start], array[high] = array[high], array[start]
    return high

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


