class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None


class Context(object):
    def __init__(self, source, dest):
        self.source = source
        self.dest = dest


def move_node(source, dest):
    start_node = Node(source.data)
    start_node.next = dest
    dest = start_node
    source = source.next
    return Context(source, dest)
