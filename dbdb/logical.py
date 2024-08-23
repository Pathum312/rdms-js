class LogicalBase(object):
    node_ref_class = None 
    
    def __init__(self, storage: str) -> None:
        self._storage: str = storage
    
    # Checks if the storage is locked
    def get(self, key: str) -> str:
        if not self._storage:
            ...
        
        return ''
    
    def _refresh_tree_ref(self):
        ...