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
    
    def right_rotation(self, node: Node) -> None:
        parent_node: Node = node
        child_node: Node = node.left # type: ignore
        
        self.swap_parent(parent_node=parent_node, child_node=child_node)
        
        parent_node.left = None
        parent_node.parent = child_node
        
        child_node.right = parent_node
    
    def left_rotation(self, node: Node) -> None:
        parent_node: Node = node
        child_node: Node = node.right # type: ignore
        
        self.swap_parent(parent_node=parent_node, child_node=child_node)
        
        parent_node.right = None
        parent_node.parent = child_node
        
        child_node.left = parent_node
    
    def left_right_rotation(self, node: Node) -> None:
        parent_node: Node = node
        child_node: Node = node.left # type: ignore
        
        self.left_rotation(node=child_node)
        self.right_rotation(node=parent_node)
    
    def swap_parent(self, parent_node: Node, child_node: Node) -> None:
        if parent_node.root:
            parent_node.root = False
            
            child_node.root = True
            child_node.parent = None
            self.node = child_node
        else:
            child_node.parent = parent_node.parent
    
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

# Print out all the details of a node
def print_node(node: Node) -> None:
    print(f'key: {node.key}')
    print(f'left: {node.left.key if node.left else node.left}')
    print(f'right: {node.right.key if node.right else node.right}')
    print(f'parent: {node.parent.key if node.parent else node.parent}')
    print(f'balance factor: {node.balance_factor}')
    print(f'root: {node.root}\n')

if __name__ == '__main__':
    tree: AVLTree = AVLTree(key=10)
    tree.insert(node=tree.node, key=20)
    tree.insert(node=tree.node, key=30)
    
    print('Initial\n')
    tree.preorder_traversal(node=tree.node)
    
    tree.left_rotation(node=tree.node)
    
    print('After rotation\n')
    tree.preorder_traversal(node=tree.node)