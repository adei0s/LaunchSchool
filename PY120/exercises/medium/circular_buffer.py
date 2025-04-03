class CircularBuffer:
    def __init__(self, size):
        self._size = size
        self._buffer = [None]*size
        self._current_idx = 0
        self._oldest = 0
        
    # put method that adds an object to the buffer    
    def put(self, item):
        if self._buffer[self._current_idx]:
            self._oldest = (self._oldest + 1) % self._size
        self._buffer[self._current_idx] = item
        self._current_idx = (self._current_idx + 1) % self._size
        
    # get to remove(and return) the oldest object in the buffer, return None if empty
    def get(self):
        output = self._buffer[self._oldest]
        if output:
            self._buffer[self._oldest] = None
            self._oldest = (self._oldest + 1) % self._size
        return output

buffer = CircularBuffer(3)

print(buffer.get() is None)          # True

buffer.put(1)
buffer.put(2)
print(buffer.get() == 1)             # True

# buffer.put(3)
# buffer.put(4)
# print(buffer.get() == 2)             # True

# buffer.put(5)
# buffer.put(6)
# buffer.put(7)
# print(buffer.get() == 5)             # True
# print(buffer.get() == 6)             # True
# print(buffer.get() == 7)             # True
# print(buffer.get() is None)          # True

# buffer2 = CircularBuffer(4)

# print(buffer2.get() is None)         # True

# buffer2.put(1)
# buffer2.put(2)
# print(buffer2.get() == 1)            # True

# buffer2.put(3)
# buffer2.put(4)
# print(buffer2.get() == 2)            # True

# buffer2.put(5)
# buffer2.put(6)
# buffer2.put(7)
# print(buffer2.get() == 4)            # True
# print(buffer2.get() == 5)            # True
# print(buffer2.get() == 6)            # True
# print(buffer2.get() == 7)            # True
# print(buffer2.get() is None)         # True