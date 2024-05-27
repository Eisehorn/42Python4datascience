def count_list(list, occurrence):
	count_occurrence = 0
	for element in list:
		if element == occurrence:
			count_occurrence += 1
	return count_occurrence
