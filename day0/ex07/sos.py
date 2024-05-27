import sys


def main():
	morse = {
		" ": "/ ",
		"A": ".- ",
		"a": ".- ",
		"B": "-... ",
		"b": "-... ",
		"C": "-.-. ",
		"c": "-.-. ",
		"D": "-.. ",
		"d": "-.. ",
		"E": ". ",
		"e": ". ",
		"F": "..-. ",
		"f": "..-. ",
		"G": "--. ",
		"g": "--. ",
		"H": ".... ",
		"h": ".... ",
		"I": ".. ",
		"i": ".. ",
		"J": ".--- ",
		"j": ".--- ",
		"K": "-.- ",
		"k": "-.- ",
		"L": ".-.. ",
		"l": ".-.. ",
		"M": "-- ",
		"m": "-- ",
		"N": "-. ",
		"n": "-. ",
		"O": "--- ",
		"o": "--- ",
		"P": ".--. ",
		"p": ".--. ",
		"Q": "--.- ",
		"q": "--.- ",
		"R": ".-. ",
		"r": ".-. ",
		"S": "... ",
		"s": "... ",
		"T": "- ",
		"t": "- ",
		"U": "..- ",
		"u": "..- ",
		"V": "...- ",
		"v": "...- ",
		"W": ".-- ",
		"w": ".-- ",
		"X": "-..- ",
		"x": "-..- ",
		"Y": "-.-- ",
		"y": "-.-- ",
		"Z": "--.. ",
		"z": "--.. ",
		"1": ".---- ",
		"2": "..--- ",
		"3": "...-- ",
		"4": "....- ",
		"5": "..... ",
		"6": "-.... ",
		"7": "--... ",
		"8": "---.. ",
		"9": "----. ",
		"0": "----- "
	}
	try:
		assert len(sys.argv) == 2, "AssertionError: the arguments are bad"
		for char in sys.argv[1]:
			if char not in morse.keys():
				raise AssertionError("AssertionError: the arguments are bad")
	except AssertionError as e:
		print(e)
		sys.exit(0)
	for i, char in enumerate(sys.argv[1]):
		if i == len(sys.argv[1]) - 1:
			print(morse[char].replace(" ", ""))
		else:
			print(morse[char], end="")


if __name__ == "__main__":
	main()
