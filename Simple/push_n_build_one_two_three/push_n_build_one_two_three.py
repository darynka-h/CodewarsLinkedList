class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def push(head, data):
    """The function link data to head"""
    if head is None:
        return Node(data)
    new_node = Node(data)
    new_node.next = head
    return new_node


def build_one_two_three():
    """The function returns linked Node
    1 -> 2 -> 3
    """
    node_3 = Node(3)
    node_2 = Node(2)
    node_2.next = node_3
    node_1 = Node(1)
    node_1.next = node_2
    return node_1
