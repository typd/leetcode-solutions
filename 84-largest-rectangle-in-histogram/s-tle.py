class Solution(object):
    def largestRectangleArea(self, hs):
        l = len(hs)
        if l == 1:
            return hs[0]
        r = 0
        last_min_h = []
        for i in range(l):
            last_min_h.append(0)
        for cur_l in range(1,l+1):
            min_h = []
            for i in range(l):
                min_h.append(0)
            for start_i in range(l + 1 - cur_l):
                if cur_l == 1:
                    min_h[start_i] = hs[start_i]
                else:
                    min_h[start_i] = min(last_min_h[start_i + 1], hs[start_i])
                if min_h[start_i] * cur_l > r:
                    r = min_h[start_i] * cur_l
            #print("cur_l, r", cur_l, r)
            #print(last_min_h)
            #print(min_h)
            #print("")
            last_min_h = min_h

        return r

def test():
    s=Solution()
    hs = [1]
    hs = [1,1]
    hs = [2,1,5,6,2,3]
    r=s.largestRectangleArea(hs)
    print(r)

test()
