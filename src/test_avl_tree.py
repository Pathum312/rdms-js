from avl_tree import AVLTree


class TestAVLTree:
    def test_tree_creation(self) -> None:
        # Create the tree.
        tree: AVLTree = AVLTree(key=10)

        # Test and validate the root node.
        assert tree.node.key is 10
        assert tree.node.root is True
        assert tree.node.left is None
        assert tree.node.right is None
        assert tree.node.parent is None

    def test_add_node(self) -> None:
        # Create the tree.
        tree: AVLTree = AVLTree(key=10)

        # Add the first child node.
        tree.insert(node=tree.node, key=20)

        # Add the second child node.
        tree.insert(node=tree.node, key=30)

        # Test and validate the first child node.
        assert tree.node.right.key is 20  # type: ignore
        assert tree.node.right.root is False  # type: ignore
        assert tree.node.right.left is None  # type: ignore
        assert tree.node.right.right.key is 30  # type: ignore
        assert tree.node.right.parent.key is 10  # type: ignore

        # Test and validate the second child node.
        assert tree.node.right.right.key is 30  # type: ignore
        assert tree.node.right.right.root is False  # type: ignore
        assert tree.node.right.right.left is None  # type: ignore
        assert tree.node.right.right.right is None  # type: ignore
        assert tree.node.right.right.parent.key is 20  # type: ignore
