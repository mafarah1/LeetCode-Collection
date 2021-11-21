class Solution:
    def reverse(self, x: int) -> int:
        n = str(x)[::-1]
        if n[-1] == "-":
            if -2**31 < int("-"+n.replace("-",'')) < 2**31-1:
                return int("-"+n.replace('-',''))
            else:
                return 0
        else:
            if -2**31 < int(n) < 2**31-1:
                return int(n)
            else:
                return 0