from logging import (
    DEBUG,
    ERROR,
    INFO,
    FileHandler,
    Formatter,
    Logger,
    StreamHandler,
    getLogger,
)

from utils import validate_dir


def LOGGER(_name: str, _filename: str) -> Logger:
    """
    Used to log critical points in the code exexution.

    Parameters:
        _name (str): Name of the logger.
        _filename (str): Name of the log file.

    Returns:
        Logger: An Logger object is returned.
    """
    # Create a logger for _name.
    logger: Logger = getLogger(name=_name)
    logger.setLevel(level=INFO)

    # File handler, which logs even debug logs.
    filepath: str = validate_dir(filename=_filename, type="LOG")
    file_handler = FileHandler(filename=filepath)
    file_handler.setLevel(level=DEBUG)

    # Console handler with higher log level.
    console_handler = StreamHandler()
    console_handler.setLevel(level=ERROR)

    # Format for the logs and is added to the handlers.
    FORMAT = "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
    formatter = Formatter(fmt=FORMAT)
    file_handler.setFormatter(fmt=formatter)
    console_handler.setFormatter(fmt=formatter)

    # Add the handlers to the logger.
    logger.addHandler(hdlr=file_handler)
    logger.addHandler(hdlr=console_handler)

    return logger


if __name__ == "__main__":
    logger: Logger = LOGGER(_name="test.py", _filename="tests.log")
    logger.info(msg="Testing Start")
    logger.info(msg="Testing...")
    logger.error(msg="Testing Failed")
    logger.info(msg="Testing Ended")
