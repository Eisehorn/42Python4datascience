def ft_filter(y, words):
    words_to_print = []
    for word in words:
        if y(word) is True:
            words_to_print.append(word)
    return words_to_print
