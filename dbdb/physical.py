import struct
import portalocker
from io import BufferedRandom

class Storage(object):
    def __init__(self, file: BufferedRandom) -> None:
        self._file: BufferedRandom = file
        self.locked = False
    
    # Lock the database file
    def lock(self) -> bool:
        if not self.locked:
            portalocker.lock(file_=self._file, flags=portalocker.LOCK_EX) # type: ignore
            self.locked = True
            return True
        else:
            return False
    
    # Unlock the database file
    def unlock(self) -> None:
        if self.locked:
            self._file.flush()
            portalocker.unlock(file_=self._file) # type: ignore
            self.locked = False