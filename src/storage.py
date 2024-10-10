from io import TextIOWrapper
from logging import Logger

from avl_tree import AVLTree, Node
from logger import LOGGER
from utils import validate_dir


class StoreAVLTree:
    def __init__(self) -> None:
        filename: str = "storage.log"
        self.logger: Logger = LOGGER(_name="storage.StoreAVLTree", _filename=filename)
        self.logger.info(msg=f"Creating a log file...")
        self.logger.info(msg=f"Log file {filename} was created.")

    def serialize(self, root: Node) -> str:
        if not root:
            return

        self.logger.info(msg=f"Serializing the AVL tree...")

        stack: list[Node] = [root]
        nodes: list[str] = []

        while stack:
            current: Node = stack.pop()

            if not current:
                continue
            else:
                nodes.append(str(object=current.key))
                stack.append(current.right)  # type: ignore
                stack.append(current.left)  # type: ignore

        serialized_tree: str = ",".join(nodes)

        self.logger.info(msg=f"Serialized AVL Tree: {serialized_tree}.")

        return serialized_tree

    def store(self, nodes: str, filename: str) -> None:
        # Get file path to the DB file.
        filepath: str = validate_dir(filename=filename, type="DB")
        # Open the DB file in write mode
        DB: TextIOWrapper = open(file=filepath, mode="w")
        # Save the AVL tree to the DB.
        DB.write(nodes)

    def read(self, filename: str) -> str:
        # Open the DB file in read mode
        DB: TextIOWrapper = open(file=filename, mode="r")

        # Return the AVL tree nodes.
        return DB.read()


if __name__ == "__main__":
    tree: AVLTree = AVLTree(key=30)
    tree.insert(key=20)
    tree.insert(key=10)
    tree.insert(key=8)
    tree.insert(key=6)
    tree.insert(key=5)
    tree.insert(key=4)

    storage: StoreAVLTree = StoreAVLTree()
    nodes: str = storage.serialize(root=tree.node)
    storage.store(nodes=nodes, filename="tree1.txt")
    nodes: str = storage.read(filename="./DB/tree1.txt")
    print(nodes)
