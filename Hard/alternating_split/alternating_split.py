class Node(object):
    def __init__(self, data=None):
        self.data = data
        self.next = None


class Context(object):
    def __init__(self, first, second):
        self.first = first
        self.second = second


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


def alternating_split(head):
    """The function splits linked list
    into two different lists"""
    if head is None:
        raise AssertionError
    data_list = listyfy(head)
    odd = []
    even = []
    for i, el in enumerate(data_list):
        if not i % 2:
            even.append(el)
        elif i % 2:
            odd.append(el)
    odd.reverse()
    even.reverse()
    first = []
    second = []
    for i, el in enumerate(odd):
        if i == 0:
            first.append(Node(el))
        else:
            new_node = Node(el)
            new_node.next = first[-1]
            first.append(new_node)
    for i, el in enumerate(even):
        if i == 0:
            second.append(Node(el))
        else:
            new_node = Node(el)
            new_node.next = second[-1]
            second.append(new_node)
    return Context(second[-1], first[-1])
