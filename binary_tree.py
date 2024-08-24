class Node:
    def __init__(self, key: int, value: int | str) -> None:
        self.left: Node | None = None
        self.right: Node | None = None
        self._key: int = key
        self._value: int | str = value
    
    @property
    def key(self) -> int:
        return self._key
    
    @property
    def value(self) -> int | str:
        return self._value

class BinaryTree:
    def __init__(self, key: int, value: int | str) -> None:
        self.node: Node = Node(key=key, value=value)
    
    def insert(self, node: Node, key: int, value: int | str) -> None:
        if key < node.key:
            if node.left is None:
                node.left = Node(key=key, value=value)
            else:
                self.insert(node=node.left, key=key, value=value)
        else:
            if node.right is None:
                node.right = Node(key=key, value=value)
            else:
                self.insert(node=node.right, key=key, value=value)
    
    def find(self, node: Node | None, key: int) -> str:
        while node is not None:
            if key < node.key:
                node = node.left
            elif key > node.key:
                node = node.right
            else:
                return f'key: {node.key},\nnode: {node.value}\n'
        
        raise KeyError
    
    def inorder_traversal(self, node: Node) -> None:
        if node.left:
            self.inorder_traversal(node=node.left)
        print(f'key: {node.key},\nnode: {node.value}\n')
        if node.right:
            self.inorder_traversal(node=node.right)
    
    def preorder_traversal(self, node: Node) -> None:
        print(f'key: {node.key},\nnode: {node.value}\n')
        if node.left:
            self.preorder_traversal(node=node.left)
        if node.right:
            self.preorder_traversal(node=node.right)
    
    def postorder_traversal(self, node: Node) -> None:
        if node.left:
            self.postorder_traversal(node=node.left)
        if node.right:
            self.postorder_traversal(node=node.right)
        print(f'key: {node.key},\nnode: {node.value}\n')

def log_node(node: Node | None) -> None:
    if node is None:
        print('Node does not exist.\n')
    else:
        print({
            'left': node.left,
            'right': node.right,
            'key': node.key,
            'value': node.value,
        })

if __name__ == '__main__':
    print('## Binary Tree Demo\n')
    
    tree: BinaryTree = BinaryTree(key=5, value='Hello World!')
    tree.insert(node=tree.node, key=6, value='Right')
    tree.insert(node=tree.node, key=4, value='Left')
    tree.insert(node=tree.node, key=8, value='Right2')
    
    print('## Inorder Traversal\n')
    tree.inorder_traversal(node=tree.node)
    
    print('## Preorder Traversal\n')
    tree.preorder_traversal(node=tree.node)
    
    print('## Postorder Traversal\n')
    tree.postorder_traversal(node=tree.node)
    
    print('## Find key: 8\n')
    print(tree.find(node=tree.node, key=8))
    
    print('## Find key: 5\n')
    print(tree.find(node=tree.node, key=5))
    
    print('## Find key: 4\n')
    print(tree.find(node=tree.node, key=4))