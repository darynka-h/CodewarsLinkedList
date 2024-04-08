class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def loop_size(node):
    slow = node
    fast = node.next
    while slow != fast:
        slow = slow.next
        fast = fast.next.next
    counter = 1
    slow = slow.next
    while slow != fast:
        slow = slow.next
        counter += 1
    return counter


# def build_one_two_three():
#     """The function returns linked Node
#     1 -> 2 -> 3
#     """
#     node_3 = Node(3)
#     node_2 = Node(2)
#     node_3.next = node_2
#     node_2.next = node_3
#     node_1 = Node(1)
#     node_1.next = node_2
#     return node_1


# print(loop_size(build_one_two_three()))