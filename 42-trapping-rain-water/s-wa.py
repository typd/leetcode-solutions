class Solution(object):
    def trap(self, a):
        total = 0
        for i in range(len(a)):
            cur = 0
            h = a[i]
            b_h = 0
            order = list(range(i))
            order.reverse()
            for j in order:
                j_h = a[j]
                if j_h <h:
                    if j_h>b_h:
                        temp_cur = 0
                        for k in range(j+1, i):
                            temp_cur += j_h - a[k]
                            a[k] = j_h
                        total += temp_cur
                        cur -= temp_cur
                        b_h=j_h
                    cur += h-b_h
                else:
                    total += cur
                    for k in range(j+1, i):
                        a[k] = h
                    cur = 0
                    break
        return total

def test():
    s=Solution()
    a=[0,1,0,2,1,0,1,3]
    a=[0,1,0,2]
    a=[0,2,0,1]
    a=[0,1,0,2,1,0,1,3,2,1,2,1]
    a=[3,2,1,2,1]
    a=[0,1,0,2,1,0,1,3,2,1,2,1]
    a=[4,2,0,3,2,5]
    print(a)
    r=s.trap(a)
    print(r)

test()
