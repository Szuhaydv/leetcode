# Canonical solution creates empty list and adds nodes one by one
# (probably simpler as we don't need to find starting point or do value checks)

# I had easier time thinkig about finding the smaller starting point (if exists)
# And then adding elements of the other list if they belong between
# the smaller list's current and next element
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # ensure both lists have starting value
        if not list1: return list2
        if not list2: return list1
        # namescape the smaller starting point to list1
        if list1.val > list2.val:
            list1, list2 = list2, list1
        # keep track of the starting point
        listStart = list1

        # while none of the lists ended
        while list1 and list2:
            # check if list2's value belongs before list1's next value (if it exists)
            if list1.next: 
                if list1.next.val >= list2.val:
                    temp = list1.next
                    list1.next = list2
                    list2 = list2.next
                    list1.next.next = temp
                list1 = list1.next
            # if list1 doesn't have a next value:
            # by this point we know list1 is in order and can break
            else:
                break
        # if list2 still has values, append them to list1
        # (it will definitely have at least one if we broke out of the loop)
        if list2:
            list1.next = list2
        return listStart
                
