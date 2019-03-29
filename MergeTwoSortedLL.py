# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def mergeTwoLists(l1, l2):
    if l1 == None:
        return l2
    if l2 == None:
        return l1
    start = None
    temp = start
    while l1 != None and l2 != None:
        if int(l1.val) > int(l2.val):
            temp = l2
            temp.next = l1
            l2 = l2.next
        elif int(l1.val) > int(l2.val):
            temp = l1
            temp.next = l2
            l1 = l1.next
        else:
            temp = l1
            l1 = l1.next
            temp.next = l2
            l2 = l2.next
    return start        
                
l1 = ListNode(1)
l1.next = ListNode(2)
l1.next.next = ListNode(4)

l2 = ListNode(1)
l2.next = ListNode(3)
l2.next.next = ListNode(4)

l = mergeTwoLists(l1, l2)
while l != None:
    print(int(l.val))
    l = l.next