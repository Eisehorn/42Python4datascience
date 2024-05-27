import sys
import numpy as np


def slice_me(family: list, start: int, end: int) -> list:
	try:
		if type(family) is not list:
			raise TypeError("Input must be a list!")
		my_family = np.array(family)
		if my_family.shape[1] != 2:
			raise TypeError("Columns must have two elements!")
		if start < 0:
			start *= -1
		if end < 0:
			end *= -1
		if start >= end:
			raise AssertionError("End must be higher than start!")
		new_family = np.zeros((end - start, 2))
		print(f"My shape is: {my_family.shape}")
		print(f"My new shape is: {new_family.shape}")
		j = 0
		for index, value in enumerate(my_family):
			if start <= index < end:
				new_family[j] = value
				j += 1
	except ValueError as e:
		print(e)
		sys.exit(1)
	except AssertionError as e:
		print(e)
		sys.exit(1)
	except TypeError as e:
		print(e)
		sys.exit(1)
	return new_family.tolist()
