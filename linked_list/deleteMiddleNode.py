'''
Implement an algorithm to delete a node in the middle of a singly linked list, given only access to that node
'''
import random

class LinkedList:
  def __init__(self,head=None):
    self.head = head
  
  class Node:
    def __init__(self, data=None,next_node=None):
      self.data = data
      self.next = next_node
      
  def printNodes(self):
    n = self.head
    while n != None:
      print(n.data)
      n = n.next

  def append(self, data):
    if self.head == None:
      self.head = self.Node(data)
      return
    current = self.head
    while current.next != None:
      current = current.next
    current.next = self.Node(data)

  def deleteNode(self,n):
    current = self.head
    prev = self.Node()
    while current != None:
      if current.data == n:
        prev.next = current.next
      else:
        prev = current
      current = current.next
    print('Node deleted',n)

#ACTION
List = LinkedList()

for x in range(6):
  List.append(random.randrange(0, 10))

List.printNodes()
List.deleteNode(4)
