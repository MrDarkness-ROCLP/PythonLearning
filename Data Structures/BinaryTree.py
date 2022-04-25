class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def search(self, target):
        if self.data == target:
            print("Found it!")
            return self

        if self.left and self.data > target:
            return self.left.search(target)

        if self.right and self.data < target:
            return self.right.search(target)

        print("Value is not in tree")

    def traversePreorder(self):
        print(self.data)
        if self.left:
            self.left.traversePreorder()
        if self.right:
            self.right.traversePreorder()

    def traverseInorder(self):
        if self.left:
            self.left.traverseInorder()
        print(self.data)
        if self.right:
            self.right.traverseInorder()

    def traversePostorder(self):
        if self.left:
            self.left.traversePostorder()
        if self.right:
            self.right.traversePostorder()
        print(self.data)

    def height(self, h=0):
        leftHeight = self.left.height(h+1)if self.left else h
        rightHeight = self.right.height(h + 1) if self.right else h
        return max(leftHeight,rightHeight)

class Tree:
    def __init__(self, root, name=''):
        self.root = root
        self.name = name

    def search(self, target):
        return self.root.search(target)

    def traversePreorder(self):
        self.root.traversePreorder()

    def traverseInorder(self):
        self.root.traverseInorder()

    def traversePostorder(self):
        self.root.traversePostorder()

    def height(self):
        return self.root.height()

# node = Node(10)
#
# node.left = Node(5)
# node.right = Node(15)
#
# node.left.left = Node(2)
# node.left.right = Node(6)
#
# node.right.left = Node(13)
# node.right.right = Node(100000)
# #print(node.right.data)
# #print(node.right.right.data)
#
# myTree = Tree(node, 'My Tree')
# print(myTree.name)
# print(myTree.root.right.data)
# print(myTree.root.right.right.data)

# foundData = myTree.root.search(33)
# print(foundData.data)
# foundData = myTree.search(100000)
# print(foundData.data)

tree = Tree(Node(50), 'Tree Traversal')
tree.root.left = Node(25)
tree.root.right = Node(75)
tree.root.left.left = Node(10)
tree.root.left.right = Node(35)
tree.root.left.right.left = Node(30)
tree.root.left.right.right = Node(42)
tree.root.left.left.left = Node(5)
tree.root.left.left.right = Node(13)
tree.root.left.left.left.left = Node(2)

# print('Traverse Pre-Order')
# tree.traversePreorder()
#
# print('\nTraverse In-order')
# tree.traverseInorder()
#
# print('\nTraverse Post-order')
# tree.traversePostorder()

print(tree.root.height())