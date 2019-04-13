# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        '''
        You are given two non-empty linked lists representing two non-negative integers. 
        The digits are stored in reverse order and each of their nodes contain a single digit. 
        Add the two numbers and return it as a linked list.
        You may assume the two numbers do not contain any leading zero, except the number 0 itself.    
        '''
        lst1=self.linklist2list(l1)
        lst1.reverse()
        s1=''.join(lst1)
        num1=int(s1)
        lst2=self.linklist2list(l2)
        lst2.reverse()
        s2=''.join(lst2)
        num2=int(s2)
        sumnum=num1+num2
        lstsum=list(str(sumnum))
        lstsum.reverse()
        lstsum=[int(x) for x in lstsum]
        result=self.list2linklist(lstsum)
        return result
        
        
    def linklist2list(self,l1:ListNode)->list:
        np=l1
        nl=[]
        nl.append(str(l1.val))
        while np.next!=None:
            nl.append(str(np.next.val))
            np=np.next
        return nl
    
    def list2linklist(self,l1:list)->ListNode:
        node=result=ListNode(l1[0])
        for i in range(len(l1)-1):
            nxnode=ListNode(l1[i+1])
            node.next=nxnode
            node=nxnode
        return result
    '''
    abstract:
    turn the linklist to a list then to a int by using str() and .reverse(),finally turn the result back to ListNode
    '''
