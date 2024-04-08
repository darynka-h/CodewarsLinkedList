class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None

def swap_pairs(head):
    if head is None:
        return None
    main_head_do_not_touch = head
    parent = None
#     print(listyfy(main_head_do_not_touch))
    if head is not None:
        counter = 0
        probe = head
        while probe is not None and probe.next is not None:
            a, b, c = probe, probe.next, probe.next.next
            if not counter % 2:
                if counter == 0:
                    main_head_do_not_touch = main_head_do_not_touch.next
                a.next = c
                b.next = a
                if parent:
                    parent.next = b   
            probe, parent = c, a
            counter += 2
    return main_head_do_not_touch



# def listyfy(node):
#     """Stringify linked list
#     >>> stringify(Node(1, Node(2, Node(3))))
#     '1 -> 2 -> 3 -> None'
#     """
#     result = []
#     if node is None:
#         return "None"
#     else:
#         probe = node
#         while probe is not None:
#             result.append(probe.data)
#             probe = probe.next
#     # result.sort()
#     return result

# def build_one_two_three():
#     """The function returns linked Node
#     1 -> 2 -> 3
#     """
#     node_4 = Node("D")
#     node_3 = Node("C")
#     node_3.next = node_4
#     node_2 = Node("B")
#     node_2.next = node_3
#     node_1 = Node("A")
#     node_1.next = node_2
#     return node_1

# class Node:
#     def __init__(self, data, next=None):
#         self.data = data
#         self.next = next

# def swap_pairs(head):
#     main_head_do_not_touch = head
#     parent = None
#     print(listyfy(main_head_do_not_touch))
#     if head is not None:
#         counter = 0
#         probe = head
#         while probe is not None and probe.next is not None:
#             a, b, c = probe, probe.next, probe.next.next
#             print(probe.data)
#             if not counter % 2:
#                 if counter == 0:
#                     main_head_do_not_touch = main_head_do_not_touch.next
#                 a.next = c
#                 b.next = a
#                 if parent:
#                     parent.next = b   
#             probe, parent = c, a
#             print(main_head_do_not_touch.data, listyfy(main_head_do_not_touch))
#             counter += 2
#             # break
#     return main_head_do_not_touch

# A = build_one_two_three()
# new_head = swap_pairs(A)
# print('real answer ->', new_head.data, listyfy(new_head))
