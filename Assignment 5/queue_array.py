class Queue:
    def __init__(self, capacity):
        self.capacity = capacity
        self.front = 0
        self.rear = 0
        self.queue = [None] * capacity
        self.num_in_queue = 0

    def __repr__(self):
        return "Queue({}, {}, {}, {}, {})".format(self.capacity,
                                                  self.front,
                                                  self.rear,
                                                  self.queue,
                                                  self.num_in_queue)

    def __eq__(self, other):
        return (isinstance(self) == isinstance(other) and
                self.capacity == other.capacity and
                self.front == other.front and
                self.rear == other.rear and
                self.queue == other.queue and
                self.num_in_queue == other.num_in_queue
                )

    def is_empty(self):
        """Returns true if the queue is empty, and False otherwise"""
        return self.num_in_queue == 0

    def is_full(self):
        """Returns True if the queue is full, and False otherwise"""
        return self.num_in_queue == self.capacity

    def enqueue(self, item):
        """Adds the item into the end of the queue"""
        if self.is_full() is True:
            raise IndexError
        self.queue[self.rear] = item  # Makes the rear index the item
        self.rear = (self.rear + 1) % self.capacity  # Moves the rear index to the next one
        self.num_in_queue += 1  # Increase the number of items in the queue by one

    def dequeue(self):
        """Removes and returns the item in front of the queue"""
        if self.is_empty() is True:
            raise IndexError
        temp = self.queue[self.front]  # temp is the number being returned and removed
        self.queue[self.front] = None  # Make the item in the front of queue None
        self.front = (self.front + 1) % self.capacity  # Makes the front index next one
        self.num_in_queue -= 1  # Reduces the number of items in the queue by one
        return temp

    def number_in_queue(self):
        """Returns how many items are in the queue"""
        return self.num_in_queue
