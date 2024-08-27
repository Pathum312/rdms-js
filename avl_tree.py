class Node:
    def __init__(self, key: int) -> None:
        self._key: int = key
        self.left: Node | None = None
        self.right: Node | None = None
        self.balance_factor: int = 0
        self.parent: Node | None = None
        self.root: bool = False
    
    @property
    def key(self) -> int:
        return self._key

class AVLTree:
    def __init__(self, key: int) -> None:
        self._key: int = key
        self.node: Node = Node(key=self._key)
        self.node.root = True
    
    def insert(self, node: Node, key: int) -> None:
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
    
    def preorder_traversal(self, node: Node) -> None:
        node.balance_factor = self.calculate_balance_factor(node=node)
        print_node(node=node)
        
        if node.left:
            self.preorder_traversal(node=node.left)
        
        if node.right:
            self.preorder_traversal(node=node.right)
    
    def max_depth(self, node: Node | None) -> int:
        if node is None:
            return 0
        else:
            ldepth: int = self.max_depth(node=node.left)
            rdepth: int = self.max_depth(node=node.right)
            
            return max(ldepth, rdepth) + 1
    
    def calculate_balance_factor(self, node: Node) -> int:
        left_height: int = self.max_depth(node=node.left)
        right_height: int = self.max_depth(node=node.right)
        
        return left_height - right_height

def print_node(node: Node) -> None:
    print(f'key: {node.key}')
    print(f'left: {node.left.key if node.left else node.left}')
    print(f'right: {node.right.key if node.right else node.right}')
    print(f'parent: {node.parent.key if node.parent else node.parent}')
    print(f'balance factor: {node.balance_factor}')
    print(f'root: {node.root}\n')

if __name__ == '__main__':
    tree: AVLTree = AVLTree(key=20)
    tree.insert(node=tree.node, key=10)
    tree.insert(node=tree.node, key=30)
    tree.insert(node=tree.node, key=5)
    tree.insert(node=tree.node, key=1)
    tree.insert(node=tree.node, key=4)
    tree.insert(node=tree.node, key=6)
    tree.insert(node=tree.node, key=3)
    
    tree.preorder_traversal(node=tree.node)