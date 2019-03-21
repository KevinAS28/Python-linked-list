import random
import string

orang = list(string.ascii_uppercase)

class Node:
 def __init__(self, node=None, next_node=None):
  self.node = node
  self.next = next_node
 
class linked_list:
 head = None
 def depan(self, data):
  self.head = Node(data, self.head)
 def belakang(self, data):
  the_node = Node(data)
  curr = self.head
  if (curr==None):
   self.head = the_node
   return
  while (curr.next):
   curr = curr.next
  curr.next = Node(data)

 def print_all_node(self):
  curr = self.head
  #if (curr==None): print(None);return
  while (True):
   print(curr.node)
   curr = curr.next
   if(curr==None): break

s = linked_list()

"""
s.depan(10)
s.depan(10)
s.depan(12)
s.depan(12)
s.depan(12)
"""
s.belakang(10)
s.belakang(10)
s.belakang(12)
s.belakang(12)
s.belakang(12)
s.print_all_node()
