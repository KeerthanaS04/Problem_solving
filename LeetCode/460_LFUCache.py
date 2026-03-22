from typing import Optional
from collections import defaultdict
class Node:
    def __init__(self, key: int, value: int) -> None:
        self.key = key
        self.value = value
        self.freq = 1
        self.prev: Optional[Node] = None
        self.next: Optional[Node] = None

class DoublyLinkedList:
    def __init__(self) -> None:
        self.head = Node(-1,-1)
        self.tail = Node(-1,-1)
        self.head.next = self.tail
        self.tail.prev = self.head
    
    def add_first(self, node: Node) -> None:
        # Add node after head
        node.prev = self.head
        node.next = self.head.next
        self.head.next.prev = node
        self.head.next = node
    
    def remove(self, node: Node) -> Node:
        # remove the specific node
        node.next.prev = node.prev
        node.prev.next = node.next
        node.next = None
        node.prev = None
        return node
    
    def remove_last(self) -> Node:
        # remove and return the LRU node (before tail)
        return self.remove(self.tail.prev)
    
    def is_empty(self) -> bool:
        return self.head.next==self.tail
    
class LFUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.min_freq = 0
        self.node_map: dict[int, Node] = {} # map from key to node
        self.freq_map: defaultdict[int, DoublyLinkedList] = defaultdict(DoublyLinkedList)
    
    def get(self, key: int) -> int:
        if self.capacity==0 or key not in self.node_map:
            return -1
        node = self.node_map[key]
        self._increment_frequency(node)
        return node.value
    
    def put(self, key: int, value: int) -> None:
        if self.capacity==0:
            return 0
        # update existing key
        if key in self.node_map:
            node = self.node_map[key]
            node.value = value
            self._increment_frequency(node)
            return
        
        # Evict LFU if it is at capacity
        if len(self.node_map)==self.capacity:
            freq_list = self.freq_map[self.min_freq]
            evicted_node = freq_list.remove_last()
            del self.node_map[evicted_node.key]
        
        # add new node
        node = Node(key, value)
        self._add_node(node)
        self.node_map[key] = node
        self.min_freq = 1
    
    def _increment_frequency(self, node: Node) -> None:
        freq = node.freq
        freq_list = self.freq_map[freq]
        freq_list.remove(node)

        if freq_list.is_empty():
            del self.freq_map[freq]
            if freq==self.min_freq:
                self.min_freq+=1
        node.freq+=1
        self._add_node(node)

    def _add_node(self, node: Node) -> None:
        freq = node.freq
        freq_list = self.node_map[freq]
        freq_list.add_first(node)