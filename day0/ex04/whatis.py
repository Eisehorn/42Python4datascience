import sys


def whatis(argument):
    try:
        int(argument)
        if argument % 2 == 0:
            print(f"{argument} is even")
        else:
            print(f"{argument} is odd")
    except ValueError:
        print("AssertionError: argument is not an integer")


try:
    assert len(sys.argv) >= 2, ""
except AssertionError:
    exit(0)

try:
    assert len(sys.argv) <= 2, "AssertionError: more than one argument is provided"
except AssertionError as e:
    print(e)
    exit(0)

whatis(sys.argv[1])
