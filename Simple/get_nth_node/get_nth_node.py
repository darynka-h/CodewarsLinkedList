class Node(object):
    """Node class for reference"""
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


def get_len(node):
    """The function returns length
    of linked list
    """
    counter = 0
    prob = node
    while prob is not None:
        counter += 1
        prob = prob.next
    return counter


def get_nth(node, index):
    """The function return element by
    index in linked list
    """
    node_length = get_len(node)
    if index >= node_length or index < 0:
        raise IndexError
    counter = 0
    prob = node
    while counter < index and prob is not None:
        counter += 1
        prob = prob.next
    return prob
