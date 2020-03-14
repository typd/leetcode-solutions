class Solution(object):
    def can_be_zero(self,p):
        for i in range(len(p)):
            if p[i] != "*":
                if i==len(p)-1:
                    return False
                if p[i+1]!="*":
                    return False
        return True

    def trim(self, p):
        new_p = ""
        size = len(p)
        ignore_next = False
        for i in range(len(p)):
            if ignore_next:
                ignore_next = False
                continue
            if p[i] != "*" and i<size-1 and p[i+1]=="*" and len(new_p)>=2 and new_p[-1]=="*" and new_p[-2]==p[i]:
                ignore_next = True
            else:
                new_p+=p[i]
        return new_p 

    def isMatch(self, s, p):
        new_p=self.trim(p)
        print("s    :", s)
        print("new_p:", new_p)
        return self.check(s, new_p)

    def check(self, s, p):
        if len(s)==0:
            if len(p)==0:
                return True
            if self.can_be_zero(p):
                return True
            return False
        if len(p)==0:
            return False
        if p[0] == '.':
            if len(p) > 1 and p[1]=="*":
                # 3 choices
                if self.check(s,p[2:]):
                    return True
                if self.check(s[1:],p[2:]):
                    return True
                if self.check(s[1:],p):
                    return True
                return False
            else:
                return self.check(s[1:],p[1:])
        if p[0] == s[0]:
            if len(p) > 1 and p[1]=="*":
                # 3 choices
                if self.check(s,p[2:]):
                    return True
                if self.check(s[1:],p[2:]):
                    return True
                if self.check(s[1:],p):
                    return True
                return False
            else:
                return self.check(s[1:],p[1:])
        else:
            if len(p) > 1 and p[1]=="*":
                return self.check(s,p[2:])
            else:
                return False

def test():
    ss = Solution()
    s = "aaa"
    p = "abb"
    s = "bbb"
    p = "bbb"
    s = "ccccccc"
    p = "c*"
    s = "ccccccc"
    p = "a*c*"
    s = "bbb"
    p = "b.b"
    s = "abcd"
    p = ".*"
    s = "bbbba"
    p = ".*a*a"
    s="aaaaaaaaaaaaab"
    p="a*a*a*a*a*a*a*a*c"
    s="aaaaaaaaaaaaab"
    p="a*a*a*a*a*a*a*a*a*a*a*a*b"
    r = ss.isMatch(s,p)
    print("s:", s)
    print("p:", p)
    print(r)

test()


