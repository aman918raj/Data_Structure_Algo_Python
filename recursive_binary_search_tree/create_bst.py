from node import Node

class BinarySearchTree:

    def __init__(self):
        self.root = None

    def __insert(self, current_node, value):
        if current_node is None:
            return Node(value)

        if value > current_node.value:
            current_node.right = self.__insert(current_node.right, value)

        if value < current_node.value:
            current_node.left = self.__insert(current_node.left, value)

        return current_node

    def insert(self, value):
        if self.root is None:
            self.root = Node(value)
        self.__insert(self.root, value)

    def __contains(self, current_node, value):
        if current_node is None:
            return False
        if current_node.value == value:
            return True
        if current_node.value > value:
            return self.__contains(current_node.left, value)
        else:
            return self.__contains(current_node.right, value)

    def contains(self, value):
        return self.__contains(self.root, value)


bst = BinarySearchTree()

bst.insert(42)
bst.insert(32)
bst.insert(46)
bst.insert(21)
bst.insert(56)
bst.insert(49)
bst.insert(24)

print(bst.root.right.value)





