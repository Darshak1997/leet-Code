from __future__ import print_function


class Node:
  def __init__(self, value, next=None):
    self.value = value
    self.next = next

  def print_list(self):
    temp = self
    while temp is not None:
      print(temp.value, end=" ")
      temp = temp.next
    print()


def reverse_every_k_elements(head, k):
  # TODO: Write your code here
  if k <= 1 or head is None:
    return head

  prev, current = None, head
  while True:
    last_node_from_prev = prev
    last_node_from_sub = current

    next = None
    i = 0
    while current is not None and i < k:
      next = current.next
      current.next = prev
      prev = current
      current = next
      i += 1
    if last_node_from_prev is not None:
      last_node_from_prev.next = prev
    else:
      head = prev
    
    last_node_from_sub.next = current

    if current is None:
      break
    prev = last_node_from_sub


  return head

def main():
  head = Node(1)
  head.next = Node(2)
  head.next.next = Node(3)
  head.next.next.next = Node(4)
  head.next.next.next.next = Node(5)
  head.next.next.next.next.next = Node(6)
  head.next.next.next.next.next.next = Node(7)
  head.next.next.next.next.next.next.next = Node(8)

  print("Nodes of original LinkedList are: ", end='')
  head.print_list()
  result = reverse_every_k_elements(head, 3)
  print("Nodes of reversed LinkedList are: ", end='')
  result.print_list()


main()







