class Node:
  def __init__(self, data=None):
    self.data = data
    self.next = None


class LinkedList:
  def __init__(self):
    self.head = None

  def insert_at_beginning(self, data):
    new_node = Node(data)
    new_node.next = self.head
    self.head = new_node

  def insert_at_end(self, data):
    new_node = Node(data)
    if self.head is None:
      self.head = new_node
    else:
      cur = self.head
      while cur.next:
        cur = cur.next
      cur.next = new_node

  def insert_after(self, prev_node: Node, data):
    if prev_node is None:
      print("Попереднього вузла не існує.")
      return
    new_node = Node(data)
    new_node.next = prev_node.next
    prev_node.next = new_node

  def delete_node(self, key: int):
    cur = self.head
    if cur and cur.data == key:
      self.head = cur.next
      cur = None
      return
    prev = None
    while cur and cur.data != key:
      prev = cur
      cur = cur.next
    if cur is None:
      return
    prev.next = cur.next
    cur = None

  def search_element(self, data: int) -> Node | None:
    cur = self.head
    while cur:
      if cur.data == data:
        return cur
      cur = cur.next
    return None

  def print_list(self):
    current = self.head
    while current:
      print(current.data)
      current = current.next

  def reverse(self):
    prev = None
    current = self.head
    while current:
      next_node = current.next
      current.next = prev
      prev = current
      current = next_node
    self.head = prev

  def sort(self):
    if self.head is None or self.head.next is None:
      return
    sorted_head = None
    current = self.head
    while current:
      next_node = current.next
      if sorted_head is None or sorted_head.data >= current.data:
        current.next = sorted_head
        sorted_head = current
      else:
        search = sorted_head
        while search.next and search.next.data < current.data:
          search = search.next
        current.next = search.next
        search.next = current
      current = next_node
    self.head = sorted_head


def merge_sorted_lists(list1: LinkedList, list2: LinkedList) -> LinkedList:
  merged = LinkedList()
  dummy = Node()
  tail = dummy

  a = list1.head
  b = list2.head

  while a and b:
    if a.data <= b.data:
      tail.next = a
      a = a.next
    else:
      tail.next = b
      b = b.next
    tail = tail.next

  tail.next = a if a else b

  merged.head = dummy.next
  return merged


if __name__ == "__main__":
  # Reverse
  ll = LinkedList()
  for val in [1, 2, 3, 4, 5]:
    ll.insert_at_end(val)
  print("Original:")
  ll.print_list()
  ll.reverse()
  print("Reversed:")
  ll.print_list()

  # Sort
  ll2 = LinkedList()
  for val in [4, 2, 7, 1, 9, 3]:
    ll2.insert_at_end(val)
  print("\nUnsorted:")
  ll2.print_list()
  ll2.sort()
  print("Sorted:")
  ll2.print_list()

  # Merge two sorted lists
  a = LinkedList()
  for val in [1, 3, 5]:
    a.insert_at_end(val)
  b = LinkedList()
  for val in [2, 4, 6]:
    b.insert_at_end(val)
  merged = merge_sorted_lists(a, b)
  print("\nMerged sorted lists:")
  merged.print_list()