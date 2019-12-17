'''
Implement an algorithm to finde the kth to last element of a singly linked list
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

  def nthToLast(self,k):
    current = self.head
    tlength = self.len()
    length = tlength - (k)
    i = 0
    if k > tlength or k < 1:
      print('nth element out of reach')
      return
    while length != i:
      current = current.next
      i += 1
    print('Nth last node',current.data)
      
  def len(self):
    current = self.head
    i = 0
    while current != None:
      current = current.next
      i += 1
    return i


#ACTION
List = LinkedList()

for x in range(6):
  List.append(random.randrange(0, 10))

List.printNodes()
List.nthToLast(3)
