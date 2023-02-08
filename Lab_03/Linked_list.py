class Node:
  def __init__(self, e, n):
    self.element = e
    self.next = n

class LinkedList:
  def __init__(self, a):
    self.head = None
    # To Do
    if type(a)==list:
        self.head=Node(a[0],None)
        tail=self.head
        for i in range(1,len(a)):
            n=Node(a[i],None)
            tail.next=n
            tail=tail.next
    else:
        self.head=a


  # Count the number of nodes in the list
  def countNode(self):
    # To Do
    count=0
    tail=self.head
    while tail!=None:
        count+=1
        tail=tail.next
    return count


  # Print elements in the list
  def printList(self):
    # To Do
    tail=self.head
    while tail!=None:
        if tail.next!=None:
            print(tail.element,end=", ")
        else:
            print(tail.element ,end=".")
            print()
        tail=tail.next


  # returns the reference of the Node at the given index. For invalid index return None.
  def nodeAt(self, idx):
    # To Do
    count=0
    tail=self.head
    while count<=idx:
        count+=1
        a=tail
        tail=tail.next
    return a


  # returns the element of the Node at the given index. For invalid
  def get(self, idx):
    # To Do
    count=0
    tail=self.head
    while count<=idx:
        count+=1
        a=tail
        tail=tail.next
    return a.element


  # updates the element of the Node at the given index.
  # Returns the old element that was replaced. For invalid index return None.
  # parameter: index, element
  def set(self, idx, elem):
    # To Do
    tail=self.head
    count=0
    while tail:                 #for the time there tail!=None
        if count==idx:
            a=tail.element
            tail.element=elem
            return a
        tail=tail.next
        count+=1


  # returns the index of the Node containing the given element.
  # if the element does not exist in the List, return -1.
  def indexOf(self, elem):
    # To Do
    tail=self.head
    idx,flag=0,False
    while tail:
        if tail.element==elem:
            return idx
        tail=tail.next
        idx+=1
    return -1
    if idx==0:
        self.head=Node(elem,tail)


  # returns true if the element exists in the List, return false otherwise.
  def contains(self, elem):
    # To Do
    tail=self.head
    while tail:
        if tail.element==elem:
            return True
        tail=tail.next
    return False


  # Makes a duplicate copy of the given List. Returns the reference of the duplicate list.
  def copyList(self):
    # To Do
    tail_of_main=self.head
    head=Node(tail_of_main.element,None)
    tail=head
    tail_of_main=tail_of_main.next
    while tail_of_main:
        n=Node(tail_of_main.element,None)
        tail.next=n
        tail=n
        tail_of_main=tail_of_main.next
    return head


  # Makes a reversed copy of the given List. Returns the head reference of the reversed list.
  def reverseList(self):
    # To Do
    tail=self.head
    n=self.countNode()
    for i in range(n):
        if i==n-1:
            head2=Node(tail.element,None)
        tail=tail.next
    tail2=head2
    tail=self.head
    for i in range(n-1,0 ,-1):
        for j in range(i):
            if j==i-1:
                tail3=Node(tail.element,None)
                tail2.next=tail3
                tail2=tail3
            tail=tail.next
        tail=self.head
    return head2


  # inserts Node containing the given element at the given index
  # Check validity of index.
  def insert(self, elem, idx):
    # To Do
    tail=self.head
    i=0
    if idx==0:
        self.head=Node(elem,tail)
        self.head.next=tail
        return self.head
    else:
        while tail:
            if i==(idx-1):
                tail.next=Node(elem,tail.next)
                return self.head
            tail=tail.next
            i+=1


  # removes Node at the given index. returns element of the removed node.
  # Check validity of index. return None if index is invalid.
  def remove(self, idx):
    # To Do
    tail=self.head
    i=0
    if idx==0:
        a=self.head.element
        self.head=self.head.next
        return f"Removed Element: {a}."
    else:
        while tail:
            if i==(idx-1):
                a=tail.next.element
                tail.next=tail.next.next
                return f"Removed Element: {a}."
            tail=tail.next
            i+=1


  # Rotates the list to the left by 1 position.
  def rotateLeft(self):
    # To Do
    tail=self.head
    x=tail
    self.head=self.head.next
    while tail:
        if tail.next==None:
            tail.next= x
            tail.next.next=None
        tail=tail.next


  # Rotates the list to the right by 1 position.
  def rotateRight(self):
    # To Do
    tail=self.head
    x=tail
    while tail:
        if tail.next.next==None:
            self.head=tail.next
            tail.next.next=x
            tail.next=None
            return self.head
        tail=tail.next