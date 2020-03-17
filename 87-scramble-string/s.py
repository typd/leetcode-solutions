class Solution(object):
    def isScramble(self, s1, s2):
        if s1 == s2:
            #print("True", s1, s2)
            return True
        l1 = len(s1)
        l2 = len(s2)
        if l1 != l2:
            return False
        m1={}
        m2={}
        for i in range(l1):
            c1=s1[i]
            if c1 in m1:
                m1[c1] = m1[c1] + 1
            else:
                m1[c1]=1
            c2=s2[i]
            if c2 in m2:
                m2[c2] = m2[c2] + 1
            else:
                m2[c2]=1
        for c in m1:
            if (not c in m2) or m1[c] != m2[c]:
                #print("False1", s1, s2)
                return False

        for i in range(1, l1):
            s11 = s1[:i]
            s12 = s1[i:]
            s21 = s2[:i]
            s22 = s2[i:]
            #print("checking", s11, s12, "   ", s21, s22)
            if self.isScramble(s11, s21) and self.isScramble(s12, s22):
                return True
            j = l1 - i
            s21 = s2[:j]
            s22 = s2[j:]
            #print("checking", s11, s12, "   ", s21, s22)
            if self.isScramble(s11, s22) and self.isScramble(s12, s21):
                return True
        #print("False2", s1, s2)
        return False

def test():
    ss = Solution()
    s1 = "great"
    s2 = "rgtae"
    s1 = "great"
    s2 = "rgeat"
    s1 = "abcde"
    s2 = "caebd"
    s1 = ""
    s2 = ""
    s1 = "a"
    s2 = "bb"
    print(s1)
    print(s2)
    r = ss.isScramble(s1,s2)
    print(r)

test()


