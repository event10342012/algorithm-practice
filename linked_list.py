class Node:
    def __init__(self, value: int, next_node=None):
        self.__value = value
        self.__next_node = next_node

    @property
    def value(self):
        return self.__value

    @property
    def next_node(self):
        return self.__next_node


class LinkedList:
    def __init__(self, first: Node = None):
        self.__first = first

    @property
    def first(self):
        return self.__first

    def print_list(self):
        if not self.first:
            raise ValueError('List is empty!')
        current = self.first
        while current is not None:
            print(current)
            current = current.next_node

    def push_back(self, x):
        pass

    def push_front(self, x):
        pass

    def delete(self, x: int):
        pass

    def clear(self):
        pass

    def reverse(self):
        pass
