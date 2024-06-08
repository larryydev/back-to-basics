class Queue_:
    def __init__(self) -> None:
        self.queue = []

    def enqueue(self, data):
        self.queue.append(data)

    def dequeue(self):
        return self.queue.pop(0)
    
    def is_empty(self):
        return len(self.queue) == 0
    

if __name__ == '__main__':
    q = Queue_()

    print(q.is_empty())

    num_ele = 6

    for i in range(num_ele):
        q.enqueue(i)
    
    print(q.is_empty())
    
    for i in range(num_ele):
        q.dequeue()

    
    print(q.is_empty())
