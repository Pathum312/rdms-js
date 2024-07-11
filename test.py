proceed: bool = True

def start() -> None:
    # global proceed
    # proceed = False

    if proceed is True:
        print('Proceed...')

    if proceed is not True:
        print('Cannot proceed...')

if __name__ == "__main__":
    start()

