class Node(object):
    """A node that is used by a linked list, it contains data and a pointer to another node."""
    def __init__(self, data=None):
        self.data = data
        self.next = None

    def __repr__(self):
            return 'Node(' + repr(self.data) + ')'


class LinkedList(object):
    """A singly linked list data structure, it contains a string of nodes that store data."""
    def __init__(self, data=None):
        # empty LinkedList
        self.head = None
        self.size = 0
        if data:
            self.head = Node(data)
            self.size = 1

    # String Representation of List
    def __repr__(self):
        string = 'LinkedList('
        data = [item for item in self]
        dataLength = len(self)
        if dataLength == 0:
            return string + ')'
        for i in range(dataLength - 1):
            string += repr(data[i]) + ', '
        return string + repr(data[dataLength - 1]) + ')'

    # Makes the list an iterable
    def __iter__(self):
        self.current = self.head
        return self

    # Used by iterable to implement iteration
    def __next__(self):
        returned = self.current
        if returned is None:
            raise StopIteration()
        else:
            self.current = self.current.next
        return returned.data

    def _node_generator(self):
        current = self.head
        while current is not None:
            yield current
            current = current.next

    def __len__(self):
        return self.size

    def is_empty(self):
        return self.size == 0

    # Creates a node at the beginning of the linked list
    def insert_at_head(self, data):
        # create a new node with the data
        new_node = Node(data)
        new_node.next = self.head
        # reassign head reference
        self.head = new_node
        self.size += 1

    # Returns the data of a node at a given index
    def get_at_index(self, idx):
        if self.is_empty():
            raise ValueError('List is empty')
        current_node = self.head
        for i in range(0, idx):
            current_node = current_node.next
        if current_node is None:
            raise IndexError('Index out of bounds')
        return current_node.data

    def set_at_index(self, data, idx):
        if self.is_empty():
            if idx > 0:
                raise IndexError('Index out of bounds')
            else:
                self.insert_at_head(data)
        current_node = self.head
        for i in range(0, idx):
            current_node = current_node.next
            if current_node is None:
                raise IndexError('Index out of bounds')
        current_node.data = data

    # Removes the first node
    def remove_head(self):
        if self.is_empty():
            raise ValueError('List is empty')
        self.head = self.head.next
        self.size -= 1

    # Removes the specific value in the linked list
    def remove_item(self, value):
        lastNode = self.head
        if value == self.head.data:
            self.remove_head()
            return
        for item in self._node_generator():
            if value == item.data:
                lastNode.next = item.next
                self.size -= 1
                break
            lastNode = item

    def calculate_size(self):
        count = 0
        for node in self._node_generator():
            count += 1
        return count


class HashBrownTable(object):
    """An implementation of a HashTable, stores data with key-value pairs."""
    def __init__(self, array=None):
        self._bucketLength = 8
        self._buckets = [LinkedList() for i in range(0, self._bucketLength)]
        self.size = 0
        if array is not None:
            for key, value in array:
                self.set(key, value)

    def __repr__(self):
        data = self.data()
        dataLength = len(self)
        if dataLength == 0:
            return 'HashTable{}'
        string = ''
        for i in range(0, dataLength - 1):
            string += repr(data[i]) + ", "
        string += repr(data[dataLength - 1])
        # [brian] instead of the above 4 lines you could also write:
        string = ', '.join([repr(datum) for datum in data])
        # In general, python tries very hard to prevent you from needing to
        # keep track of which iteration you're currently on. If you find
        # yourself doing a lot of -1 and +1 math with indices, it's likely
        # an easier way exists.

        return 'HashTable{' + string + '}'

    # [brian] Nice use of magic methods in this file, they're very pythonic and make your code so much
    # easier to read and write.
    def __len__(self):
        return self.size

    # Expands the hash table so there is less chance of a collision
    def _expand(self):
        if self.size / self._bucketLength > 0.7:
            saved = self.data()
            self._bucketLength *= 2
            # keys = self.keys()
            self._buckets = [LinkedList() for i in range(0, self._bucketLength)]
            for savedItem in saved:
                self._buckets[hash(savedItem[0]) % self._bucketLength].insert_at_head(savedItem)

    # Sets the value for a given key.
    def set(self, key, data):
        bucket = self._buckets[hash(key) % self._bucketLength]
        if bucket.is_empty():
            bucket.insert_at_head((key, data))
            self.size += 1
        else:
            for i, pair in enumerate(bucket):
                if pair[0] == key:
                    bucket.set_at_index((key, data), i)
                    return
            bucket.insert_at_head((key, data))
            self.size += 1
            self._expand()

    # Removes the data for a given key.
    def remove_item(self, key):
        self.set(key, None)
        self._buckets[hash(key) % self._bucketLength].remove_item((key, None))
        self.size -= 1

    # Returns the data for a given key.
    def get(self, key):
        for item in self._buckets[hash(key) % self._bucketLength]:
            if item[0] == key:
                return item[1]
        raise KeyError('Key not founds')

    # Returns an array of keys.
    def keys(self):
        keys = []
        for pairsLL in self._buckets:
            for key, data in pairsLL:
                if key is not None:
                    keys.append(key)
        return keys

    # Returns an array of values.
    def values(self):
        vals = []
        for pairsLL in self._buckets:
            for key, value in pairsLL:
                if value is not None:
                    vals.append(value)
        return vals

    # Returns all the data as an array of key-value pairs.
    def data(self):
        data = []
        for pairsLL in self._buckets:
            for key, value in pairsLL:
                if key is not None or value is not None:
                    data.append((key, value))
        return data


def test():
    print('=====LINKED LIST TEST=====')
    testLL = LinkedList()
    print('Empty LL:', testLL)
    testLL.insert_at_head('This')
    print('One Item:', testLL)
    testLL.insert_at_head('is')
    testLL.insert_at_head('backwards')
    testLL.insert_at_head('blank')
    print('Multiple items:', testLL)
    testLL.remove_item('blank')
    print('Removed an item:', testLL)
    print('Value at index 1:', repr(testLL.get_at_index(1)))
    print('Reversed:', [item for item in reversed([item for item in testLL])])
    print('Counted size:', str(testLL.size) + "; Calculated size:", testLL.calculate_size())
    print('=====HASH TABLE TEST=====')
    testHT = HashBrownTable()
    print('Empty hash table:', testHT)
    testHT.set('Key', 7)
    print('Hash table has one element:', testHT)
    testHT.set('OtherKey', 14)
    testHT.set('ThirdKey', 28)
    print('Hash table has three elements:', testHT)
    testHT.set('FourthKey', 56)
    testHT.set('FifthKey', 112)
    testHT.set('SixthKey', 224)
    testHT.set('SeventhKey', 448)
    print('Hash table should have expanded')
    print('Hash table keys:', testHT.keys())
    print('Hash table values:', testHT.values())
    testHT.remove_item('Key')
    print('Hash table removed items:', testHT)
    testHT.remove_item('key')
    print('Hash table should be the same:', testHT)
    testHT.set('OtherKey', 5)
    print('\'OtherKey\' should be different:', testHT)


if __name__ == '__main__':
    test()
