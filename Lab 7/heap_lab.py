class MaxHeap:

    def __init__(self, capacity=50):
        """Constructor creating an empty heap with default capacity = 50 but allows heaps of other capacities to be created."""
        self.heap = [None]*(capacity+1)     # index 0 not used for heap
        self.num_items = 0                       # empty heap
        self.capacity = capacity

    def enqueue(self, item):
        """inserts "item" into the heap
        Raises IndexError if there is no room in the heap"""
        if self.num_items < self.capacity:
            self.heap.append(item)
            self.num_items += 1
            self.perc_up(self.num_items)
            return True
        else:
            return False

    def peek(self):
        """returns root of heap (highest priority) without changing the heap
        Raises IndexError if the heap is empty"""
        if self.num_items == 0:
            raise IndexError
        else:
            return self.heap[1]

    def dequeue(self):
        """returns item at root (highest priority) - removes it from the heap and restores the heap property
           Raises IndexError if the heap is empty"""
        if self.num_items == 0:
            raise IndexError
        else:
            root = self.heap[1]
            self.heap[1] = self.heap[self.num_items]     # Swaps the root and last element
            self.heap.pop()                         # Removes the last element which is now the root
            self.num_items -= 1                     # Reduces num_items by 1
            self.perc_down(1)                       # Executes the perc_down function to fix heap
            return root                             # Returns the value of the root

    def contents(self):
        """returns a list of contents of the heap in the order it is stored internal to the heap.
        (This may be useful for in testing your implementation.)
        If heap is empty, returns empty list []"""
        return self.heap

    def build_heap(self, alist):
        """Discards the items in the current heap and builds a heap from
        the items in alist using the bottom up method.
        If the capacity of the current heap is less than the number of
        items in alist, the capacity of the heap will be increased to accommodate the items in alist"""

        i = len(alist) // 2             # sets the value of i to be the middle of the heap
        self.num_items = len(alist)     # sets num_items of heap to be the size of the inserted list

        # increase the capacity of the heap if the len is bigger
        if self.num_items > self.capacity:
            return False
        else:
            self.heap = [0] + alist[:]  # creates the heap that contains the list
            while i > 0:                # while loop iterates until i becomes zero
                self.perc_down(i)
                i -= 1
            return True

    def is_empty(self):
        """returns True if the heap is empty, false otherwise"""
        return self.num_items == 0

    def is_full(self):
        """returns True if the heap is full, false otherwise"""
        return self.num_items == self.capacity

    def capacity(self):
        """This is the maximum number of a entries the heap can hold, which is
        1 less than the number of entries that the array allocated to hold the heap can hold"""
        return self.capacity
    
    def size(self):
        """the actual number of elements in the heap, not the capacity"""
        return self.num_items

    def perc_down(self,i):
        """where the parameter i is an index in the heap and perc_down moves the element stored
        at that location to its proper place in the heap rearranging elements as it goes."""

        while (i * 2) <= self.num_items:    # runs until the left child of i is greater than num_items
            if i * 2 + 1 > self.num_items:  # if left child of i is greater than num_items
                mc = i * 2                  # max child equal left child of i
            else:
                # if value of left child of i is greater than value of right child of i
                if self.heap[i * 2] > self.heap[i * 2 + 1]:
                    mc = i * 2              # mc equal left child of i
                else:
                    mc = i * 2 + 1          # mc equal right child of i
            # if value of i is less than value of mc
            if self.heap[i] < self.heap[mc]:
                self.heap[i], self.heap[mc] = self.heap[mc], self.heap[i]   # swap the values of i and mc
            i = mc     # new i will be the index of mc

    def perc_up(self, i):
        """where the parameter i is an index in the heap and perc_up moves the element stored
        at that location to its proper place in the heap rearranging elements as it goes."""
        while (i // 2) > 0:     # Iterates until parent of i is zero
            if self.heap[i] > self.heap[i // 2]:    # if value of i is greater than value of it's parent
                self.heap[i], self.heap[i // 2] = self.heap[i // 2], self.heap[i]  # swap values of i and it's parent
            i = i // 2  # new i will be the index of it's parent

    def heap_sort_ascending(self, alist):
        """perform heap sort on input alist in ascending order
        This method will discard the current contents of the heap, build a new heap using
        the items in alist, and mutate alist to put the items in ascending order"""
        heap = MaxHeap()
        heap.build_heap(alist)
        length = len(alist)
        ascending = [0] * (length + 1)
        for i in range(length):
            val = heap.dequeue()            #  Sets val to be equal to the max of the heap and remove it from the heap
            ascending[length - i] = val        # Adds val to the last index in the list
        return ascending
