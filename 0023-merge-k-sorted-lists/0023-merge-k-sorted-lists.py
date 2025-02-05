# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        ndict={}
        for i in range(len(lists)):
            if not lists[i]:
                continue
            curr=lists[i]
            while curr!=None:
                if curr.val not in ndict:
                    head=ListNode(curr.val)
                    ndict[curr.val]=[head,head]
                else:
                    ndict[curr.val][1].next=ListNode(curr.val)
                    ndict[curr.val][1]=ndict[curr.val][1].next
                curr=curr.next
        if not ndict:
            return None
        myNums=list(ndict.keys())
        myNums.sort()
        tail_node=ndict[myNums[0]][1]
        i=1
        while i<len(myNums):
            tail_node.next=ndict[myNums[i]][0]
            tail_node=ndict[myNums[i]][1]
            i+=1
        return ndict[myNums[0]][0]

