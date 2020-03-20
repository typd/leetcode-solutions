class Solution(object):
    def maxProfit(self, ps):
        if len(ps) == 0:
            return 0
        d=[
                [0] * len(ps),
                [0] * len(ps),
                [0] * len(ps)]

        for k in range(1,3):
            for i in range(1,len(ps)):
                d[k][i] = max(d[k][i-1], d[k-1][i])
                j = i-1
                while j >= 0:
                    if ps[i] > ps[j]:
                        last = 0
                        if j > 0:
                            last = d[k-1][j-1]
                        d[k][i] = max(d[k][i], last + ps[i]-ps[j])
                    elif j > 0 and ps[j] <= ps[j-1]:
                        break
                    j-=1
                #print("k:", k, "i:", i, "::::", ps[:i+1], d[k][i], ",", d[k][i-1], d[k-1][i])
        return d[2][len(ps)-1]

def test():
    ss = Solution()
    ps = [1]
    ps = [6,1,3,2,4,7]
    ps = [7,6,4,3,1] 
    ps = [2,4,1]
    ps = [1,2,3,4,5]
    ps = [1,2,4,2,5,7,2,4,9,0]
    ps = [3,3,5,0,0,3,1,4]
    r = ss.maxProfit(ps)
    print(ps)
    print(r)

test()
