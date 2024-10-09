from logging import Logger

from logger import LOGGER


class Node:
    def __init__(self, key: int) -> None:
        self._key: int = key
        self.root: bool = False
        self.balance_factor: int = 0
        self.left: Node | None = None
        self.right: Node | None = None
        self.parent: Node | None = None

    @property
    def key(self) -> int:
        return self._key


class AVLTree:
    def __init__(self, key: int) -> None:
        self.node: Node = Node(key=key)
        self.node.root = True
        self.logger: Logger = LOGGER(_name="avl_tree.AVLTree", _filename="tree.log")
        self.logger.info(msg="Creating AVL tree...")
        self.logger.info(msg=f"Origin node {self.node.key} is created.")

    def insert(self, key: int) -> None:
        stack = []  # Stack to keep track of nodes
        node = self.node

        while True:
            stack.append(node)
            if key < node.key:
                if node.left is None:
                    node.left = Node(key=key)
                    node.left.parent = node
                    self.logger.info(
                        msg=f"Left child node {node.left.key} of node {node.key} is created."
                    )
                    break
                node = node.left
            elif key > node.key:
                if node.right is None:
                    node.right = Node(key=key)
                    node.right.parent = node
                    self.logger.info(
                        msg=f"Right child node {node.right.key} of node {node.key} is created."
                    )
                    break
                node = node.right
            else:
                # Key already exists, do not insert duplicates
                return

        self.balance(stack)

    def max_depth(self, node: Node | None) -> int:
        if node is None:
            return 0
        return max(self.max_depth(node.left), self.max_depth(node.right)) + 1

    def calculate_balance_factor(self, node: Node) -> int:
        return self.max_depth(node.left) - self.max_depth(node.right)

    def balance(self, stack: list[Node]) -> None:
        while stack:
            node = stack.pop()
            node.balance_factor = self.calculate_balance_factor(node)

            if node.balance_factor > 1:
                if self.calculate_balance_factor(node.left) < 0:
                    self.rotate_left(node.left)  # Left-Right case
                self.rotate_right(node)  # Right case
            elif node.balance_factor < -1:
                if self.calculate_balance_factor(node.right) > 0:
                    self.rotate_right(node.right)  # Right-Left case
                self.rotate_left(node)  # Left case

    def rotate_left(self, node: Node) -> None:
        right_node = node.right
        node.right = right_node.left
        if right_node.left:
            right_node.left.parent = node
        right_node.parent = node.parent

        if node.parent is None:
            self.node = right_node
            right_node.root = True
        elif node == node.parent.left:
            node.parent.left = right_node
        else:
            node.parent.right = right_node

        right_node.left = node
        node.parent = right_node

        self.logger.info(msg=f"Rotated left at node {node.key}")

    def rotate_right(self, node: Node) -> None:
        left_node = node.left
        node.left = left_node.right
        if left_node.right:
            left_node.right.parent = node
        left_node.parent = node.parent

        if node.parent is None:
            self.node = left_node
            left_node.root = True
        elif node == node.parent.right:
            node.parent.right = left_node
        else:
            node.parent.left = left_node

        left_node.right = node
        node.parent = left_node

        self.logger.info(msg=f"Rotated right at node {node.key}")


if __name__ == "__main__":
    tree = AVLTree(key=30)
    tree.insert(20)
    tree.insert(10)
    tree.insert(8)
    tree.insert(6)
