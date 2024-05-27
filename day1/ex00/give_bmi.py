import sys


def give_bmi(height: list[int | float], weight: list[int | float]) -> list[int | float]:
	try:
		if len(height) != len(weight):
			raise AssertionError("AssertionError: bad arguments")
		bmi = []
		for i, j in zip(height, weight):
			if type(i) is not (int and float) or type(j) is not (int and float):
				raise AssertionError("AssertionError: bad arguments")
			if i == 0:
				raise AssertionError("AssertionError: bad arguments")
			bmi.append(j/pow(i, 2))
	except AssertionError as e:
		print(e)
		sys.exit(1)
	return bmi


def apply_limit(bmi: list[int | float], limit: int) -> list[bool]:
	try:
		if limit == 0:
			raise AssertionError("AssertionError: bad arguments")
		perc = []
		for i in bmi:
			perc.append(i > limit)
	except AssertionError as e:
		print(e)
		sys.exit(1)
	return perc
