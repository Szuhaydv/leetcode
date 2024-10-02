from list_node import ListNode

# destroys the original list and builds a new one as describe in the book
# (you might also want to sort in place, either with preserving node identity or just value swapping)
def selection_sort(list):
    newList = ListNode()
    endOfList = newList

    while list:
        largestNode = nodeBeforeLargest = prevNode = list
        currentNode = list.next
        while currentNode:
            if currentNode.val > largestNode.val:
                largestNode = currentNode
                nodeBeforeLargest = prevNode
            prevNode = currentNode
            currentNode = currentNode.next
        # append to newList
        endOfList.next = ListNode(largestNode.val)
        endOfList = endOfList.next
        # remove from old list
        if largestNode == list:
            list = list.next
        else:
            nodeBeforeLargest.next = largestNode.next

    return newList.next
    

