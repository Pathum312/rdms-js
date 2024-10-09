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

    def insert(self, key: int) -> None:
        """
        Add a new node to the binary tree.

        Parameters:
            key (int): The value stored in the node.

        Returns:
            None
        """
        node: Node = self.node
        # List of nodes.
        stack: list[Node] = []

        while True:
            stack.append(node)

            # Since the key is less than the key of the current node, add a left node.
            if key < node.key:
                # If the current node doesn't have a left child node, then add the left child node.
                if not node.left:
                    node.left = Node(key=key)
                    # Assign the current node as the parent of the new left child node.
                    node.left.parent = node
                    self.logger.info(
                        msg=f"Left child node {node.left.key} of node {node.key} is created."
                    )
                    break
                # If, it does have a left node, then loop through the next lefy child node.
                node = node.left
            # Since the key is more than the key of the current node, add a right node.
            elif key > node.key:
                # If the current node doesn't have a right child node, then add the right child node.
                if not node.right:
                    node.right = Node(key=key)
                    # Assign the current node as the parent of the new right child node.
                    node.right.parent = node
                    self.logger.info(
                        msg=f"Right child node {node.right.key} of node {node.key} is created."
                    )
                    break
                # If, it does have a right node, then loop through the next right child node.
                node = node.right
            else:
                # Do not duplicate a existing node.
                return

        # Balance the binary tree
        self.balancing(stack=stack)

    def max_depth(self, node: Node | None) -> int:
        """
        Finds the max height of a subtree.

        Parameters:
            node (Node): Node object used to find the height.

        Returns:
            int: Height of the subtree.
        """
        # If a node doesn't exist, return 0.
        if not node:
            return 0

        # If a node exists, add 1 to the count for that particular subtree.
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

    def balancing(self, stack: list[Node]) -> None:
        """
        Calculates the balance factors for all the nodes, then rotates the unbalanced nodes.

        Attributes:
            stack (list[Node]): List of nodes in the order, they were inserted to the tree.

        Returns:
            None
        """
        # While the node stack is not empty.
        while stack:
            # Get the last node from the list.
            node: Node = stack.pop()
            # Calculate the balance factor for that node.
            node.balance_factor = self.calculate_balance_factor(node=node)

            # If the balance factor is greater that 1, there is more child nodes on the left side.
            if node.balance_factor > 1:
                self.logger.info(
                    msg=f"Node {node.key} has a balance factor of {node.balance_factor}."
                )

                # If the balance factor is less than 1, rotate left first.
                if self.calculate_balance_factor(node=node.left) < 0:  # type: ignore
                    self.rotate_left(node=node.left)  # type: ignore

                # Finally, rotate the node to the right.
                self.rotate_right(node=node)
            # If the balance factor is greater that 1, there is more child nodes on the right side.
            elif node.balance_factor < -1:
                self.logger.info(
                    msg=f"Node {node.key} has a balance factor of {node.balance_factor}."
                )

                # If the balance factor is greater than 1, rotate right first.
                if self.calculate_balance_factor(node=node.right) > 0:  # type: ignore
                    self.rotate_right(node=node.right)  # type: ignore

                # Finally, rotate the node to the left.
                self.rotate_left(node=node)

    def rotate_right(self, node: Node) -> None:
        """
        Rotate the unblanced node to the right.

        Attributes:
            node (Node): Unblanced node that is going to be rotated.

        Returns:
            None
        """
        self.logger.info(msg=f"Node {node.key} requires right rotation.")
        self.logger.info(msg=f"Rotating...")

        # Left child node of the unbalanced node.
        child_node: Node = node.left  # type: ignore
        # Parent node of the unbalanced node.
        parent_node: Node = node.parent  # type: ignore

        # If the child node has a right child node;
        # Assign it as the left child node of the unbalanced node.
        if child_node.right:
            node.left = child_node.right
        # If there is no child node;
        # Assign None to the left of the unbalanced node.
        else:
            node.left = None

        # The child node becomes the parent of the unbalanced node.
        node.parent = child_node
        # The unbalanced node becomes the right child node of the child node.
        child_node.right = node

        # If the unbalanced node is the root node.
        if node.root:
            # Mark the unbalanced node as not the root node.
            node.root = False
            # Mark the child node as the root node.
            child_node.root = True
            self.node = child_node
        # If, it is not the root node, swap the parents.
        else:
            # The parent node of the unbalanced node, becomes the parent of the child node.
            child_node.parent = parent_node
            # The left child node the parent node becomes the child node.
            parent_node.left = child_node

        self.logger.info(msg=f"Rotated right at node {node.key}.")

    def rotate_left(self, node: Node) -> None:
        """
        Rotate the unblanced node to the right.

        Attributes:
            node (Node): Unblanced node that is going to be rotated.

        Returns:
            None
        """
        self.logger.info(msg=f"Node {node.key} requires left rotation.")
        self.logger.info(msg=f"Rotating...")

        # Right child node of the unbalanced node.
        child_node: Node = node.right  # type: ignore
        # Parent node of the unbalanced node.
        parent_node: Node = node.parent  # type: ignore

        # If the child node has a left child node;
        # Assign it as the right child node of the unbalanced node.
        if child_node.left:
            node.right = child_node.left
        # If there is no child node;
        # Assign None to the right of the unbalanced node.
        else:
            node.right = None

        # The child node becomes the parent of the unbalanced node.
        node.parent = child_node
        # The unbalanced node becomes the right child node of the child node.
        child_node.left = node

        # If the unbalanced node is the root node.
        if node.root:
            # Mark the unbalanced node as not the root node.
            node.root = False
            # Mark the child node as the root node.
            child_node.root = True
            self.node = child_node
        # If, it is not the root node, swap the parents.
        else:
            # The parent node of the unbalanced node, becomes the parent of the child node.
            child_node.parent = parent_node
            # The right child node the parent node becomes the child node.
            parent_node.right = child_node

        self.logger.info(msg=f"Rotated left at node {node.key}.")


if __name__ == "__main__":
    # Right Rotation
    tree: AVLTree = AVLTree(key=30)
    tree.insert(key=20)
    tree.insert(key=10)
    tree.insert(key=8)
    tree.insert(key=6)
    tree.insert(key=5)
    tree.insert(key=4)

    # # Left Rotation
    # tree: AVLTree = AVLTree(key=10)
    # tree.insert(key=20)
    # tree.insert(key=30)

    # # Right-Left Rotation
    # tree: AVLTree = AVLTree(key=10)
    # tree.insert(key=30)
    # tree.insert(key=20)

    # # Left-Right Rotation
    # tree: AVLTree = AVLTree(key=30)
    # tree.insert(key=10)
    # tree.insert(key=20)
