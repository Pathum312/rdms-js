from logging import Logger

from avl_tree import AVLTree, Node
from logger import LOGGER


class StoreAVLTree:
    def __init__(self) -> None:
        self.logger: Logger = LOGGER(
            _name="storage.StoreAVLTree", _filename="storage.log"
        )
        self.logger.info(msg=f"Creating a storage...")

    def serialize(self, root: Node) -> None:
        if not root:
            return

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

        print(",".join(nodes))


if __name__ == "__main__":
    tree: AVLTree = AVLTree(key=30)
    tree.insert(key=20)
    tree.insert(key=10)
    tree.insert(key=8)
    tree.insert(key=6)
    tree.insert(key=5)
    tree.insert(key=4)

    storage: StoreAVLTree = StoreAVLTree()
    storage.serialize(root=tree.node)
