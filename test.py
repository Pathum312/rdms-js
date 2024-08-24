from typing import Any

class BinaryTree:
    def __init__(self, key: int, content: dict[str, str | int] | None = None) -> None:
        self.left: BinaryTree | None = None
        self.right: BinaryTree | None = None
        self._key: int = key
        self._content: dict[str, str | int] | None = content
    
    # Insert a new node or update the content of an existing node
    def insert(self, key: int, content: dict[str, str | int] | None = None) -> None:
        # If current node has no left node, create left node
        # Or check the left node to create a new left node
        if key < self._key:
            if self.left is None:
                self.left = BinaryTree(key=key, content=content)
            else:
                self.left.insert(key=key, content=content)
        # If current node has no right node, create right node
        # Or check the right node to create a new right node
        elif key > self._key:
            if self.right is None:
                self.right = BinaryTree(key=key, content=content)
            else:
                self.right.insert(key=key, content=content)
        # If, it's the current node, just update the content
        else:
            self._content = content
    
    def find_by_key(self, key: int) -> Any | dict[str, str | int] | None:
        if key < self._key:
            if self.left is not None:
                return self.left.find_by_key(key=key)
            else:
                return None
        elif key > self._key:
            if self.right is not None:
                return self.right.find_by_key(key=key)
            else:
                return None
        else:
            return {
                'key': self._key,
                'content': self._content
            }
    
    def traverse_tree(self) -> None:
        print(f'Key: {self.key},\nContent: {self.content},\nleft: {self.left},\nright: {self.right}\n')
        if self.left:
            self.left.traverse_tree()
        if self.right:
            self.right.traverse_tree()
    
    @property
    def key(self) -> int:
        return self._key
    
    @property
    def content(self) -> dict[str, str | int] | None:
        return self._content

if __name__ == '__main__':
    tree: BinaryTree = BinaryTree(key=0, content={'name': 'Book Database'})
    tree.insert(
        key=1,
        content={
            'title': 'Lord of the Rings',
            'price': 20 
        }
    )
    tree.insert(
        key=2,
        content={
            'title': 'Harry Potter',
            'price': 30 
        }
    )
    
    # tree.traverse_tree()
    data: Any | dict[str, str | int] | None = tree.find_by_key(key=2)
    if data:
        print(f'key: {data['key']}')