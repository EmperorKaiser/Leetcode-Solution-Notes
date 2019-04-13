class Solution:
    def isPalindrome(self, x: int) -> bool:
        '''
        Determine whether an integer is a palindrome. An integer is a palindrome when it reads the same backward as forward.
        '''
        # My function starts here
        xList=list(str(x))
        nLoop=math.floor(len(xList)/2)
        for i in range(nLoop):
            if xList[i]!=xList[-i-1]:
                return False
        return True
        '''
        abstract
        Using list and compare the string of x.Pay attention that the sign is also turned into a char in the String
        '''
