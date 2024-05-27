import pandas as pd
from load_csv import load
from matplotlib import pyplot as plt


def print_graph(years, italy_life_expectancy):
	plt.plot(years, italy_life_expectancy)
	plt.xlabel('Year')
	plt.ylabel('Life Expectancy')
	plt.xticks(range(int(years.min()), int(years.max()), 40))
	plt.title('Italy Life expectancy Projections')
	plt.show()


def main():
	df = pd.read_csv('../life_expectancy_years.csv', header=None)
	italy_row_index = df[df.iloc[:, 0] == 'Italy'].index[0]
	italy_life_expectancy = df.iloc[italy_row_index, 1:]
	df = df.T
	years = df.iloc[1:, 0]
	italy_life_expectancy = pd.to_numeric(italy_life_expectancy)
	print_graph(years, italy_life_expectancy)


if __name__ == '__main__':
	main()
