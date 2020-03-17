class Solution(object):
    def isInterleave(self,s1,s2,s3):
        if s1 == "":
            return s3 == s2
        if s2 == "":
            return s3 == s1
        t1 = 0
        t2 = 0
        t3 = 0
        l3 = len(s3)
        l1 = len(s1)
        l2 = len(s2)
        if l1+l2 != l3:
            return False
        d=[]
        for i in range(l1+1):
            d.append([True] * (l2+1))
        for i in range(l1+1):
            for j in range(l2+1):
                if i == 0:
                    c1 = ""
                else:
                    c1 = s1[i-1]
                if j == 0:
                    c2 = ""
                else:
                    c2 = s2[j-1]
                if i==0 and j==0:
                    continue
                c3 = s3[i+j-1]
                if c1 == c3 and d[i-1][j]:
                    d[i][j] = True
                elif c2 == c3 and d[i][j-1]:
                    d[i][j] = True
                else:
                    d[i][j]=False
                #print(s1[:i], ",", s2[:j], ",",s3[:i+j], d[i][j])
                #print("  ", i,j,i+j, s3[i+j], s3)
                #print("  ", c1, c2, c3, d[i-1][j], d[i][j-1])
        return d[l1][l2]

def test():
    ss = Solution()
    s1="aabd"
    s2="abdc"
    s3="aabdabcd"
    s1="aabcc"
    s2="dbbca"
    s3="aadbbbaccc"
    s1 = "aabcc"
    s2 = "dbbca"
    s3 = "aadbbcbcac"
    r = ss.isInterleave(s1,s2,s3)
    print(s1)
    print(s2)
    print(s3)
    print(r)

test()


