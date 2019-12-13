'''
Write code to remove duplicates from an unsorted linked list.
'''
import random

class DoubleLinkedList:
  def __init__(self,head=None):
    self.head = head
  
  class Node:
    def __init__(self, data=None,next_node=None):
      self.data = data
      self.next = next_node
      
  def printNodes(self):
    n = self.head
    while n.next_node != None:
      print(n.data)
      n = n.next_node
    print(n.data)

  def insert(self, data):
    new_node = self.Node(data)
    new_node.next_node = self.head
    self.head = new_node
    print('New node inserted',new_node.data)

  def sort(self):
    n = self.head
    tmp = self.Node

    while n.next_node != None:
      if n > n.next_node:
        tmp = n.next_node
        n.next_node = n
        n = 

      


List = DoubleLinkedList()

for x in range(6):
  List.insert(random.randrange(0, 50, 3))

List.printNodes()
