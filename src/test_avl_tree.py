from avl_tree import AVLTree


class TestAVLTree:
    """
    Tests the AVL tree functions
    """

    def test_tree_creation(self) -> None:
        """
        Tests and validates whether, the tree was created successfully.

        Returns:
            None
        """
        # Create the tree.
        tree: AVLTree = AVLTree(key=10)

        # Test and validate the root node.
        assert tree.node.key is 10
        assert tree.node.root is True
        assert tree.node.left is None
        assert tree.node.right is None
        assert tree.node.parent is None

    def test_node_insertion(self) -> None:
        """
        Validating whether, the node was added correctly.

        Returns:
            None
        """

        # Create the tree.
        tree: AVLTree = AVLTree(key=10)

        # Add a node.
        tree.insert(key=20)

        # Validate the root node.
        assert tree.node.key is 10  # type: ignore
        assert tree.node.root is True  # type: ignore
        assert tree.node.left is None  # type: ignore
        assert tree.node.right.key is 20  # type: ignore
        assert tree.node.parent is None  # type: ignore

        # Validate the child node.
        assert tree.node.right.key is 20  # type: ignore
        assert tree.node.right.root is False  # type: ignore
        assert tree.node.right.left is None  # type: ignore
        assert tree.node.right.right is None  # type: ignore
        assert tree.node.right.parent.key is 10  # type: ignore

    def test_right_rotation(self) -> None:
        """
        Testing whether, the right rotation logic works.

        Returns:
            None
        """

        # Create a AVL Tree.
        tree: AVLTree = AVLTree(key=30)
        tree.insert(key=20)
        tree.insert(key=10)

        # Validate the root node.
        assert tree.node.key is 20  # type: ignore
        assert tree.node.root is True  # type: ignore
        assert tree.node.left.key is 10  # type: ignore
        assert tree.node.right.key is 30  # type: ignore
        assert tree.node.parent is None  # type: ignore

        # Validate the left child node.
        assert tree.node.left.key is 10  # type: ignore
        assert tree.node.left.root is False  # type: ignore
        assert tree.node.left.left is None  # type: ignore
        assert tree.node.left.right is None  # type: ignore
        assert tree.node.left.parent.key is 20  # type: ignore

        # Validate the right child node.
        assert tree.node.right.key is 30  # type: ignore
        assert tree.node.right.root is False  # type: ignore
        assert tree.node.right.left is None  # type: ignore
        assert tree.node.right.right is None  # type: ignore
        assert tree.node.right.parent.key is 20  # type: ignore

    def test_left_rotation(self) -> None:
        """
        Testing whether, the left rotation logic works.

        Returns:
            None
        """

        # Create a AVL Tree.
        tree: AVLTree = AVLTree(key=10)
        tree.insert(key=20)
        tree.insert(key=30)

        # Validate the root node.
        assert tree.node.key is 20  # type: ignore
        assert tree.node.root is True  # type: ignore
        assert tree.node.left.key is 10  # type: ignore
        assert tree.node.right.key is 30  # type: ignore
        assert tree.node.parent is None  # type: ignore

        # Validate the left child node.
        assert tree.node.left.key is 10  # type: ignore
        assert tree.node.left.root is False  # type: ignore
        assert tree.node.left.left is None  # type: ignore
        assert tree.node.left.right is None  # type: ignore
        assert tree.node.left.parent.key is 20  # type: ignore

        # Validate the right child node.
        assert tree.node.right.key is 30  # type: ignore
        assert tree.node.right.root is False  # type: ignore
        assert tree.node.right.left is None  # type: ignore
        assert tree.node.right.right is None  # type: ignore
        assert tree.node.right.parent.key is 20  # type: ignore

    def test_left_right_rotation(self) -> None:
        """
        Testing whether, the left-right rotation logic works.

        Returns:
            None
        """

        # Create a AVL Tree.
        tree: AVLTree = AVLTree(key=30)
        tree.insert(key=10)
        tree.insert(key=20)

        # Validate the root node.
        assert tree.node.key is 20  # type: ignore
        assert tree.node.root is True  # type: ignore
        assert tree.node.left.key is 10  # type: ignore
        assert tree.node.right.key is 30  # type: ignore
        assert tree.node.parent is None  # type: ignore

        # Validate the left child node.
        assert tree.node.left.key is 10  # type: ignore
        assert tree.node.left.root is False  # type: ignore
        assert tree.node.left.left is None  # type: ignore
        assert tree.node.left.right is None  # type: ignore
        assert tree.node.left.parent.key is 20  # type: ignore

        # Validate the right child node.
        assert tree.node.right.key is 30  # type: ignore
        assert tree.node.right.root is False  # type: ignore
        assert tree.node.right.left is None  # type: ignore
        assert tree.node.right.right is None  # type: ignore
        assert tree.node.right.parent.key is 20  # type: ignore

    def test_right_left_rotation(self) -> None:
        """
        Testing whether, the right-left rotation logic works.

        Returns:
            None
        """

        # Create a AVL Tree.
        tree: AVLTree = AVLTree(key=10)
        tree.insert(key=30)
        tree.insert(key=20)

        # Validate the root node.
        assert tree.node.key is 20  # type: ignore
        assert tree.node.root is True  # type: ignore
        assert tree.node.left.key is 10  # type: ignore
        assert tree.node.right.key is 30  # type: ignore
        assert tree.node.parent is None  # type: ignore

        # Validate the left child node.
        assert tree.node.left.key is 10  # type: ignore
        assert tree.node.left.root is False  # type: ignore
        assert tree.node.left.left is None  # type: ignore
        assert tree.node.left.right is None  # type: ignore
        assert tree.node.left.parent.key is 20  # type: ignore

        # Validate the right child node.
        assert tree.node.right.key is 30  # type: ignore
        assert tree.node.right.root is False  # type: ignore
        assert tree.node.right.left is None  # type: ignore
        assert tree.node.right.right is None  # type: ignore
        assert tree.node.right.parent.key is 20  # type: ignore
