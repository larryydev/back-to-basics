class LNode:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def insert(self, data):
        new_node = LNode(data)

        if not self.head and not self.tail:
            self.head = self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
        
        self.size += 1

    def at(self, index):
        if index < 0 or index >= self.size:
            raise IndexError('index out of range')
        
        if index == 0:
            return self.head.data
        
        if index == self.size-1:
            return self.tail.data
    
        cur = self.head
        for _ in range(index):
            cur = cur.next

        return cur.data

    def remove(self, data):
        cur = self.head
        for i in range(self.size):
            if cur.data == data:
                if cur == self.head:
                    self.remove_first()
                elif cur == self.tail:
                    self.remove_last()
                else:
                    self.remove_at(i)
                return True
        return False

    def remove_first(self):
        if self.size == 1:
            self.head = self.tail = None
        else:
            self.head = self.head.next
            self.head.prev = None

        self.size -= 1

    def remove_at(self, index):
        if index < 0 or index >= self.size:
            raise IndexError('index out of range')
        
        if index == 0:
            self.remove_first()
        elif index == self.size-1:
            self.remove_last()
        else:
            cur = self.head
            for _ in range(index):
                cur = cur.next
            prev = cur.prev
            next_ = cur.next
            del cur

            prev.next = next_
            next_.prev = prev
            self.size -= 1

    def remove_last(self):
        if self.size == 1:
            self.head = self.tail = None
        else:
            self.tail = self.tail.prev
            self.tail.next = None

        self.size -= 1


if __name__ == '__main__':
    l = LinkedList()


    i = [11, 23, 43, 49, 55, 392, 400]

    for n in i:
        l.insert(n)


    l.remove_at(3)

    for i in range(l.size):
        print(l.at(i))

    l.remove_at(0)

    l.remove_at(l.size-1)


    print()
    for i in range(l.size):
        print(l.at(i))
    
