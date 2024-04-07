class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


def linked_list_from_string(node_string):
    """The function creates linked list
    from a such string '1 -> 2 -> 3 -> None'
    """
    result = []
    splited_list = node_string.split(" -> ")
    rev_splited_list = splited_list[::-1]
    for i, el in enumerate(rev_splited_list):
        if rev_splited_list[i-1] == "None" and el != "None":
            result.append((Node(int(el), None)))
        elif el != "None":
            result.append(Node(int(el), result[-1]))
    if len(result) == 0:
        return None
    return result[-1]

# if __name__ == "__main__":
#     import doctest
#     doctest.testmod()
