class Node:
    def __init__(self, value: int, next_node=None):
        self.__value: int = value
        self.next_node: Node = next_node

    @property
    def value(self):
        return self.__value


class LinkedList:
    def __init__(self, first: Node = None):
        self.__head: Node = first

    @property
    def head(self):
        return self.__head

    def print_list(self):
        if not self.head:
            print('List is empty!')
            return

        current = self.head
        while current is not None:
            print(current.value)
            current = current.next_node

    def push_back(self, x):
        new_node = Node(x)

        if self.head is None:
            self.__head = new_node
            return

        current = self.head
        while current.next_node is not None:
            current = current.next_node

        current.next_node = new_node

    def push_front(self, x):
        new_node = Node(x)
        new_node.next_node = self.__head
        self.__head = new_node

    def delete(self, x: int):
        pass

    def clear(self):
        while self.head is not None:
            current = self.head
            self.__head = current.next_node
            del current

    def reverse(self):
        if self.head is None or self.head.next_node is None:
            return

        previous = None
        current = self.head
        preceding = current.next_node

        while self.head is not None:
            current.next_node = previous
            previous = current
            current = preceding
            preceding = preceding.next_node


if __name__ == '__main__':
    node = Node(1)
    node.__next__(1)
    linked_list = LinkedList()
    linked_list.print_list()
    linked_list.push_back(1)
    linked_list.push_back(2)
    linked_list.push_front(3)
    linked_list.print_list()
    linked_list.reverse()
    linked_list.print_list()
    linked_list.clear()
    linked_list.print_list()
