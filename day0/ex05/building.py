import sys


def main():
    try:
        assert len(sys.argv) <= 2, "AssertionError: max one arguments required"
    except AssertionError as e:
        print(e)
        exit(1)
    if len(sys.argv) == 1:
        str = input("What is the text to count?\n")
    else:
        str = sys.argv[1]
    print(f"The text contains {len(str)} characters:")
    upper = 0
    lower = 0
    punctuation = 0
    digit = 0
    spaces = 0
    for char in str:
        if char.isupper():
            upper += 1
        elif char.islower():
            lower += 1
        elif char.isspace():
            spaces += 1
        elif char.isdigit():
            digit += 1
        else:
            punctuation += 1

    print(f"{upper} upper letters")
    print(f"{lower} lower letters")
    print(f"{punctuation} punctuations marks")
    print(f"{spaces} spaces")
    print(f"{digit} digits")


if __name__ == "__main__":
    main()
