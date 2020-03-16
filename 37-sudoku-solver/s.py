class Solution(object):
    def solveSudoku(self, b):
        slots = []
        for i in range(9):
            for j in range(9):
                if b[i][j] == '.':
                    s = [i,j]
                    options = ['1','2','3','4','5','6','7','8','9']
                    for ki in range(9):
                        v = b[ki][j]
                        if v in options:
                            options.remove(v)
                    for kj in range(9):
                        v = b[i][kj]
                        if v in options:
                            options.remove(v)
                    ki_s = (i/3) * 3
                    kj_s = (j/3) * 3
                    for di in range(3):
                        for dj in range(3):
                            ki = ki_s + di
                            kj = kj_s + dj
                            v = b[ki][kj]
                            if v in options:
                                #print("removing", ki,kj,v,ki_s,kj_s,di,dj)
                                options.remove(v)
                    s.append(options)
                    slots.append(s)
        r = self.put(b,slots)
        print(r)

    def put(self,b,origin_slots):
        slots = list(origin_slots)
        if len(slots) == 0:
            return True
        target = None
        for s in slots:
            if target == None or len(s[2]) < len(target):
                target = s
        slots.remove(target)
        i = target[0]
        j = target[1]
        o = target[2]
        for k in o:
            b[i][j] = k
            new_slots = []
            allright = True
            for s in slots:
                si = s[0]
                sj = s[1]
                so = s[2]
                new_so = list(so)
                if k in so:
                    if si == i or sj == j or (i/3 == si/3 and j/3==sj/3):
                        new_so.remove(k)
                        if len(new_so) == 0:
                            allright = False
                            break
                new_s=[si,sj,new_so]
                new_slots.append(new_s)
            if allright:
                if self.put(b,new_slots):
                    return True
        return False

def test():
    s=Solution()
    b=[
            ['5','3','.','6','.','8','9','1','2'],
            ['6','7','2','1','9','5','3','4','.'],
            ['1','.','8','3','4','2','.','6','7'],
            ['8','5','.','.','6','1','4','2','3'],
            ['4','.','6','8','5','3','7','.','1'],
            ['7','1','3','.','2','4','8','5','6'],
            ['.','6','1','5','3','.','2','8','4'],
            ['2','8','7','.','1','9','6','3','.'],
            ['3','4','.','2','8','6','1','.','9']]
    b=[
            ["5","3",".",".","7",".",".",".","."],
            ["6",".",".","1","9","5",".",".","."],
            [".","9","8",".",".",".",".","6","."],
            ["8",".",".",".","6",".",".",".","3"],
            ["4",".",".","8",".","3",".",".","1"],
            ["7",".",".",".","2",".",".",".","6"],
            [".","6",".",".",".",".","2","8","."],
            [".",".",".","4","1","9",".",".","5"],
            [".",".",".",".","8",".",".","7","9"]]
    for line in b:
        print(line)
    print()
    s.solveSudoku(b)
    for line in b:
        print(line)

test()
