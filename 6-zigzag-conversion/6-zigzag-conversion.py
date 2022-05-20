class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if s is None or numRows is None:
            return ''
        if numRows == 1:
            return s
        rows = [ '' for _ in range(numRows) ]
        i = 0
        opposite = False
        for j in s:
            if i < numRows - 1 and opposite == False:
                rows[i]+=j
                i+=1
            elif i >0:
                rows[i]+=j
                i-=1
            if i == 0:
                opposite = False
            if i == numRows - 1:
                opposite = True
        return ''.join(rows)
        