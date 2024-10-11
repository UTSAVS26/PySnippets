class Queue:

    def __init__(self, k):
        self.k = k
        self.queue = [None] * k
        self.head = self.tail = -1

    # Insert an element into the queue
    def enqueue(self, data):
        if (self.tail + 1) % self.k == self.head:  # Corrected condition for full queue
            print("The queue is full\n")
        else:
            self.tail = (self.tail + 1) % self.k
            self.queue[self.tail] = data
            if self.head == -1:  # If queue was empty
                self.head = 0

    # Delete an element from the queue
    def dequeue(self):
        if self.head == -1:  # If queue is empty
            print("The queue is empty\n")
            return None
        else:
            temp = self.queue[self.head]
            if self.head == self.tail:  # Queue becomes empty after this dequeue
                self.head = self.tail = -1
            else:
                self.head = (self.head + 1) % self.k
            return temp

    def printQueue(self):
        if self.head == -1:
            print("No element in the queue")
        else:
            i = self.head
            while True:
                print(self.queue[i], end=" ")
                if i == self.tail:
                    break
                i = (i + 1) % self.k
            print()

# Your Queue object will be instantiated and called as such:
obj = Queue(5)  # Pass the size of the queue as an argument
obj.enqueue(1)
obj.enqueue(2)
obj.enqueue(3)
obj.enqueue(4)
obj.enqueue(5)
print("Initial queue")
obj.printQueue()

obj.dequeue()
print("After removing an element from the queue")
obj.printQueue()
