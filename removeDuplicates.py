'''
Write code to remove duplicates from an unsorted linked list.
'''
import random

class DoubleLinkedList:
  def __init__(self,head=None):
    self.head = head
  
  class Node:
    def __init__(self, data=None,next_node=None,prev=None):
      self.data = data
      self.next = next_node
      
  def printNodes(self):
    n = self.head
    while n.next_node != None:
      print(n.data)
      n = n.next_node
    print(n.data)

  def insertionSort(self, data):
    new_node = self.Node(data)
    curr_node = self.Node()
    if (self.head == None) or (new_node.data < self.head.data):
        new_node.next_node = self.head
        self.head = new_node
    else:
      while curr_node.next_node != None:   
        if new_node.data > curr_node.data:
          curr_node = curr_node.next_node
        elif curr_node == new_node:
          print('Error: Node already exists')
          return
        new_node.prev = curr_node
        new_node.next_node = curr_node.next_node.next_node
        curr_node.next_node = new_node
    
    print('New node inserted',new_node.data)
        
#ACTION
List = DoubleLinkedList()

for x in range(6):
  List.insertionSort(random.randrange(0, 50, 3))

List.printNodes()
