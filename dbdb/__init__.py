import os
from .interface import DBDB
from io import BufferedRandom

# Opens the database file and will create a new file, if database file is not available.
# But will not overwrite an existing file.
def connect(dbname: str) -> DBDB:
    try:
        # Open the database file and read in binary mode.
        file: BufferedRandom = open(file=dbname, mode='r+b')
    except IOError:
        # Database file should be opened in read and write mode.
        # Database file, if it doesn't exist create one.
        fd: int = os.open(path=dbname, flags=os.O_RDWR | os.O_CREAT)
        # Creates a file according to the file descriptors, and opens in read in binary mode.
        file: BufferedRandom = os.fdopen(fd=fd, mode='r+b')
    
    return DBDB(file=file)