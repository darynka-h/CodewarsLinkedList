class Node:
    """Represents a singly linked node."""
    def __init__(self, data, next = None):
        """Instantiates a Node with a default next of None."""
        self.data = data
        self.next = next


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


# if __name__ == "__main__":
#     import doctest
#     doctest.testmod()
