proceed: bool = True
sample: list[int] = [1, 2, 3, 4]

def main() -> None:
    # global proceed
    # proceed = False

    if proceed is True:
        print('Proceed...')

    if proceed is not True:
        print('Cannot proceed...')

def test() -> None:
    ...

if __name__ == "__main__":
    main()