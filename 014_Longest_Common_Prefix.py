class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        '''
        Write a function to find the longest common prefix string amongst an array of strings.
        If there is no common prefix, return an empty string ""
        '''
        if len(strs)==0:return ''
        elif len(strs)==1:return strs[0]
        prefix=self.cmp_two_str(strs[0],strs[1])
        if len(strs)==2:return prefix
        # pay attention to the special cases of only 0,1,2 strings in strs
        for crnts in strs[2:]:
            prefix = self.cmp_two_str(prefix,crnts)
            if prefix =='' :
                return ''
        return prefix
    def cmp_two_str(self,str1:str,str2:str) -> str:
        '''
        find the longest common prefix in two string by compare the str1 and str2 char by char
        '''
        minlen=min(len(str1),len(str2))
        cmlen=0
        for i in range(minlen):
            if str1[i]==str2[i]:
                cmlen+=1
            else: return str1[:cmlen]
        return str1[:cmlen]
    '''
    abstract:
    horizontal scanning
    '''
