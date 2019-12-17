'''
Write code to remove duplicates from an unsorted linked list.
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

def removeDuplicates(list):
    current = list.head
    hashTable = {}
    prev = list.Node()
    while current != None:
        if str(current.data) in hashTable:
            prev.next = current.next
        else:
            hashTable[str(current.data)] = current.data
            prev = current
        current = current.next

#ACTION
List = LinkedList()
for x in range(6):
  List.append(random.randrange(0, 10))
print('Nodes with duplicates')
List.printNodes()
print('Nodes with no duplicates')
removeDuplicates(List)
List.printNodes()
