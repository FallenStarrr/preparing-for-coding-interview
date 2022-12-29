class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, val):
        new_node = Node(val)
        if not self.root:
            self.root = new_node
            return
        current_node = self.root
        while True:
            if val < current_node.val:
                if not current_node.left:
                    current_node.left = new_node
                    return

                current_node = current_node.left

                else:
                    if not current_node.right:
                        current_node.right = new_node
                        return
                    current_node  = current_node.right

    def search(self, val):
        current_node = self.root
        while current_node:
            if val == current_node.val:
                return True
            elif val < current_node.val:
                current_node = current.node.left
            else:
                current_node = current_node.right

        return False

def delete(root, val):
    if not root:
        return root

    if val < root.val:
        root.left = delete(root.left, val)
    elif val > root.val:
        root.right = delete(root.right, val)
    else:
        if not root.left:
            return root.right
        elif not root.right:
            return root.left

        else:
            successor = root.right
            while successor.left:
                successor = successor.left
            root.val = successor.val
            root.right = delete(root.right, successor.val)

    return root    
