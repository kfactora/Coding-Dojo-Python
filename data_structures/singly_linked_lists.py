class SLNode:
  def __init__(self, val):
    self.value = val
    self.next = None
  
class SLList:
  def __init__(self):
    self.head = None
  def addToFront(self, val):
    new_node = SLNode(val)
    current_head = self.head
    new_node.next = current_head
    self.head = new_node	
    return self	      

my_list = SLList()
my_list.addToFront("Jim").addToFront("Dwight").addToFront("Andy")
print(my_list)
