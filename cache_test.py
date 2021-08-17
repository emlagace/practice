import unittest
import cache

class LRUCacheTest(unittest.TestCase):

    def test_initializes_cache_item(self):
        key = 123
        value = "a value"
        item = self.createItem(key, value)
        self.assertEqual(key, item.key)
        self.assertEqual(value, item.value)
        self.assertTrue(item.next_item is None)
        self.assertTrue(item.previous_item is None)

    def test_initializes_cache_doubly_linked_list(self):
        linked_list = cache.DoublyLinkedList()
        self.assertTrue(linked_list.head is None)
        self.assertTrue(linked_list.tail is None)

    def test_first_item_added_to_doubly_linked_list_is_head_and_tail(self):
        item = self.createItem(1, "value")
        linked_list = cache.DoublyLinkedList()
        linked_list.add(item)
        self.assertEqual(item, linked_list.head)
        self.assertEqual(item, linked_list.tail)
        self.assertTrue(linked_list.head.previous_item is None)
        self.assertTrue(linked_list.head.next_item is None)

    def test_adds_many_items_to_doubly_linked_list_in_order(self):
        item1, item2, item3 = self.createTestItems()
        linked_list = cache.DoublyLinkedList()
        linked_list.add(item1)
        linked_list.add(item2)
        linked_list.add(item3)

        self.assertTrue(item1.next_item is None)
        self.assertEqual(item2, item1.previous_item)
        self.assertEqual(item1, item2.next_item)
        self.assertEqual(item3, item2.previous_item)
        self.assertEqual(item2, item3.next_item)
        self.assertTrue(item3.previous_item is None)
    
    def test_most_recently_added_item_to_doubly_linked_list_is_head(self):
        item1, item2, item3 = self.createTestItems()
        linked_list = cache.DoublyLinkedList()

        linked_list.add(item1)
        self.assertEqual(item1, linked_list.head)
        linked_list.add(item2)
        self.assertEqual(item2, linked_list.head)
        linked_list.add(item3)
        self.assertEqual(item3, linked_list.head)

    def test_least_recently_added_item_to_doubly_linked_list_is_tail(self):
        item1, item2, item3 = self.createTestItems()
        linked_list = cache.DoublyLinkedList()

        linked_list.add(item1)
        self.assertEqual(item1, linked_list.tail)
        linked_list.add(item2)
        self.assertEqual(item1, linked_list.tail)
        linked_list.add(item3)
        self.assertEqual(item1, linked_list.tail)

    def test_updates_head_item_in_doubly_linked_list(self):
        tail_item, middle_item, head_item = self.createTestItems()
        linked_list = cache.DoublyLinkedList()
        linked_list.add(tail_item)
        linked_list.add(middle_item)
        linked_list.add(head_item)

        linked_list.update(head_item)

        self.assertEqual(head_item, linked_list.head)
        self.assertTrue(head_item.previous_item is None)
        self.assertEqual(middle_item, head_item.next_item)
        self.assertEqual(head_item, middle_item.previous_item)        
        self.assertEqual(tail_item, middle_item.next_item)    
        self.assertEqual(middle_item, tail_item.previous_item)
        self.assertTrue(tail_item.next_item is None)
        self.assertEqual(tail_item, linked_list.tail)

    def test_updates_middle_item_in_doubly_linked_list_to_head(self):
        tail_item, middle_item, head_item = self.createTestItems()
        linked_list = cache.DoublyLinkedList()
        linked_list.add(tail_item)
        linked_list.add(middle_item)
        linked_list.add(head_item)

        linked_list.update(middle_item)

        self.assertEqual(middle_item, linked_list.head)
        self.assertTrue(middle_item.previous_item is None)
        self.assertEqual(head_item, middle_item.next_item)
        self.assertEqual(middle_item, head_item.previous_item)        
        self.assertEqual(tail_item, head_item.next_item)    
        self.assertEqual(head_item, tail_item.previous_item)
        self.assertTrue(tail_item.next_item is None)
        self.assertEqual(tail_item, linked_list.tail)

    def test_updates_tail_item_in_doubly_linked_list_to_head(self):
        tail_item, middle_item, head_item = self.createTestItems()
        linked_list = cache.DoublyLinkedList()
        linked_list.add(tail_item)
        linked_list.add(middle_item)
        linked_list.add(head_item)

        linked_list.update(tail_item)

        self.assertEqual(tail_item, linked_list.head)
        self.assertTrue(tail_item.previous_item is None)
        self.assertEqual(head_item, tail_item.next_item)
        self.assertEqual(tail_item, head_item.previous_item)
        self.assertEqual(middle_item, head_item.next_item)
        self.assertEqual(head_item, middle_item.previous_item)        
        self.assertTrue(middle_item.next_item is None)
        self.assertEqual(middle_item, linked_list.tail)

    def test_updates_item_when_item_is_only_item_in_doubly_linked_list(self):
        item = self.createItem(10, "test")
        linked_list = cache.DoublyLinkedList()
        linked_list.add(item)

        linked_list.update(item)

        self.assertEqual(item, linked_list.head)
        self.assertTrue(item.previous_item is None)
        self.assertEqual(item, linked_list.tail)
        self.assertTrue(item.next_item is None)

    def test_removes_tail_from_doubly_linked_list_with_one_item(self):
        item = self.createItem(99, "a value")
        linked_list = cache.DoublyLinkedList()
        linked_list.add(item)

        linked_list.removeTail()

        self.assertTrue(linked_list.head is None)
        self.assertTrue(linked_list.tail is None)

    def test_removes_tail_item_from_doubly_linked_list_with_many_items(self):
        tail_item, middle_item, head_item = self.createTestItems()
        linked_list = cache.DoublyLinkedList()
        linked_list.add(tail_item)
        linked_list.add(middle_item)
        linked_list.add(head_item)

        linked_list.removeTail()

        self.assertEqual(middle_item, linked_list.tail)
        self.assertTrue(middle_item.next_item is None)

    def test_deletes_item_from_doubly_linked_list_with_one_item(self):
        item = self.createItem(99, "a value")
        linked_list = cache.DoublyLinkedList()
        linked_list.add(item)

        linked_list.delete(item)

        self.assertTrue(linked_list.head is None)
        self.assertTrue(linked_list.tail is None)

    def test_deletes_head_item_from_doubly_linked_list_with_many_items(self):
        tail_item, middle_item, head_item = self.createTestItems()
        linked_list = cache.DoublyLinkedList()
        linked_list.add(tail_item)
        linked_list.add(middle_item)
        linked_list.add(head_item)

        linked_list.delete(head_item)

        self.assertEqual(middle_item, linked_list.head)
        self.assertTrue(middle_item.previous_item is None)
        self.assertEqual(tail_item, middle_item.next_item)

    def test_deletes_middle_item_from_doubly_linked_list_with_many_items(self):
        tail_item, middle_item, head_item = self.createTestItems()
        linked_list = cache.DoublyLinkedList()
        linked_list.add(tail_item)
        linked_list.add(middle_item)
        linked_list.add(head_item)

        linked_list.delete(middle_item)

        self.assertEqual(head_item, linked_list.head)
        self.assertEqual(tail_item, head_item.next_item)
        self.assertEqual(head_item, tail_item.previous_item)
        self.assertEqual(tail_item, linked_list.tail)

    def test_deletes_tail_item_from_doubly_linked_list_with_many_items(self):
        tail_item, middle_item, head_item = self.createTestItems()
        linked_list = cache.DoublyLinkedList()
        linked_list.add(tail_item)
        linked_list.add(middle_item)
        linked_list.add(head_item)

        linked_list.delete(tail_item)

        self.assertEqual(middle_item, linked_list.tail)
        self.assertTrue(middle_item.next_item is None)
        self.assertEqual(head_item, middle_item.previous_item)

    def test_removes_tail_from_doubly_linked_list_with_no_item(self):
        linked_list = cache.DoublyLinkedList()

        linked_list.removeTail()

        self.assertTrue(linked_list.head is None)
        self.assertTrue(linked_list.tail is None)

    def test_clears_doubly_linked_list_with_no_items(self):
        linked_list = cache.DoublyLinkedList()

        linked_list.clear()

        self.assertTrue(linked_list.head is None)
        self.assertTrue(linked_list.tail is None)

    def test_clears_doubly_linked_list_with_one_item(self):
        linked_list = cache.DoublyLinkedList()
        linked_list.add(self.createItem(1, "test"))

        linked_list.clear()

        self.assertTrue(linked_list.head is None)
        self.assertTrue(linked_list.tail is None)

    def test_clears_doubly_linked_list_with_many_items(self):
        linked_list = cache.DoublyLinkedList()
        item1, item2, item3 = self.createTestItems()
        linked_list.add(item1)
        linked_list.add(item2)
        linked_list.add(item3)

        linked_list.clear()

        self.assertTrue(linked_list.head is None)
        self.assertTrue(linked_list.tail is None)

    def test_initializes_lru_cache_with_max_size(self):
        lru_cache = cache.LRUCache(1)
        self.assertEqual(1, lru_cache.max_size)

        lru_cache = cache.LRUCache("5")
        self.assertEqual(5, lru_cache.max_size)

    def test_requires_max_size_greater_than_zero(self):
        self.assertRaises(AssertionError, cache.LRUCache, 0)
        self.assertRaises(AssertionError, cache.LRUCache, "0")

    def test_puts_a_key_value_pair_in_lru_cache(self):
        lru_cache = cache.LRUCache(5)
        key = 123
        value = "a value"
        
        lru_cache.put(key, value)

        self.assertEqual(key, lru_cache.doubly_linked_list.head.key)
        self.assertEqual(value, lru_cache.doubly_linked_list.head.value)
        self.assertEqual(1, len(lru_cache.dictionary))
        self.assertTrue(key in lru_cache.dictionary)
        self.assertEqual(value, lru_cache.dictionary[key].value)

    def test_puts_many_key_value_pairs_in_lru_cache(self):
        lru_cache = cache.LRUCache(5)
        
        lru_cache.put(1, "value1")
        lru_cache.put(2, "value2")
        lru_cache.put(3, "value3")

        self.assertEqual(3, lru_cache.doubly_linked_list.head.key)
        self.assertEqual("value3", lru_cache.doubly_linked_list.head.value)
        self.assertEqual(3, len(lru_cache.dictionary))
        self.assertTrue(1 in lru_cache.dictionary)
        self.assertTrue(2 in lru_cache.dictionary)
        self.assertTrue(2 in lru_cache.dictionary)

    def test_putting_new_key_into_lru_cache_at_max_size_bumps_lru_item(self):
        lru_cache = cache.LRUCache(2)
        
        lru_cache.put(1, "value1")
        lru_cache.put(2, "value2")
        lru_cache.put(3, "value3")

        self.assertEqual(2, len(lru_cache.dictionary))
        self.assertTrue(3 in lru_cache.dictionary)
        self.assertTrue(2 in lru_cache.dictionary)
        self.assertFalse(1 in lru_cache.dictionary)
    
    def test_putting_existing_key_into_lru_cache_updates_item_in_cache(self):
        lru_cache = cache.LRUCache(5)
        lru_cache.put(1, "value1")
        lru_cache.put(2, "value2")
        lru_cache.put(3, "value3")

        new_value = "different value"
        lru_cache.put(1, new_value)

        self.assertEqual(3, len(lru_cache.dictionary))
        self.assertEqual(new_value, lru_cache.dictionary[1].value)
        self.assertEqual(1, lru_cache.doubly_linked_list.head.key)
        self.assertEqual(new_value, lru_cache.doubly_linked_list.head.value)
        self.assertEqual(2, lru_cache.doubly_linked_list.tail.key)
        self.assertEqual("value2", lru_cache.doubly_linked_list.tail.value)

    def test_gets_value_of_key_from_lru_cache(self):
        lru_cache = cache.LRUCache(5)
        lru_cache.put(1, "value1")
        lru_cache.put(2, "value2")
        lru_cache.put(3, "value3")

        self.assertEqual("value1", lru_cache.get(1))
        self.assertEqual("value2", lru_cache.get(2))
        self.assertEqual("value3", lru_cache.get(3))

    def test_getting_value_of_key_from_lru_cache_updates_item_to_head(self):
        lru_cache = cache.LRUCache(5)
        lru_cache.put(1, "value1")
        lru_cache.put(2, "value2")
        lru_cache.put(3, "value3")

        lru_cache.get(1)
        self.assertEqual(1, lru_cache.doubly_linked_list.head.key)

        lru_cache.get(3)
        self.assertEqual(3, lru_cache.doubly_linked_list.head.key)

        lru_cache.get(2)
        self.assertEqual(2, lru_cache.doubly_linked_list.head.key)

    def test_gets_none_value_from_lru_cache_when_key_does_not_exist(self):
        lru_cache = cache.LRUCache(3)
        self.assertEqual(None, lru_cache.get(1))
        lru_cache.put(1, "value1")
        lru_cache.put(2, "value2")
        lru_cache.put(3, "value3")
        self.assertEqual(None, lru_cache.get(4))

    def test_deletes_by_key_from_lru_cache_when_cache_has_one_item(self):
        lru_cache = cache.LRUCache(3)
        lru_cache.put(1, "value1")

        lru_cache.delete(1)

        self.assertEqual(0, len(lru_cache.dictionary))
        self.assertTrue(lru_cache.doubly_linked_list.head is None)
        self.assertTrue(lru_cache.doubly_linked_list.tail is None)

    def test_attempting_to_delete_a_key_from_empty_lru_cache_is_no_op(self):
        lru_cache = cache.LRUCache(3)

        lru_cache.delete(1)

        self.assertEqual(0, len(lru_cache.dictionary))

    def test_attempting_to_delete_a_key_from_lru_cache_that_does_not_exist_is_no_op(self):
        lru_cache = cache.LRUCache(2)
        lru_cache.put(1, "value1")
        lru_cache.put(2, "value2")

        lru_cache.delete(333)

        self.assertEqual(2, len(lru_cache.dictionary))
    
    def test_resets_lru_cache_with_one_item(self):
        lru_cache = cache.LRUCache(5)
        lru_cache.put(1, "value1")

        lru_cache.reset()

        self.assertEqual(5, lru_cache.max_size)
        self.assertEqual(0, len(lru_cache.dictionary))
        self.assertTrue(lru_cache.doubly_linked_list.head is None)
        self.assertTrue(lru_cache.doubly_linked_list.tail is None)

    def test_resets_lru_cache_with_no_items(self):
        lru_cache = cache.LRUCache(5)

        lru_cache.reset()

        self.assertEqual(5, lru_cache.max_size)
        self.assertEqual(0, len(lru_cache.dictionary))
        self.assertTrue(lru_cache.doubly_linked_list.head is None)
        self.assertTrue(lru_cache.doubly_linked_list.tail is None)

    def test_resets_lru_cache_with_many_items(self):
        lru_cache = cache.LRUCache(5)
        lru_cache.put(1, "value1")
        lru_cache.put(2, "value2")
        lru_cache.put(3, "value3")

        lru_cache.reset()

        self.assertEqual(5, lru_cache.max_size)
        self.assertEqual(0, len(lru_cache.dictionary))
        self.assertTrue(lru_cache.doubly_linked_list.head is None)
        self.assertTrue(lru_cache.doubly_linked_list.tail is None)

    def createTestItems(self):
        item1 = self.createItem(11, "value11")
        item2 = self.createItem(22, "value22")
        item3 = self.createItem(33, "value33")
        return item1, item2, item3

    def createItem(self, key, value):
        return cache.Item(key, value)

