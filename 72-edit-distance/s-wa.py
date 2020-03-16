class Solution(object):
    def minDistance(self, w1, w2):
        if w1 == "":
            return len(w2)
        if w2 == "":
            return len(w1)
        l1 = len(w1)
        l2 = len(w2)
        p1 = 0
        p2 = 0
        r = 0
        while p1<l1 and p2<l2:
            c11=w1[p1]
            if p1 < l1-1:
                c12 = w1[p1+1]
            else:
                c12 = ""
            c21 = w2[p2]
            if p2 < l2-1:
                c22 = w2[p2+1]
            else:
                c22 = ""
            left1 = l1-p1
            left2 = l2-p2
            if c11 == c21:
                p1+=1
                p2+=1
            elif c12 == c22:
                # replace
                r += 1
                p1+=1
                p2+=1
                print("r", c11, " to ", c21)
            elif left1 > left2:
                if c12 == c21:
                    # delete
                    r+=1
                    p1+=1
                elif c11 == c22:
                    # insert
                    r+=1
                    p2+=1
                else:
                    # replace
                    r+=1
                    p1+=1
                    p2+=1
            elif left1 < left2:
                if c11 == c22:
                    # insert
                    r+=1
                    p2+=1
                elif c12 == c21:
                    # delete
                    r+=1
                    p1+=1
                else:
                    # replace
                    r+=1
                    p1+=1
                    p2+=1
            else:
                r+=1
                p1+=1
                p2+=1
        if p1==l1:
            r += l2 - p2
        if p2==l2:
            r += l1 - p1
        return r

def test():
    s=Solution()
    w1 = "intention"
    w2 = "execution"
    w1 = "abc"
    w2 = "1abc"
    w1 = "abc1"
    w2 = "abc"
    w1 = "abc"
    w2 = "abc1"
    w1="sma"
    w2="uism"
    w1="pity"
    w2="pties"
    w1 = "horse"
    w2 = "ros"
    w1 = "abcde"
    w2 = "bcdea"
    r=s.minDistance(w1,w2)
    print(w1)
    print(w2)
    print(r)

test()
