'''
Design a data structure that follows the constraints of a Least Recently Used (LRU) cache.

Implement the LRUCache class:

LRUCache(int capacity) Initialize the LRU cache with positive size capacity.

int get(int key) Return the value of the key if the key exists, otherwise return -1.
void put(int key, int value) Update the value of the key if the key exists. 
Otherwise, add the key-value pair to the cache. 
If the number of keys exceeds the capacity from this operation, evict the least recently used key.

Follow up:
Could you do get and put in O(1) time complexity?

Example 1:

Input
["LRUCache", "put", "put", "get", "put", "get", "put", "get", "get", "get"]
[[2], [1, 1], [2, 2], [1], [3, 3], [2], [4, 4], [1], [3], [4]]
Output
[null, null, null, 1, null, -1, null, -1, 3, 4]

Explanation
LRUCache lRUCache = new LRUCache(2);
lRUCache.put(1, 1); // cache is {1=1}
lRUCache.put(2, 2); // cache is {1=1, 2=2}
lRUCache.get(1);    // return 1
lRUCache.put(3, 3); // LRU key was 2, evicts key 2, cache is {1=1, 3=3}
lRUCache.get(2);    // returns -1 (not found)
lRUCache.put(4, 4); // LRU key was 1, evicts key 1, cache is {4=4, 3=3}
lRUCache.get(1);    // return -1 (not found)
lRUCache.get(3);    // return 3
lRUCache.get(4);    // return 4
'''


class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None


'''
dict = { key : pointer to the node storing the key }
'''


class DoublyLinkedList:
    def __init__(self, capacity):
        self.start = None
        self.end = None
        self.capacity = capacity
        self.length = 0
        self.hash_map = {}

    def remove_last_node(self):
        key_to_delete = self.end.key

        self.end.prev.next = None  # have the second last node's next point to None
        self_end_prev = self.end.prev  # second last node in self_end_prev
        self.end.prev = None
        self.end = self_end_prev

        # delete the key from the hashMap
        del self.hash_map[key_to_delete]

        self.length -= 1

    def move_last_node_to_front(self):
        # start --> Node1 <--> Node2 <--> Node3 <-- end

        last_node = self.end
        self.end = self.end.prev

        self.end.next = None
        last_node.prev = None

        last_node.next = self.start
        last_node.next.prev = last_node
        self.start = last_node

    def put(self, key, value):
        # if key exists in hash_map, then update the value and do nothing
        if key in self.hash_map:
            pointer_to_node = self.hash_map[key]
            pointer_to_node.value = value

            if not pointer_to_node.prev:  # start node
                return

            if not pointer_to_node.next:  # end node
                if self.length > 1:
                    self.move_last_node_to_front()

            else:
                if self.length > 1:
                    self.move_middle_node_to_front(pointer_to_node)

            return

        if self.length == 0:
            new_node = Node(key, value)

            self.start = new_node
            self.end = new_node

            self.hash_map[key] = self.start

        else:
            # insert at the very beginning in order to implement LRU

            # start --> Node1 <--> Node2 <--> Node3 <-- end

            new_node = Node(key, value)

            new_node.next = self.start
            new_node.next.prev = new_node

            self.start = new_node

            self.hash_map[key] = self.start

        self.length += 1

        # check if we exceeded the capacity with the new insert
        if self.length > self.capacity:
            self.remove_last_node()

    def move_middle_node_to_front(self, pointer_to_node):
        next_of_pointer_to_node = pointer_to_node.next
        prev_of_pointer_to_node = pointer_to_node.prev

        pointer_to_node.next.prev = prev_of_pointer_to_node
        pointer_to_node.prev.next = next_of_pointer_to_node

        pointer_to_node.next = self.start
        pointer_to_node.next.prev = pointer_to_node
        pointer_to_node.prev = None
        self.start = pointer_to_node

    def get(self, key):
        if key not in self.hash_map:
            return -1

        pointer_to_node = self.hash_map[key]
        value_to_return = pointer_to_node.value

        if self.length == 1 or self.start == pointer_to_node:
            return value_to_return

        # move the accessed key to the very beginning of the list
        if not pointer_to_node.next:  # end node
            self.move_last_node_to_front()
            return value_to_return

        self.move_middle_node_to_front(pointer_to_node)

        return value_to_return

    def print_linked_list(self):
        current_node = self.start

        for _ in range(self.length):
            print(f"key = {current_node.key}, value = {current_node.value}")
            current_node = current_node.next

        print("\n-----------------------------\n")


dbb = DoublyLinkedList(2)

# ["LRUCache","put","put","get","put","put","get"]
# [[2]       ,[2,1],[2,2],[2]  ,[1,1],[4,1],[2]]

# ["LRUCache","get","put","get","put","put","get","get"]
# [[2]       ,[2]  ,[2,6],[1]  ,[1,5],[1,2],[1]  ,[2]]

print(dbb.get('two'))
dbb.print_linked_list()

dbb.put('two', 6)
dbb.print_linked_list()

print(dbb.get('one'))
dbb.print_linked_list()

dbb.put('one', 5)
dbb.print_linked_list()

dbb.put('one', 2)
dbb.print_linked_list()

print(dbb.get("one"))
dbb.print_linked_list()

print(dbb.get('two'))
dbb.print_linked_list()
