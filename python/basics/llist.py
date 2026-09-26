class Node:
    def __init__(self, data):
        self.data = data; 
        self.next = None;


class LinkedList:
    def __init__(self):
        self.head = None;

myList = LinkedList();
node = Node(1);
myList.head = node;
myList.head.next = Node(2);
myList.head.next.next = Node(3);
myList.head.next.next.next = Node(4);
myList.head.next.next.next.next = Node(5);
current  = myList.head;
while(current):
    print(current.data, '-->');
    current = current.next;

# now trying to find the middle of the list.
slow = myList.head;
fast = myList.head;

while(fast and fast.next):
    slow = slow.next;
    fast = fast.next.next;

print("Middle element is: ", slow.data);
