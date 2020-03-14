class Solution(object):
    def trap(self, a):
        total = 0
        left_max = [0] * len(a)
        right_max = [0] * len(a)
        for i in range(len(a)):
            if i==0:
                left_max[i]=a[i]
            else:
                left_max[i] = max(left_max[i-1], a[i])
        order = list(range(len(a)))
        order.reverse()
        for i in order:
            if i==len(a)-1:
                right_max[i] = a[i]
            else:
                right_max[i]=max(right_max[i+1],a[i]) 
        for i in range(len(a)):
            if i>0:
                max_left = left_max[i-1]
            else:
                max_left = 0
            if i<len(a)-1:
                max_right = right_max[i+1]
            else:
                max_right = 0
            h = min(max_left,max_right)
            w = max(0,h-a[i])
            total += w
        return total

def test():
    s=Solution()
    a=[0,1,0,2]
    a=[0,2,0,1]
    a=[3,2,1,2,1]
    a=[0,1,0,2,1,0,1,3]
    a=[0,1,0,2,1,0,1,3,2,1,2,1]
    a=[4,2,0,3,2,5]
    print(a)
    r=s.trap(a)
    print(r)

test()
