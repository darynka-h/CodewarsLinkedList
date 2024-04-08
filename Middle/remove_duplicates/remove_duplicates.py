class Node(object):
    def __init__(self, data):
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
    required_result = list(set(result))
    required_result.sort()
    return required_result


def remove_duplicates(head):
    if head is None:
        return None
    result = []
    data_list = listyfy(head)
    data_list = data_list[::-1]
    for i, el in enumerate(data_list):
        if i == 0:
            result.append(Node(int(el)))
        else:
            new_node = Node(int(el))
            new_node.next = result[-1]
            result.append(new_node)
    return result[-1]
