from io import BufferedRandom

class DBDB(object):
    def __init__(self, file: BufferedRandom) -> None:
        self._storage: str = '' # Storage(f)
        self._tree: str = self._storage # BinaryTree(self._storage)
    
    def __getitem__(self, key: str) -> str:
        self._assert_not_closed()
        return key # return self._tree.get(key)
    
    # Check if the database is closed
    def _assert_not_closed(self) -> None:
        # if self._storage.closed:
        if self._storage:
            raise ValueError('Databse closed.')