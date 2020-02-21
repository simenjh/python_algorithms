class Solution:
    def isPowerOfFour(self, num: int) -> bool:
        if(num == 1):
            return True
        elif(num == 0):
            return False
        rem = 0
        while rem == 0:
            if(num == 4):
                return True
            else:
                rem = num % 4
                num = int(num/4)
        return False
        
