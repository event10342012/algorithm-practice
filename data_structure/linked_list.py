class Node:
    def __init__(self, value: int, next_node=None):
        self.__value: int = value
        self.next_node: Node = next_node

    @property
    def value(self):
        return self.__value

    def __next__(self, x=None):
        return x


class LinkedList:
    def __init__(self, first: Node = None):
        self.__first: Node = first

    @property
    def first(self):
        return self.__first

    def print_list(self):
        if not self.first:
            print('List is empty!')
            return

        current = self.first
        while current is not None:
            print(current.value)
            current = current.next_node

    def push_back(self, x):
        new_node = Node(x)

        if self.first is None:
            self.__first = new_node
            return

        current = self.first
        while current.next_node is not None:
            current = current.next_node

        current.next_node = new_node

    def push_front(self, x):
        new_node = Node(x)
        new_node.next_node = self.__first
        self.__first = new_node

    def delete(self, x: int):
        pass

    def clear(self):
        while self.first is not None:
            current = self.first
            self.__first = current.next_node
            del current

    def reverse(self):
        if self.first is None or self.first.next_node is None:
            return

        previous = None
        current = self.first
        preceding = current.next_node

        while self.first is not None:
            current.next_node = previous
            previous = current
            current = preceding
            preceding = preceding.next_node


if __name__ == '__main__':
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
