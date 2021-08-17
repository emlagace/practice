# document
class Item:
    """A class to represent one item in a doubly linked list.

    Attributes
    ----------
    key : str
        the key of the item
    value: str
        the value of the item
    previous_item: Item
        a link to the previous item
    next_item: Item
        a link to the next item
    """

    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.previous_item = None
        self.next_item = None


class DoublyLinkedList:
    """A class to represent a doubly linked list of items.

    Attributes
    ----------
    head : Item
        the first item
    tail: Item
        the last item
    """

    def __init__(self):
        self.head = None
        self.tail = None

    def add(self, item):
        """Add an item to the head"""
        if self.head:
            self.head.previous_item = item
            item.next_item = self.head
            item.previous_item = None
        else:
            # very first item added is both tail and head
            self.tail = item
        self.head = item

    def update(self, item):
        """Update an existing item and move it to the head"""
        previous_item = item.previous_item
        next_item = item.next_item

        if previous_item:
            # item is not already currently the head
            previous_item.next_item = next_item
            if next_item:
                # item is also not the tail
                next_item.previous_item = previous_item
            else:
                # item is the tail, set a new tail
                self.tail = previous_item

            self.add(item)

    def removeTail(self):
        """Remove the tail item"""
        if self.tail:
            previous_item = self.tail.previous_item
            if previous_item:
                previous_item.next_item = None
                self.tail = previous_item
            else:
                # there is only one item in the list
                self.clear()

    def delete(self, item):
        "Delete an existing item"
        previous_item = item.previous_item
        next_item = item.next_item

        if item is self.head:
            if next_item:
                next_item.previous_item = None
                self.head = next_item
            else:
                self.head = None

        if item is self.tail:
            if previous_item:
                previous_item.next_item = None
                self.tail = previous_item
            else:
                self.tail = None

        if previous_item and next_item:
            #item is in the middle
            previous_item.next_item = next_item
            next_item.previous_item = previous_item

    def clear(self):
        "Clear all the items in the list"
        self.head = None
        self.tail = None

class LRUCache:
    """An impelementation of a Least Recently Used Cache.

    Attributes
    ----------
    max_size : int
        the maximum capacity of the cache
    dictionary: dictionary
        a dictionary containing the key value pairs of items in the cache
    doubly_linked_list: DoublyLinkedList
        a doubly linked list containing the items of the cache
    """

    def __init__(self, max_size):
        max_size = int(max_size)
        assert (max_size > 0), "Max capacity must be greater than zero"
        self.max_size = max_size
        self.dictionary = {}
        self.doubly_linked_list = DoublyLinkedList()

    def put(self, key, value):
        """Put a key value pair into the cache.

        Parameters:
        key (string): the cache item key
        value (string): the cach item value
        """
        if key in self.dictionary:
            # key already exists, update it
            self.dictionary[key].value = value
            self.doubly_linked_list.update(self.dictionary[key])
        else:
            # this is a new key value pair
            if len(self.dictionary) == self.max_size:
                #it will exceed max capacity, remove tail first
                self.dictionary.pop(self.doubly_linked_list.tail.key)
                self.doubly_linked_list.removeTail()
            item = Item(key, value)
            self.doubly_linked_list.add(item)
            self.dictionary[key] = item

    def get(self, key):
        """Get a value from the cache by its key.

        Parameter:
        key (string): the cache item key

        Returns:
            value (string): the corresponding cache item value
        """
        if key in self.dictionary:
            item = self.dictionary[key]
            self.doubly_linked_list.update(item)
            return item.value
        return None
    
    def delete(self, key):
        """Delete a value from the cache by its key.

        Parameter:
        key (string): the key of the cache item to delete
        """
        if key in self.dictionary:
            item = self.dictionary[key]
            self.doubly_linked_list.delete(item)
            self.dictionary.pop(key)

    def reset(self):
        """Reset the cache to be empty."""
        self.dictionary = {}
        self.doubly_linked_list.clear()

    def show(self):
        """Print the contents of the cache."""
        print("------------------")
        print("Current LRU Cache:")
        item = self.doubly_linked_list.head
        while item:
            print(item.key, item.value)
            item =  item.next_item
        print("Max capacity = ", self.max_size)

def main():
    max_capacity = input("Enter LRU Cache max capacity: ")
    lru_cache = LRUCache(max_capacity)
    lru_cache.show()

    is_continue = True
    while is_continue:
        command = input("Enter command (put/get/delete/reset/exit): ")
        if command == "put":
            key = input("Enter key: ")
            value = input("Enter value: ")
            lru_cache.put(key, value)
        elif command == "get":
            key = input("Enter key: ")
            print(lru_cache.get(key))
        elif command == "delete":
            key = input("Enter key: ")
            lru_cache.delete(key)
        elif command == "reset":
            lru_cache.reset()
        elif command == "exit":
            is_continue = False
        lru_cache.show()

if __name__ == '__main__':
    main()
