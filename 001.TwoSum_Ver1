class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        '''
        目标是给定一个整数数组 nums 和一个目标值 target，请你在该数组中找出和为目标值的那 两个 整数，并返回他们的数组下标。
        你可以假设每种输入只会对应一个答案。但是，你不能重复利用这个数组中同样的元素
        打算用字典存储历史来做搜索
        '''
        dictnum={}
        for indexc,num in enumerate(nums):
            
            cnum =target-num 
            if cnum in dictnum :
            # 注意此处的in搜索的是key不是value!
               return [dictnum[cnum],indexc]
            dictnum[num]=indexc
            # 此处的赋值不能放在for的下一行，因为目标是搜索以前的项有没有与当前项匹配的
            # 如果这么做了，就会出现当输入list中答案为等值不同元素时只能搜出第一个，违背了不能重复利用数组同样元素这一条
        return []
