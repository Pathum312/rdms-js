from io import TextIOWrapper
from logging import Logger

from avl_tree import AVLTree, Node
from logger import LOGGER
from utils import validate_dir


class StoreAVLTree:
    """
    Manage the DB files.
    """

    def __init__(self) -> None:
        """
        Initializes a StoreAVLTree object.
        """

        filename: str = "storage.log"
        self.logger: Logger = LOGGER(_name="storage.StoreAVLTree", _filename=filename)
        self.logger.info(msg=f"Creating a log file...")
        self.logger.info(msg=f"Log file {filename} was created.")

    def serialize(self, root: Node) -> str:
        """
        Serialize a AVL tree int oa single str.

        Attributes:
            root (Node): Pass the root node of the tree.

        Returns:
            None
        """

        if not root:
            return

        self.logger.info(msg=f"Serializing the AVL tree...")

        # Queue of nodes to loop through.
        stack: list[Node] = [root]
        # Nodes to be serialized.
        nodes: list[str] = []

        while stack:
            current: Node = stack.pop()

            if not current:
                continue
            else:
                nodes.append(str(object=current.key))
                stack.append(current.right)  # type: ignore
                stack.append(current.left)  # type: ignore

        # Convert the list[str] into a single str.
        serialized_tree: str = ",".join(nodes)

        self.logger.info(msg=f"Serialized AVL Tree: {serialized_tree}.")

        return serialized_tree

    def deserialize(self, nodes: str) -> AVLTree:
        """
        Deserialize the single str into an AVL tree.

        Attributes:
            nodes (str): Serialized str of nodes.

        Returns:
            AVLTree: Returns an AVLTree object.
        """

        self.logger.info(msg=f"Deserializing the AVL tree...")

        # Convert the str into an usable list[int].
        deserialized_nodes: list[int] = list(map(int, nodes.split(sep=",")))

        # Get the root from the deserialized nodes list.
        root_key: int = deserialized_nodes.pop(0)
        # Create a AVL tree with the root ey.
        tree: AVLTree = AVLTree(key=root_key)

        # If the deserialized nodes list is not empty.
        while deserialized_nodes:
            # The the first value from the list.
            key: int = deserialized_nodes.pop(0)
            # Add the key as a node in the AVL tree.
            tree.insert(key=key)

        self.logger.info(msg=f"Deserialized the AVL tree.")

        # Return the created AVL tree.
        return tree

    def store(self, nodes: str, filename: str) -> None:
        """
        Save the str of nodes in the DB file.

        Attributes:
            nodes (str): Serialized str of nodes.
            filename (str): DB file path.

        Returns:
            None
        """

        self.logger.info(msg=f"Creating DB file {filename}...")

        # Get file path to the DB file.
        filepath: str = validate_dir(filename=filename, type="DB")

        self.logger.info(msg=f"DB file created: {filepath}")

        # Open the DB file in write mode
        DB: TextIOWrapper = open(file=filepath, mode="w")
        # Save the AVL tree to the DB.
        DB.write(nodes)

        self.logger.info(msg=f"AVL tree saved in {filepath}.")

    def read(self, filename: str) -> str:
        """
        Retrieves the serialized str of nodes from the DB file.

        Attributes:
            filename (str): Path to the DB file.

        Returns:
            str: Returns the serialized str of nodes.
        """

        self.logger.info(msg=f"Opening DB file {filename}...")

        # Open the DB file in read mode
        DB: TextIOWrapper = open(file=filename, mode="r")

        self.logger.info(msg=f"AVL tree retrieved from {filename}.")

        # Return the AVL tree nodes.
        return DB.read()


if __name__ == "__main__":
    tree: AVLTree = AVLTree(key=42)
    tree.insert(key=7)
    tree.insert(key=86)
    tree.insert(key=23)
    tree.insert(key=15)
    tree.insert(key=91)
    tree.insert(key=34)

    storage: StoreAVLTree = StoreAVLTree()
    nodes: str = storage.serialize(root=tree.node)
    storage.store(nodes=nodes, filename="tree1.txt")
    nodes: str = storage.read(filename="./DB/tree1.txt")
    tree1: AVLTree = storage.deserialize(nodes=nodes)
    tree1.show(node=tree1.node)
