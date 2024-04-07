


class Node:
    def __init__(self, data, next=None): 
        self.data = data
        self.next = next


def linked_list_from_string(node_string):
    """The function creates linked list
    from a such string '1 -> 2 -> 3 -> None'
    >>> linked_list_from_string('1 -> 2 -> 3 -> None')
    Node(1, Node(2, Node(3)))
    """
    result = []
    splited_list = node_string.split(" -> ")
    rev_splited_list = splited_list[::-1]
    print(rev_splited_list)
    for el in rev_splited_list:
        if el == "None":
            result.append((Node(None, None)))
        else:
            result.append(Node(int(el), result[-1]))
    print(len(result))
    return result[-1]

print(linked_list_from_string('1 -> 2 -> 3 -> None'))


def stringify(node):
    """Stringify linked list
    >>> stringify(Node(1, Node(2, Node(3))))
    '1 -> 2 -> 3 -> None'
    """
    result = ""
    if node is None:
        return "None"
    else:
        probe = node
        while probe is not None:
            if probe.next is None:
                result += f"{probe.data} -> None"
            else:
                result += f"{probe.data} -> "
            probe = probe.next
    return result


print(stringify(linked_list_from_string('1 -> 2 -> 3 -> None')))
