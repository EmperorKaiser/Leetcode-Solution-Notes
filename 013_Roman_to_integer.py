class Solution:
    def romanToInt(self, s: str) -> int:
        '''
        Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.
        For example, two is written as II in Roman numeral, just two one's added together. 
        Twelve is written as, XII, which is simply X + II. 
        The number twenty seven is written as XXVII, which is XX + V + II.
        Roman numerals are usually written largest to smallest from left to right. 
        However, the numeral for four is not IIII. Instead, the number four is written as IV. 
        Because the one is before the five we subtract it making four. The same principle applies to the number nine, 
        which is written as IX. 
        There are six instances where subtraction is used:
            I can be placed before V (5) and X (10) to make 4 and 9.
            X can be placed before L (50) and C (100) to make 40 and 90. 
            C can be placed before D (500) and M (1000) to make 400 and 900.
            Given a roman numeral, convert it to an integer. Input is guaranteed to be within the range from 1 to 3999.
        '''
        # my function starts
        SNdict = {'I':0,'V':0,'X':0,'L':0,'C':0,'D':0,'M':0}
        #number of the corresponding symbols
        Slist = ['I','V','X','L','C','D','M']
        SSNdict={'CM':0,'CD':0,'XC':0,'XL':0,'IX':0,'IV':0}
        #number of the corresponding symbols
        SSlist=['CM','CD','XC','XL','IX','IV']
        for sx in SSlist:
            SSNdict[sx]=s.count(sx)
            s=s.replace(sx,'')
            # remove the counted symbols ,mention that the original s won't be changed if not resigned
        for sx in Slist:
            SNdict[sx]=s.count(sx)
            s=s.replace(sx,'')
            # remove the counted symbols ,mention that the original s won't be changed if not resigned

        if not(s):
            result = \
            (1*SNdict['I']+5*SNdict['V']+10*SNdict['X']+50*SNdict['L']+100*SNdict['C'] \
            +500*SNdict['D']+1000*SNdict['M']+900*SSNdict['CM']+400*SSNdict['CD']+90*SSNdict['XC'] \
            +40*SSNdict['XL']+9*SSNdict['IX']+4*SSNdict['IV'] )
            return result
       ''' 
       abstract:
       scan the given s and count the special substrings of 'CM','CD','XC'... 
       and then count the substrings of 'M','D','C'...mention that the symbols that have been counted should be removed
       '''
