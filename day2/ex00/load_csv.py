import sys
from pandas import read_csv, DataFrame


def load(path: str) -> DataFrame:
	try:
		df = read_csv(path)
		print('Loading dataframe of dimensions', df.shape)
		return df
	except FileNotFoundError as e:
		print(e)
		sys.exit(1)
