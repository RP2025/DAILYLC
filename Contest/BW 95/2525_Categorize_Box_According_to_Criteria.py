class Solution:
    def categorizeBox(self, length: int, width: int, height: int, mass: int) -> str:
        ans = 0
        if length >= 10000 or width >= 10000 or height >= 10000 or length*width*height >= 1000000000:
            ans = 1
        if mass >= 100:
            if ans == 1:
                ans = 12
            else:
                ans = 2
            
        if ans == 1:
            return "Bulky"
        elif ans == 2:
            return "Heavy"
        elif ans == 12:
            return "Both"
        return "Neither"
