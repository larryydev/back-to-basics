class Stack:
    def __init__(self):
        self.stack = []

    def add(self, data):
        self.stack.append(data)

    def peek(self):
        return self.stack[-1]
    
    def pop(self):
        return self.stack.pop()
    
    def is_empty(self):
        return len(self.stack) == 0
    

if __name__ == '__main__':
    s = Stack()
    for i in range(6):
        s.add(i)
    
    print(s.peek())

    print(s.pop())


    print()