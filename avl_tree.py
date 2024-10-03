from logging import Logger

from logger import LOGGER


class Node:
    """
    A class representing a node in a binary tree.

    Attributes:
        key (int): The value stored in the node.
        left (Node | None): The left Node object of the current node.
        right (Node | None): The right Node object of the current node.
        balance_factor (int): Checks if the left and right child nodes have matching heights, the balance factor should be -1, 0 or 1.
        parent (Node | None): The parent node of the current node.
        root (bool): Whether the current node od the origin node.
    """

    def __init__(self, key: int) -> None:
        """
        Initializes a Node object.

        Parameters:
            key (int): The value to be stored in the node.
        """
        self._key: int = key
        self.left: Node | None = None
        self.right: Node | None = None
        self.balance_factor: int = 0
        self.parent: Node | None = None
        self.root: bool = False

    @property
    def key(self) -> int:
        """
        Returns the private value of _key.

        Returns:
            int: Value of _key of the Node object.
        """
        return self._key


class AVLTree:
    """
    A class representing a balancing binary tree.

    Attributes:
        key (int): The value stored in the node.
        node (Node): The origin node; that is created, when the AVLTree object is initialzed.
        logger (Logger): The logger will post logs to the tree.log file.
    """

    def __init__(self, key: int) -> None:
        """
        Initializes a AVLTree object

        Parameters:
            key (int): The value stored in the node.
        """
        self._key: int = key
        self.node: Node = Node(key=self._key)
        self.node.root = True
        self.logger: Logger = LOGGER(_name="avl_tree.AVLTree", _filename="tree.log")
        self.logger.info(msg=f"Creating AVL tree...")
        self.logger.info(msg=f"Origin node {self.node.key} is created.")

    def insert(self, node: Node, key: int) -> None:
        """
        Add a new node to the binary tree.

        Parameters:
            node (Node): The node object the new the node object is being added too.
            key (int): The value stored in the node.

        Returns:
            None
        """
        # Since the key is less than the key of the current node, add a left node.
        if key < node.key:
            # If the current node doesn't have a left child node, then add the left child node.
            if node.left is None:
                node.left = Node(key=key)
                # Assign the current node as the parent of the new left child node.
                node.left.parent = node
                self.logger.info(
                    msg=f"Left child node {node.left.key} of node {node.key} is created."
                )
            # When there is already a left child node, run the function again but with left child node.
            else:
                self.insert(node=node.left, key=key)

        # Since the key is more than the key of the current node, add a right node.
        if key > node.key:
            # If the current node doesn't have a right child node, then add the right child node.
            if node.right is None:
                node.right = Node(key=key)
                # Assign the current node as the parent of the new right child node.
                node.right.parent = node
                self.logger.info(
                    msg=f"Right child node {node.right.key} of node {node.key} is created."
                )
            # When there is already a right child node, run the function again but with right child node.
            else:
                self.insert(node=node.right, key=key)

    def max_depth(self, node: Node | None) -> int:
        """
        Finds the max height of a subtree.

        Parameters:
            node (Node): Node object used to find the height.

        Returns:
            int: Height of the subtree.
        """
        if node is None:
            return 0
        else:
            ldepth: int = self.max_depth(node=node.left)
            rdepth: int = self.max_depth(node=node.right)

            return max(ldepth, rdepth) + 1

    def calculate_balance_factor(self, node: Node) -> int:
        """
        Calculating the balance factor of a node.

        Parameters:
            node (Node): The balance factor is calculated for this node.

        Returns:
            int: The balance factor of the Node object.
        """
        left_height: int = self.max_depth(node=node.left)
        right_height: int = self.max_depth(node=node.right)

        return left_height - right_height

    def right_rotation(self, node: Node) -> None:
        parent_node: Node = node
        child_node: Node = node.left  # type: ignore

        self.swap_parent(parent_node=parent_node, child_node=child_node)

        parent_node.left = None
        parent_node.parent = child_node

        child_node.right = parent_node

    def left_rotation(self, node: Node) -> None:
        parent_node: Node = node
        child_node: Node = node.right  # type: ignore

        self.swap_parent(parent_node=parent_node, child_node=child_node)

        parent_node.right = None
        parent_node.parent = child_node

        child_node.left = parent_node

    def left_right_rotation(self, node: Node) -> None:
        parent_node: Node = node
        child_node: Node = node.left  # type: ignore

        self.left_rotation(node=child_node)
        self.right_rotation(node=parent_node)

    def swap_parent(self, parent_node: Node, child_node: Node) -> None:
        if parent_node.root:
            parent_node.root = False

            child_node.root = True
            child_node.parent = None
            self.node = child_node
        else:
            child_node.parent = parent_node.parent

    def preorder_traversal(self, node: Node) -> None:
        node.balance_factor = self.calculate_balance_factor(node=node)

        if node.left:
            self.preorder_traversal(node=node.left)

        if node.right:
            self.preorder_traversal(node=node.right)


if __name__ == "__main__":
    tree: AVLTree = AVLTree(key=10)
    tree.insert(node=tree.node, key=20)
    tree.insert(node=tree.node, key=30)
