class Node:
    def __init__(self, value: int, next_node=None):
        self.__value: int = value
        self.next_node: Node = next_node

    @property
    def value(self):
        return self.__value


class LinkedList:
    def __init__(self, head: Node = None):
        self.__head: Node = head

    @property
    def head(self):
        return self.__head

    def print_list(self):
        if not self.head:
            print('List is empty!')
            return

        output = ''
        current = self.head
        while current:
            output += f" {current.value}"
            current = current.next_node
        print(output)

    def push_back(self, x):
        new_node = Node(x)

        if self.head is None:
            self.__head = new_node
            return

        current = self.head
        while current.next_node:
            current = current.next_node

        current.next_node = new_node

    def push_front(self, x):
        new_node = Node(x)
        new_node.next_node = self.__head
        self.__head = new_node

    def insert(self, x: int):
        pass

    def delete(self, x: int):
        if self.head is None:
            print('List is empty')
            return

        previous = None
        current = self.head
        if current.next_node is None:
            if current.value == x:
                del current
                return
            else:
                print(f'{x} not in list')
                return

        if current.value == x:
            self.__head = current.next_node
            del current
            return

        while current.next_node:
            if current.value == x:
                previous.next_node = current.next_node
                del current
                return
            previous = current
            current = current.next_node

        if current.value == x:
            del current
            previous.next_node = None
            return
        print(f'{x} not in list')

    def clear(self):
        while self.head:
            current = self.head
            self.__head = current.next_node
            del current

    def reverse(self):
        if self.head is None or self.head.next_node is None:
            return

        previous = None
        current = self.head
        preceding = current.next_node
        while preceding:
            current.next_node = previous
            previous = current
            current = preceding
            preceding = current.next_node

        current.next_node = previous
        self.__head = current


if __name__ == '__main__':
    node = Node(1)
    linked_list = LinkedList()
    linked_list.print_list()
    linked_list.push_back(1)
    linked_list.push_back(2)
    linked_list.push_front(3)
    linked_list.push_back(4)
    linked_list.push_back(5)
    linked_list.print_list()

    print('reverse')
    linked_list.reverse()
    linked_list.print_list()

    print('delete')
    linked_list.delete(3)
    linked_list.print_list()

    print('clear')
    linked_list.clear()
    linked_list.print_list()
