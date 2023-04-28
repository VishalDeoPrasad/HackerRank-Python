def insertNodeAtPosition(llist, data, position):
    node = SinglyLinkedListNode(data)
    node.next = None
    
    if llist is None:
        return node
    
    if position == 0:
        node.next = llist
        return node
    
    else:
        temp = llist
        cnt = 0
        while cnt < position-1:
            cnt += 1
            temp = temp.next
        
        node.next = temp.next
        temp.next = node
        return llist
            