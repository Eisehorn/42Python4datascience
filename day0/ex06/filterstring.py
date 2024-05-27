import string
import sys
from ft_filter import ft_filter


def main():
    try:
        assert len(sys.argv) == 3, "AssertionError: the arguments are bad"
    except AssertionError as e:
        print(e)
        exit(0)
    try:
        int(sys.argv[2]),
    except ValueError:
        print("AssertionError: the arguments are bad")
        exit(0)
    for char in sys.argv[1]:
        if char in string.punctuation:
            return
    n = int(sys.argv[2])
    words = [x for x in sys.argv[1].split(' ')]
    print(ft_filter(lambda y: len(y) > n, words))


if __name__ == "__main__":
    main()
