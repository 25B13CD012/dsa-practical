from collections import deque

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def append(head, value):
    node = Node(value)

    if head is None:
        return node

    cur = head
    while cur.next:
        cur = cur.next

    cur.next = node
    return head

def insert(root, value):
    if root is None:
        return BST(value)

    if value < root.value:
        root.left = insert(root.left, value)
    elif value > root.value:
        root.right = insert(root.right, value)

    return root

def inorder(root):
    if root:
        return (
            inorder(root.left)
            + [root.value]
            + inorder(root.right)
        )
    return []

# Stack
stack = []

for x in (10, 20, 30):
    stack.append(x)

print("Stack pop:", stack.pop())

# Queue
queue = deque((10, 20, 30))
print("Queue remove:", queue.popleft())

# Linked List
head = None

for x in (10, 20, 30):
    head = append(head, x)

items = []
cur = head

while cur:
    items.append(cur.value)
    cur = cur.next

print("List:", " -> ".join(map(str, items)))

# Binary Search Tree
root = None

for x in (40, 20, 60, 10, 30, 50, 70):
    root = insert(root, x)

print("BST inorder:", *inorder(root))