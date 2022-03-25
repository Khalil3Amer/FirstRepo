class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def addTwoNumbers(self,l1,l2):
        res=[]
        add=False
        while l1!=None or l2!=None:
            
            if l1!=None and l2!=None:
                
                toAdd=l1.val+l2.val + (1 if add else 0)
                if toAdd > 9:
                    toAdd=toAdd%10
                    add=True
                else:
                    add=False
                res.append(toAdd)
                l1=l1.next
                l2=l2.next
            elif l1!=None:
                toAdd=l1.val + (1 if add else 0)
                if toAdd > 9:
                    toAdd=toAdd%10
                    add=True
                else:
                    add=False
                res.append(toAdd)
                l1=l1.next
            elif l2!=None:
                toAdd=l2.val + (1 if add else 0)
                if toAdd > 9:
                    toAdd=toAdd%10
                    add=True
                else:
                    add=False
                res.append(toAdd)
                l2=l2.next
        if add:
            res.append(1)
        header=ListNode(res[len(res)-1])
        if len(res)>1:
            prev=header
            for i in range(len(res)-2,-1,-1):
                prev=ListNode(res[i],prev)
            header=prev
        return header
                    
        
                    