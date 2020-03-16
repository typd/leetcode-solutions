class Solution(object):
    def largestRectangleArea(self, hs):
        l = len(hs)
        if l == 1:
            return hs[0]
        r = 0
        stack = [-1]
        hs.append(0)
        l = len(hs)
        for i in range(l):
            h = hs[i]
            if len(stack) == 1 or h >= hs[stack[-1]]:
                stack.append(i)
                #print("append", i)
            else:
                while len(stack) >= 1 and h < hs[stack[-1]]:
                    s = stack[-1]
                    pre_s = stack[-2]
                    sh = hs[s]
                    now = sh * (i-pre_s-1)
                    if now > r:
                        r = now
                #        print(r, stack, sh, "*", pre_s+1, " to ", i-1)
                    stack.pop()
                stack.append(i)
        return r

def test():
    s=Solution()
    hs = [1]
    hs = [1,1]
    hs = [2,1,5,6,2,3]
    hs=[6, 7, 5, 2, 4, 5, 9, 3]
    #print(hs)
    r=s.largestRectangleArea(hs)
    print(r)

test()
