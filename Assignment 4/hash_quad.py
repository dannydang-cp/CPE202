class Node:
    def __init__(self, val, data):
        self.val = val
        if type(data) == list:
            self.data = data
        else:
            self.data = [data]

    def __repr__(self):
        return "[%s, %s]" % (self.val, self.data)


class HashTable:
    def __init__(self, table_size):
        self.table_size = table_size
        self.hash_table = [None] * table_size
        self.num_items = 0

    def insert(self, key, value=None):
        ''' Inserts an entry into the hash table (using Horner hash function to determine index,
        and quadratic probing to resolve collisions).
        The key is a string (a word) to be entered, and value is any object (e.g. Python List).
        If the key is not already in the table, the key is inserted along with the associated value
        If the key is is in the table, the new value replaces the existing value.
        If load factor is greater than 0.5 after an insertion, hash table size should be increased (doubled + 1).'''
        if type(key) != str:                # Raises a TypeError if the key is not a string value
            raise TypeError("Invalid Token")
        elif type(key) == str:
            node = Node(key, value)         # Creates a node for the key and value
            horn = self.horner_hash(key)    # Finds the index of the key
            col = 0                         # Counter for collision
            insert = False
            index = (horn + col ** 2)
            while insert is False:
                if index >= self.table_size - 1:
                    index -= self.table_size
                    print(index)
                if self.hash_table[index] is None:          # Checks if there is an empty spot for insertion
                    self.hash_table[index] = node
                    self.num_items += 1
                    if self.get_load_factor() > .5:         # Checks the load factor and rehashes the table
                        self.rehash()
                    insert = True
                elif self.hash_table[index] is not None:    # Changes the value or adds 1 to collision
                    if self.hash_table[index].val == key:
                        self.hash_table[index].data.append(value)
                        insert = True
                    else:
                        col += 1
                        index = (horn + col ** 2) % self.table_size
                        print(col)

    def rehash(self):
        new_ts = (self.table_size * 2) + 1
        new_ht = [None] * new_ts
        old_ht = self.hash_table
        self.num_items = 0
        self.hash_table = new_ht
        self.table_size = new_ts
        for i in old_ht:
            if i is not None:
                self.insert(i.val, i.data)

    def horner_hash(self, key):
        ''' Compute and return an integer from 0 to the (size of the hash table) - 1
        Compute the hash value by using Horner’s rule, as described in project specification.'''
        i = 0
        horn = 0
        n = min(8, len(key))
        while i < n:    # Adds up the ASCII Values and multiplies them
            horn += ord(key[i]) * (31 ** (n - 1 - i))
            i += 1
        hashed = horn % self.table_size  # Mods by table size
        return hashed

    def in_table(self, key):
        ''' Returns True if key is in an entry of the hash table, False otherwise.'''
        horn = self.horner_hash(key)
        col = 0
        found = False
        while found is False:
            index = (horn + col ** 2) % self.table_size
            if self.hash_table[index] is None:
                return False
            elif self.hash_table[index].val == key:
                found = True
                return True
            else:
                col += 1

    def get_index(self, key):
        ''' Returns the index of the hash table entry containing the provided key.
        If there is not an entry with the provided key, returns None.'''
        horn = self.horner_hash(key)
        col = 0
        found = False
        while found is False:
            index = (horn + col ** 2) % self.table_size
            if self.hash_table[index] is None:
                return None
            elif self.hash_table[index].val == key:
                found = True
                return index
            else:
                col += 1

    def get_all_keys(self):
        ''' Returns a Python list of all keys in the hash table.'''
        key_lst = []
        for i in self.hash_table:
            if i is not None:
                key_lst.append(i.val)
        return key_lst

    def get_value(self, key):
        ''' Returns the value associated with the key.
        If key is not in hash table, returns None.'''
        horn = self.horner_hash(key)
        col = 0
        found = False
        while found is False:
            index = (horn + col ** 2) % self.table_size
            if self.hash_table[index] is None:
                return None
            elif self.hash_table[index].val == key:
                found = True
                return self.hash_table[index].data
            else:
                col += 1

    def get_num_items(self):
        ''' Returns the number of entries in the table.'''
        return self.num_items

    def get_table_size(self):
        ''' Returns the size of the hash table.'''
        return self.table_size

    def get_load_factor(self):
        ''' Returns the load factor of the hash table (entries / table_size).'''
        return self.num_items / self.table_size


hash = HashTable(3)
hash.insert("hello", 5)
#hash.insert("e", 2)
print(hash.hash_table)

