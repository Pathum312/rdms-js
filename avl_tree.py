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

    def insert(self, node: Node, key: int) -> None:
        """
        Add a new node to the binary tree.

        Parameters:
            node (Node): The node object the new the node object is being added too.
            key (int): The value stored in the node.

        Returns:
            None
        """
        # Add a left node
        if key < node.key:
            if node.left is None:
                node.left = Node(key=key)
                node.left.parent = node
            else:
                self.insert(node=node.left, key=key)
        # Add a right node
        if key > node.key:
            if node.right is None:
                node.right = Node(key=key)
                node.right.parent = node
            else:
                self.insert(node=node.right, key=key)

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
        print_node(node=node)

        if node.left:
            self.preorder_traversal(node=node.left)

        if node.right:
            self.preorder_traversal(node=node.right)

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


# Print out all the details of a node
def print_node(node: Node) -> None:
    print(f"key: {node.key}")
    print(f"left: {node.left.key if node.left else node.left}")
    print(f"right: {node.right.key if node.right else node.right}")
    print(f"parent: {node.parent.key if node.parent else node.parent}")
    print(f"balance factor: {node.balance_factor}")
    print(f"root: {node.root}\n")


if __name__ == "__main__":
    # tree: AVLTree = AVLTree(key=10)
    # tree.insert(node=tree.node, key=20)
    # tree.insert(node=tree.node, key=30)

    # print("Initial\n")
    # tree.preorder_traversal(node=tree.node)

    # tree.left_rotation(node=tree.node)

    # print("After rotation\n")
    # tree.preorder_traversal(node=tree.node)
    # help(request=Node)
    help(request=AVLTree)
