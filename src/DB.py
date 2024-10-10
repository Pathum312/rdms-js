import argparse
import os
from argparse import ArgumentParser, Namespace

from avl_tree import AVLTree, Node
from storage import StoreAVLTree


def store_node(root: Node, filename: str) -> None:
    """
    Store the AVL tree in the DB file.

    Attributes:
        root (Node): Root node of the AVL tree.
        filename (str): Path to the DB file.

    Returns:
        None
    """
    storage: StoreAVLTree = StoreAVLTree()
    # Serialize the AVL tree into a node str
    nodes: str = storage.serialize(root=root)
    # Save the node str in the DB file.
    filename = filename.split(sep="./DB/")[1]
    storage.store(nodes=nodes, filename=filename)


def read_nodes(filename: str) -> AVLTree:
    """
    Retrieve the AVL tree from the DB.

    Attibutes:
        filename (str): Path to the DB file.

    Returns:
        AVLTree
    """
    storage: StoreAVLTree = StoreAVLTree()
    # Retrieve the DB file and get the node str.
    nodes: str = storage.read(filename=filename)
    # Deserialize the node str and get the AVL tree.
    tree: AVLTree = storage.deserialize(nodes=nodes)
    return tree


def add(key: int, filename: str) -> None:
    """
    Add a node and visualize the added node.

    Attributes:
        key (int): Value of the node.
        filename (str): Path to the DB file.

    Returns:
        None
    """
    if not os.path.exists(path=filename):
        tree: AVLTree = AVLTree(key=key)
        store_node(root=tree.node, filename=filename)
        tree.show(node=tree.node)
    else:
        tree: AVLTree = read_nodes(filename=filename)
        tree.insert(key=key)
        store_node(root=tree.node, filename=filename)

        saved_tree: AVLTree = read_nodes(filename=filename)
        saved_tree.show(node=saved_tree.node)


def show(filename: str) -> None:
    """
    Retrieve the AVL tree and visualize the tree.

    Attributes:
        filename (str): Path to the DB file.

    Returns:
        None
    """
    if os.path.exists(path=filename):
        tree: AVLTree = read_nodes(filename=filename)
        tree.show(node=tree.node)
    else:
        print("\nDB file give, doesn't exist.\n")


def main() -> None:
    parser: ArgumentParser = argparse.ArgumentParser(description="DB Management System")

    subparsers = parser.add_subparsers(dest="command", help="Commands: show")

    add_parser: ArgumentParser = subparsers.add_parser(
        name="add", help="Add a node in the AVL tree."
    )
    add_parser.add_argument("key", type=int, help="Key of the node.")
    add_parser.add_argument("filename", type=str, help="Path to the DB file.")

    show_parser: ArgumentParser = subparsers.add_parser(
        name="show", help="Show AVL tree."
    )
    show_parser.add_argument("filename", type=str, help="Path to the DB file.")

    args: Namespace = parser.parse_args()

    if args.command == "show":
        show(filename=args.filename)
    elif args.command == "add":
        add(key=args.key, filename=args.filename)


if __name__ == "__main__":
    main()
