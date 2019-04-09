class Solution:
    def reverse(self, x: int) -> int:
        '''
        题目：Given a 32-bit signed integer, reverse digits of an integer.
        Assume we are dealing with an environment which could only store integers within the 32-bit signed integer range: [−2^31,  2^31 − 1]. 
        For the purpose of this problem, assume that your function returns 0 when the reversed integer overflows.
        思路：先获取符号位，然后取绝对值转换为list，调用reverse()再转换回去
        '''
        # my function starts

        if x>=0: 
            sflag=True
        else:
            sflag=False
        xabsS=str(abs(x))
        xVList=list(xabsS)
        xVList.reverse()
        #注意此处.reverse()是无返回值的，但是xVList已经被反转了
        SR="".join(xVList)
        xVR=int(SR)
        if not(sflag) : xVR=-xVR
        if xVR < -(2**31) or xVR > (2**31 -1):
            return 0
        #注意，提出的需求不仅x要求在32bit内，而且反转后的值不在32bit内则返回0
        else:
            return xVR
