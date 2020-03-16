class Solution(object):
    def minDistance(self, w1, w2):
        if w1 == "":
            return len(w2)
        if w2 == "":
            return len(w1)
        l1 = len(w1)
        l2 = len(w2)
        d=[]
        for i in range(l1+1):
            d.append([0] * (l2 + 1))
        for i in range(0, l1 + 1):
            for j in range(0, l2 + 1):
                if i==0 and j!=0:
                    d[i][j] = j
                if i!=0 and j==0:
                    d[i][j] = i

        for i in range(1, l1 + 1):
            for j in range(1, l2 + 1):
                if w1[i-1] == w2[j-1]:
                    d[i][j] = d[i-1][j-1]
                else:
                    #print("--d[i-1][j]", d[i-1][j])
                    #print("--d[i][j-1]", d[i][j-1])
                    d[i][j] = min(d[i-1][j], d[i][j-1], d[i-1][j-1]) + 1
                #print(i,j,w1[:i], w2[:j], d[i][j])
        return d[l1][l2]

def test():
    s=Solution()
    w1 = "abc"
    w2 = "1abc"
    w1 = "abc1"
    w2 = "abc"
    w1 = "abc"
    w2 = "abc1"
    w1="sma"
    w2="uism"
    w1="ity"
    w2="ties"
    w1="asma"
    w2="truism"
    w1="prosperity"
    w2="properties"
    w1 = "horse"
    w2 = "ros"
    w1 = "abcde"
    w2 = "bcdea"
    w1 = "intention"
    w2 = "execution"
    r=s.minDistance(w1,w2)
    print(w1)
    print(w2)
    print(r)

test()
