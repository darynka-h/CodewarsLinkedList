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

def removeLastNode(head):
    if head == None:
        return None
    if head.next == None:
        head = None
        return None
    second_last = head
    while(second_last.next.next):
        second_last = second_last.next
    second_last.next = None
    return head

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

def reverse(head):
    if head.next is None:
        return head
    length_list = get_len(head)
    last_node = get_nth(head, length_list - 1)
    return 

# def get_len(node):
#     """The function returns length
#     of linked list
#     """
#     counter = 0
#     prob = node
#     while prob is not None:
#         counter += 1
#         prob = prob.next
#     return counter

# print(get_len(removeLastNode(build_one_two_three())))