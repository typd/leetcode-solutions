class Solution(object):
    def insert(self, intervals, working):
        r = []
        s = working[0]
        e = working[1]
        for pair in intervals:
            print(r,s,e,pair)
            print()
            cs = pair[0]
            ce = pair[1]
            if ce < s:
                r.append(pair)
            elif cs <= s and ce >= s and ce <= e:
                s = cs
                e = e
            elif cs >= s and ce <= e:
                pass
            elif cs <=s and ce >= e:
                s = cs
                e = ce
            elif cs >= s and cs <= e and ce >= e:
                s = s
                e = ce
            elif cs > e:
                r.append([s,e])
                s = cs
                e = ce
            else:
                print("should not happen")
                print(r,s,e,cs,ce)
        r.append([s,e])
        return r

def test():
    s=Solution()
    cur = [[1,2],[3,5],[6,7],[8,10],[12,16]]
    new = [4,8]
    cur = [[1,3],[6,9]]
    new = [2,5]
    r=s.insert(cur, new)
    print(cur)
    print(new)
    print(r)

test()
