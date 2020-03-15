class Solution(object):
    def fullJustify(self, ws, width):
        lines = []
        cur_line = []
        cur_left = width
        for w in ws:
            l = len(w)
            needs = l + 1
            if len(cur_line)==0:
                needs = l
            if cur_left >= needs:
                cur_line.append(w)
                cur_left -= needs
            else:
                lines.append(cur_line)
                cur_line = [w]
                cur_left = width - l
        lines.append(cur_line)
        strs = []
        for i in range(len(lines)):
            line = lines[i]
            if i == len(lines)-1:
                str = " ".join(line)
            else:
                spaces = width
                for w in line:
                    spaces -= len(w)
                slots = len(line) - 1
                str = ""
                for w in line:
                    str += w
                    count = 0
                    if slots > 0:
                        if spaces % slots == 0:
                            count = spaces/slots
                        else:
                            count = spaces/slots + 1
                        str += " " * count
                    spaces -= count
                    slots -= 1
            if len(str) < width:
                str += " " * (width - len(str))
            strs.append(str)
        return strs

def test():
    s=Solution()
    ws = ["What","must","be","acknowledgment","shall","be"]
    w = 16
    ws = ["This", "is", "an", "example", "of", "text", "justification."]
    ws = ["Science","is","what","we","understand","well","enough","to","explain","to","a","computer.","Art","is","everything","else","we","do"]
    w = 20
    r=s.fullJustify(ws, w)
    for l in r:
        print("'", l, "'")

test()
