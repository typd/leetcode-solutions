class Solution(object):
    def num(self,s,allow_dot=True):
        if len(s) == 0:
            return False
        if s[0] in ['-','+']:
            s = s[1:]
        had_num = False
        had_dot = False
        for c in s:
            if c == ".":
                if not allow_dot:
                    return False
                if had_dot:
                    return False
                had_dot = True
            elif c in ["0","1","2","3",'4','5','6','7','8','9']:
                had_num = True
            else:
                return False
        return had_num

    def isNumber(self, s):
        while len(s) > 0 and s[0]==" ":
            s=s[1:]
        while len(s) > 0 and s[-1]==" ":
            s=s[:-1]
        e_index = -1
        for i in range(len(s)):
            if s[i] == "e":
                e_index = i
                break
        if e_index > -1:
            s1 = s[:e_index]
            s2 = s[e_index + 1:]
            return self.num(s1) and self.num(s2,False)
        else:
            return self.num(s)
        return False

def test():
    ss = Solution()
    sl = [
            "0","-1","2e10", "-3e2.5","-2e1","--6", "95a54e53", ".1"]
    # ".1" is True
    for s in sl:
        r = ss.isNumber(s)
        print(s, r)

test()


