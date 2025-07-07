class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None

class Solution:
    def boundaryTraversal(self, root):
        if not root:
            return []

        result = []

        # Root ko tabhi add karo agar wo leaf nahi hai
        if not self._isLeaf(root):
            result.append(root.data)

        # Step 1: Add left boundary (excluding leaves)
        self.addLeftBoundary(root.left, result)

        # Step 2: Add all leaf nodes (left to right)
        self.addLeaves(root, result)

        # Step 3: Add right boundary in reverse (excluding leaves)
        self.addRightBoundary(root.right, result)

        return result

    # Leaf node check karne ke liye helper method
    def _isLeaf(self, node):
        return node.left is None and node.right is None

    # Left boundary nodes add karne ka kaam
    def addLeftBoundary(self, node, result):
        while node:
            if not self._isLeaf(node):
                result.append(node.data)

            if node.left:
                node = node.left
            else:
                node = node.right

    # Saare leaf nodes add karne ka kaam
    def addLeaves(self, node, result):
        if node is None:
            return

        if self._isLeaf(node):
            result.append(node.data)
            return

        self.addLeaves(node.left, result)
        self.addLeaves(node.right, result)

    # Right boundary nodes reverse order mein add karna
    def addRightBoundary(self, node, result):
        temp = []
        while node:
            if not self._isLeaf(node):
                temp.append(node.data)

            if node.right:
                node = node.right
            else:
                node = node.left

        result.extend(reversed(temp))  # Reverse karke result mein add karna
