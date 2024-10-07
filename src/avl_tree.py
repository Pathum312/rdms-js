from enum import StrEnum
from logging import Logger

from logger import LOGGER


class TRAVERSAL_FUNCTION(StrEnum):
    """
    A class that holds StrEnum values.

    Attributes:
        CALCULATE (str): Used to trigger calculations.
        FIND (str): Used to find a unbalanced node.
    """

    CALCULATE = "CALCULATE"
    FIND = "FIND"


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
        self.root: bool = False
        self.balance_factor: int = 0
        self.left: Node | None = None
        self.right: Node | None = None
        self.parent: Node | None = None

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
                # Balance the binary tree.
                self.balancing(node=self.node)
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
                # Balance the binary tree.
                self.balancing(node=self.node)
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
        # If a node doesn't exist, return 0.
        if node is None:
            return 0
        # If a node exists, add 1 to the count for that particular subtree.
        else:
            ldepth: int = self.max_depth(node=node.left)
            rdepth: int = self.max_depth(node=node.right)

            return max(ldepth, rdepth) + 1

    def calculate_balance_factor(self, node: Node) -> int:
        """
        Calculating the balance factor of a node.\n
        Balance Factor = Left Subtree Depth - Right Subtree Depth

        Parameters:
            node (Node): The balance factor is calculated for this node.

        Returns:
            int: The balance factor of the Node object.
        """
        # Depth of the left subtree.
        left_height: int = self.max_depth(node=node.left)
        # Depth of the right subtree.
        right_height: int = self.max_depth(node=node.right)

        # Balance factor = Left Subtree Depth = Right Subtree Depth
        balance_factor: int = left_height - right_height

        return balance_factor

    def traversal(
        self, node: Node | None, type: TRAVERSAL_FUNCTION | None = None
    ) -> None | Node:
        """
        Travels through the binary treee using preorder logic.

        Attributes:
            node (Node | None): The initial node to start travelling from.
            type (TRAVERSAL_FUNCTION | None): A StrEnum, that executest calculations or find specific nodes.

        Returns:
            Node | None: Returns an unbalanced node, or returns nothing.
        """
        # If node is None just return.
        if not node:
            return

        # Calculate the balance factor of the node.
        if type is TRAVERSAL_FUNCTION.CALCULATE:
            node.balance_factor = self.calculate_balance_factor(node=node)
        # Find the unbalanced node.
        elif type is TRAVERSAL_FUNCTION.FIND:
            unbalanced_node: Node | None = self.find_unbalanced_node(node=node)
            # Check if the returns value is not None.
            if unbalanced_node:
                return unbalanced_node

        # Travel along left child tree.
        self.traversal(node=node.left, type=type)

        # Travel along right child tree.
        self.traversal(node=node.right, type=type)

    def find_unbalanced_node(self, node: Node) -> Node | None:
        """
        Check if the node is not balanced.

        Attributes:
            node (Node): Node that is going to be checked.

        Returns:
            Node | None: Returns the unbalanced node, if found.
        """
        # Balance factor has to be > 1 or < -1 to be considered unbalanced.
        if node.balance_factor > 1 or node.balance_factor < -1:
            return node

    def rotating(self, node: Node) -> None:
        if not node:
            return

        if node.balance_factor < 0:
            if node.right.balance_factor < 0:  # type: ignore
                self.logger.info(msg=f"Node {node.key} requires left rotation.")
            elif node.right.balance_factor > 0:  # type: ignore
                self.logger.info(msg=f"Node {node.key} requires right-left rotation.")
        elif node.balance_factor > 0:
            if node.left.balance_factor > 0:  # type: ignore
                self.logger.info(msg=f"Node {node.key} requires right rotation.")
            elif node.left.balance_factor < 0:  # type: ignore
                self.logger.info(msg=f"Node {node.key} requires left-right rotation.")

    def balancing(self, node: Node) -> None:
        """
        Balanacing the node tree.

        Attributes:
            node (Node): Origin node must always be passed here.

        Returns:
            None
        """
        # Calculating the balance factor for the nodes.
        self.traversal(node=node, type=TRAVERSAL_FUNCTION.CALCULATE)
        # Find the unbalanced node from the binary tree.
        unbalanced_node: None | Node = self.traversal(
            node=node, type=TRAVERSAL_FUNCTION.FIND
        )
        # Rotating the unbalanced nodes to balance the binary tree.
        self.rotating(node=unbalanced_node)  # type: ignore


if __name__ == "__main__":
    # Right Rotation
    tree: AVLTree = AVLTree(key=30)
    tree.insert(node=tree.node, key=20)
    tree.insert(node=tree.node, key=10)

    # # Left Rotation
    # tree: AVLTree = AVLTree(key=10)
    # tree.insert(node=tree.node, key=20)
    # tree.insert(node=tree.node, key=30)

    # # Right-Left Rotation
    # tree: AVLTree = AVLTree(key=10)
    # tree.insert(node=tree.node, key=30)
    # tree.insert(node=tree.node, key=20)

    # # Left-Right Rotation
    # tree: AVLTree = AVLTree(key=30)
    # tree.insert(node=tree.node, key=10)
    # tree.insert(node=tree.node, key=20)
