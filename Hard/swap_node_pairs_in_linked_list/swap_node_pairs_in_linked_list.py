# працює за умови що є дата
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
    # result.sort()
    return result

def build_one_two_three():
    """The function returns linked Node
    1 -> 2 -> 3
    """
    node_4 = Node("D")
    node_3 = Node("C")
    node_3.next = node_4
    node_2 = Node("B")
    node_2.next = node_3
    node_1 = Node("A")
    node_1.next = node_2
    return node_1

print(listyfy(build_one_two_three()))
# def swap_pairs(head):
#     data_list = listyfy(head)
#     if not len(data_list) % 2:
#         for i, el in enumerate(data_list):
#             if i % 2:
#                 data_list[i], data_list[i - 1] = data_list[i - 1], el
#     if len(data_list) % 2:
#         for i, el in enumerate(data_list[:-1]):
#             if i % 2:
#                 data_list[i], data_list[i - 1] = data_list[i - 1], el
#     # print(data_list)
#     result = []
#     for i, el in enumerate(data_list):
#         if i == 0:
#             result.append(Node(el))
#         else:
#             new_node = Node(el)
#             new_node.next = result[-1]
#             result.append(new_node)
#     return result[-1]

# print(swap_pairs(build_one_two_three()))

class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

def swap_pairs(head):
    main_head_do_not_touch = head
    if head is not None:
        counter = 0
        probe = head
        while probe is not None and probe.next is not None:
            if not counter % 2:
                probe.next.next, probe.next = probe, probe.next.next
#                 нехай наступний посилається на поточний
#                 probe.next.next = probe
#     нехай поточний посилається на те, що посилався наступний
#                 probe.next = probe.next.next
            probe = probe.next
            print(main_head_do_not_touch)
            counter += 1
    return head

print(swap_pairs(build_one_two_three()))