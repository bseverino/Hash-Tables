class HashTableEntry:
    """
    Hash Table entry, as a linked list node.
    """

    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

class HashLinkedList:
    def __init__(self, head=None):
        self.head = head

    def add(self, key, value):
        if self.head is None:
            self.head = HashTableEntry(key, value)
        elif self.head.key == key:
            self.head.value = value
            return
        else:
            current_node = self.head
            while current_node.next is not None:
                if current_node.next.key == key:
                    current_node.next.value = value
                    return
                current_node = current_node.next
            current_node.next = HashTableEntry(key, value)
    
    def get(self, key):
        current_node = self.head
        while current_node is not None:
            if current_node.key == key:
                return current_node.value
            current_node = current_node.next
        return None
    
    def delete(self, key):
        current_node = self.head
        if current_node.key == key:
            self.head = current_node.next
            return True
        prev_node = None
        while current_node is not None:
            if current_node.key == key:
                prev_node.next = current_node.next
                current_node.next = None
                return True
            prev_node = current_node
            current_node = current_node.next
        return False
        

class HashTable:
    """
    A hash table that with `capacity` buckets
    that accepts string keys

    Implement this.
    """
    def __init__(self, capacity):
        self.capacity = capacity
        self.size = 0
        self.storage = [None] * capacity

    def fnv1(self, key):
        """
        FNV-1 64-bit hash function

        Implement this, and/or DJB2.
        """
        fnv_offset_basis = 0xcbf29ce484222325
        fnv_prime = 0x100000001b3
        fnv_size = 2**64

        fnv_hash = fnv_offset_basis

        for char in key:
            fnv_hash = (fnv_hash * fnv_prime) % fnv_size
            fnv_hash = fnv_hash ^ ord(char)
        
        return fnv_hash
        

    def djb2(self, key):
        """
        DJB2 32-bit hash function

        Implement this, and/or FNV-1.
        """
        djb_hash = 5381

        for char in key:
            djb_hash = ((djb_hash * 33) + ord(char))

        return djb_hash


    def hash_index(self, key):
        """
        Take an arbitrary key and return a valid integer index
        between within the storage capacity of the hash table.
        """
        # return self.fnv1(key) % self.capacity
        return self.djb2(key) % self.capacity

    def put(self, key, value):
        """
        Store the value with the given key.

        Hash collisions should be handled with Linked List Chaining.

        Implement this.
        """
        load = self.load_factor()
        if load > 0.7 :
            self.resize(self.capacity * 2)
                   
        index = self.hash_index(key)
        if self.storage[index] is not None:
            self.storage[index].add(key, value)
        else:
            self.storage[index] = HashLinkedList(HashTableEntry(key, value))
        self.size += 1
        

    def delete(self, key):
        """
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Implement this.
        """
        load = self.load_factor()
        if load < 0.2:
            if self.capacity // 2 >= 128:
                self.resize(self.capacity // 2)

        index = self.hash_index(key)
        if self.storage[index] is None:
            print('Key not found')
        else:
            response = self.storage[index].delete(key)
            if response is True:
                self.size -= 1
            else:
                print('Key not found')

    def get(self, key):
        """
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Implement this.
        """        
        index = self.hash_index(key)
        if self.storage[index] is None:
            print('Key not found')
        else:
            return self.storage[index].get(key)
    
    def load_factor(self):
        return self.size / self.capacity

    def for_each(self, cb):
        for i in self.storage:
            if i:
                i.for_each(cb)
    
    def rehash(self, key, value, target):
        index = self.hash_index(key)
        if target[index] is not None:
            target[index].add(key, value)
        else:
            target[index] = HashLinkedList(HashTableEntry(key, value))

    def resize(self, size):
        """
        Doubles the capacity of the hash table and
        rehash all key/value pairs.

        Implement this.
        """
        self.capacity = size

        new_storage = [None] * self.capacity

        for i in self.storage:
            if i:
                current_node = i.head
                while current_node is not None:
                    self.rehash(current_node.key, current_node.value, new_storage)
                    current_node = current_node.next

        self.storage = new_storage
        print(f'Resized to {size}')


if __name__ == "__main__":
    ht = HashTable(2)

    ht.put("line_1", "Tiny hash table")
    ht.put("line_2", "Filled beyond capacity")
    ht.put("line_3", "Linked list saves the day!")

    print("")

    # Test storing beyond capacity
    print(ht.get("line_1"))
    print(ht.get("line_2"))
    print(ht.get("line_3"))

    # Test resizing
    old_capacity = len(ht.storage)
    ht.resize(6)
    new_capacity = len(ht.storage)

    print(f"\nResized from {old_capacity} to {new_capacity}.\n")

    # Test if data intact after resizing
    print(ht.get("line_1"))
    print(ht.get("line_2"))
    print(ht.get("line_3"))

    print("")
