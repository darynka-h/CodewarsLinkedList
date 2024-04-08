class Node(object):
    def __init__(self, data=None):
        self.data = data
        self.next = None

def listyfy(node):
    """Stringify linked list
    >>> stringify(Node(1, Node(2, Node(3))))
    '1 -> 2 -> 3 -> None'
    """
    result = []
    if node is None:
        return "None"
    else:
        probe = node
        while probe is not None:
            result.append(probe.data)
            probe = probe.next
    return result


def reverse(head):
    if head is None:
        return None
    data_list = listyfy(head)
    result = []
    for i, el in enumerate(data_list):
        if i == 0:
            result.append(Node(el))
        else:
            new_node = Node(el)
            new_node.next = result[-1]
            result.append(new_node)
    return result[-1]
