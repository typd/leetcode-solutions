class Solution(object):
    def numDistinct(self, s, t):
        d = []
        for i in range(0, len(s)+1):
            d.append([0] * (len(t)+1))
            d[i][0]=1

        for j in range(1, len(t)+1):
            for i in range(1, len(s)+1):
                sc = s[i-1]
                tc = t[j-1]
                if sc==tc:
                    d[i][j] += d[i-1][j-1]
                d[i][j] += d[i-1][j]
                #print(s[:i], t[:j], d[i][j], ";", d[i-1][j-1], d[i-1][j])
        return d[len(s)][len(t)]

def test():
    ss = Solution()
    s = "babgbag"
    t = "bag"
    s = "rabbbit"
    t = "rabbit"
    r = ss.numDistinct(s, t)
    print(s)
    print(t)
    print(r)

test()
