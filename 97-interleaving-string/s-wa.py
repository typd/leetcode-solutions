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
        while t3 <= l3-1:
            print("checking", t3, s3[t3])
            print("  s1:", s1[t1:])
            print("  s2:", s2[t2:])
            print("  s3:", s3[t3:])
            if t1 <= l1-1:
                c1 = s1[t1]
            else:
                c1 = "c1end"
            if t2 <= l2-1:
                c2 = s2[t2]
            else:
                c2 = "c2end"
            c3 = s3[t3]
            if c1 == c2 and c1 == c3:
                if t1 + 1 <= l1-1:
                    c1n = s1[t1+1]
                else:
                    c1n = "c1end"
                if t2 + 1 <= l2-1:
                    c2n = s2[t2+1]
                else:
                    c2n = "c2end"
                if t3+1 <= l3-1:
                    c3n = s3[t3+1]
                    if c3n == c1n:
                        t1 += 1
                    else:
                        t2 += 1
                else:
                    t1 += 1
            elif c1 == c3:
                print("  use s1:", t1, s1[t1])
                t1 += 1
            elif c2 == c3:
                print("  use s2:", t2, s2[t2])
                t2 += 1
            else:
                print("  no match")
                return False
            t3 += 1
        return True

def test():
    ss = Solution()
    s1 = "aabcc"
    s2 = "dbbca"
    s3 = "aadbbcbcac"
    s1="aabcc"
    s2="dbbca"
    s3="aadbbbaccc"
    s1="aabd"
    s2="abdc"
    s3="aabdabcd"
    r = ss.isInterleave(s1,s2,s3)
    print(s1)
    print(s2)
    print(s3)
    print(r)

test()


