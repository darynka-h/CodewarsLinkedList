class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None


def sorted_insert(head, data):
    """The function insert Node in linked 
    list in in ascending order"""
    tail = Node(data)
    if head is not None:
        prob = head
        while prob is not None:
            if prob.data > data:
                tail.next = prob
                return tail
            elif prob.data < data and prob.next is not None and prob.next.data > data:
                tail.next = prob.next
                prob.next = tail
                return head
            elif prob.next is None:
                prob.next = tail
                return head
            prob = prob.next
    elif head is None:
        return Node(data)
