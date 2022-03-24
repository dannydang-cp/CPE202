class Node:
    """ An data structure that stores a data the next Node object
    Attributes:
        value(*): The value that will be stored in this Node. Can be any data
                 type.
        next(Node): The next Node if it exist, else None.
        prev(Node: The prev Node if it exist, else None.
    """

    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None

    def __repr__(self):
        return str(self.value)


class OrderedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.num_nodes = 0

    def __repr__(self):
        node_list = []
        temp = self.head
        while temp is not None:
            node_list.append(temp.value)
            temp = temp.next
        return str(node_list)

    def add(self, item):
        """Adds a new item to the list while keep the numerical order of smallest
        to largest. The item is the input and returns nothing"""
        current = self.head
        previous = None

        while current is not None:
            if current.value > item:
                break
            previous = current
            current = current.next

        if previous is None:
            new_node = Node(item)
            new_node.next = current
            new_node.prev = None
            self.head = new_node

            if self.num_nodes == 0:
                self.tail = new_node
            else:
                current.prev = new_node

        elif current is None:
            new_node = Node(item)
            new_node.next = current
            new_node.prev = previous
            previous.next = new_node
            self.tail = new_node

        else:
            new_node = Node(item)
            new_node.next = current
            new_node.prev = previous
            current.prev = new_node
            previous.next = new_node

        self.num_nodes += 1

    def remove(self, item):
        """Removes the item from the list and modifies the list to keep it's
        numerical order. The input is the item and the returns nothing"""
        current = self.head
        index = 0

        while current is not None:
            if current.value == item:
                break
            current = current.next
            index += 1

            if current is None:
                return -1

        if index == 0:
            self.head = current.next
            self.head.prev = None
        elif current.next is None:
            self.tail = current.prev
            self.tail.next = None
        else:
            current.prev.next = current.next
            current.next.prev = current.prev
        self.num_nodes -= 1

    def search_forward(self, item):
        """Searches the list for the item and starts for the front to the end.
        The input is the item and the output is a boolean of True if found"""
        current = self.head
        while current is not None:
            if current.value == item:
                return True
            else:
                current = current.next
        return False

    def search_backward(self, item):
        """Searches the list for the item and starts for the end to the front.
        The input is the item and the output is a boolean of True if found"""
        current = self.tail
        while current is not None:
            if current.value == item:
                return True
            else:
                current = current.prev
        return False

    def is_empty(self):
        """Returns a boolean of True if the list is empty"""
        return self.num_nodes == 0

    def size(self):
        """Returns a integer value of the size of the list"""
        return self.num_nodes

    def index(self, item):
        """Returns the index value of where the input item is"""
        index = 0
        curr = self.head
        if curr.value == item:
            return 0
        else:
            i = 0
            while i < self.num_nodes:
                i += 1
                if curr.value == item:
                    return index
                else:
                    curr = curr.next
                    index += 1
            return -1

    def pop(self):
        """Removes the last item in the list and returns that item removed"""
        current = self.head
        previous = None
        if current.next is None:
            self.head = None
        else:
            while current.next is not None:
                previous = current
                current = current.next
            previous.next = None
        return current.value

    def pop_pos(self, pos):
        """Removes the item at the inputted positions and returns the removed item"""
        index = 0
        current = self.head
        previous = None
        if pos == 0:
            self.head = current.next
        else:
            while index < pos:
                index += 1
                previous = current
                current = current.next
            previous.next = current.next
        return current.value
