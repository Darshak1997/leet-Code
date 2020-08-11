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


def reverse_sub_list(head, p, q):
  # TODO: Write your code here
  if p == q:
    return head
  prev, current = None, head
  i = 0
  # To store the elements before p
  while current is not None and i < p - 1:
    prev = current
    current = current.next
    i += 1

  # To join the elements after p in future
  last_node_of_first_part = prev
  # Starting of the sub list
  last_node_of_sub_list = current
  next = None

  i = 0
  # Reverse the sublist between p and q
  while current is not None and i < q - p + 1:
    next = current.next
    current.next = prev
    prev = current
    current = next
    i += 1
  # If p is not equal to 1
  if last_node_of_first_part is not None:
    last_node_of_first_part.next = prev
  # if p is equal to one and the head is empty
  else:
    head = prev
  # Join the list after q to the reversed list
  last_node_of_sub_list.next = current
  return head


def main():
  head = Node(1)
  head.next = Node(2)
  head.next.next = Node(3)
  head.next.next.next = Node(4)
  head.next.next.next.next = Node(5)

  print("Nodes of original LinkedList are: ", end='')
  head.print_list()
  result = reverse_sub_list(head, 2, 4)
  print("Nodes of reversed LinkedList are: ", end='')
  result.print_list()


main()
