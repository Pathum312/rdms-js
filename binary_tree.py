# from typing import Any

class Node:
    def __init__(self, content: dict[str, str | int]) -> None:
        self.left: Node | None = None
        self.right: Node | None = None
        self._content: dict[str, str | int] = content
        self._key: int = self.__getkey__(content=self._content)
    
    def __getkey__(self, content: dict[str, str | int]) -> int:
        return len(str(object=content))
    
    @property
    def key(self) -> int:
        return self._key
    
    @property
    def content(self) -> dict[str, str | int] | None:
        return self._content

class BinaryTree:
    def __init__(self, dbname: str) -> None:
        self._dbname: str = dbname
        self.root = Node(
            content={
                'dbname': self._dbname
            }
        )
    
    # Add a new node or update an existing node
    def insert(self, parent_node: Node, new_node: Node) -> None:
        # Add a left node
        if new_node.key < parent_node.key:
            if parent_node.left is None:
                parent_node.left = new_node
            else:
                self.insert(parent_node=parent_node.left, new_node=new_node)
        # Add a right node
        elif new_node.key > parent_node.key:
            if parent_node.right is None:
                parent_node.right = new_node
            else:
                self.insert(parent_node=parent_node.right, new_node=new_node)
        # If the node already exists, then update it
        else:
            parent_node = new_node
    
    def preorder_traversal(self, node: Node) -> None:
        print(f'Key: {node.key},\nContent: {node.content},\nleft: {node.left},\nright: {node.right}\n')
        
        if node.left:
            self.preorder_traversal(node=node.left)
        
        if node.right:
            self.preorder_traversal(node=node.right)
    
    # # Insert a new node or update the content of an existing node
    # def insert(self, content: dict[str, str | int]) -> None:
    #     key: int = self.__getkey__(content=content)
    #     # If current node has no left node, create left node
    #     # Or check the left node to create a new left node
    #     if key < self._key:
    #         if self.left is None:
    #             self.left = BinaryTree(content=content)
    #         else:
    #             self.left.insert(content=content)
    #     # If current node has no right node, create right node
    #     # Or check the right node to create a new right node
    #     elif key > self._key:
    #         if self.right is None:
    #             self.right = BinaryTree(content=content)
    #         else:
    #             self.right.insert(content=content)
    #     # If, it's the current node, just update the content
    #     else:
    #         self._content = content
    
    # def find_by_key(self, key: int) -> Any | dict[str, str | int] | None:
    #     if key < self._key:
    #         if self.left is not None:
    #             return self.left.find_by_key(key=key)
    #         else:
    #             return None
    #     elif key > self._key:
    #         if self.right is not None:
    #             return self.right.find_by_key(key=key)
    #         else:
    #             return None
    #     else:
    #         return {
    #             'key': self._key,
    #             'content': self._content
    #         }
    
    # def traverse_tree(self) -> None:
    #     print(f'Key: {self._key},\nContent: {self._content},\nleft: {self.left},\nright: {self.right}\n')
    #     if self.left:
    #         self.left.traverse_tree()
    #     if self.right:
    #         self.right.traverse_tree()

if __name__ == '__main__':
    book_tree: BinaryTree = BinaryTree(dbname='Book Database')
    book_tree.insert(
        parent_node=book_tree.root,
        new_node=Node(
            content={
                'title': 'Lord of the Rings',
                'price': 30
            }
        )
    )
    book_tree.insert(
        parent_node=book_tree.root,
        new_node=Node(
            content={
                'title': 'Harry Potter',
                'price': 20
            }
        )
    )
    book_tree.insert(
        parent_node=book_tree.root,
        new_node=Node(
            content={
                'title': 'Goosebumps',
                'price': 15
            }
        )
    )
    book_tree.insert(
        parent_node=book_tree.root,
        new_node=Node(
            content={
                'title': 'A returner\'s magic should be special',
                'price': 25
            }
        )
    )
    book_tree.insert(
        parent_node=book_tree.root,
        new_node=Node(
            content={
                'title': 'Dune',
                'price': 10
            }
        )
    )
    
    book_tree.preorder_traversal(node=book_tree.root)