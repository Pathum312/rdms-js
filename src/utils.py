import os


def validate_dir(filename: str, type: str) -> str:
    """
    Checks if the file directory exists.

    Parameters:
        filename (str): Name of the log/txt file.
        type (str): Send LOG to add a .log file, or DB to add a .txt file.

    Returns:
        str: Returns the filepath to the log/txt file.
    """
    # Log files directory.
    file_dir: str = "./logs/" if type is "LOG" else "./DB/"
    # Path to the log file.
    filepath: str = os.path.join(file_dir, filename)

    # If the file directory doesn't exist, create the directory.
    if not os.path.exists(path=file_dir):
        os.makedirs(name=file_dir)

    return filepath
