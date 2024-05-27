def ft_tqdm(lst: range) -> None:
    tot = len(lst)
    pr = 0
    w = 100
    for elem in lst:
        yield elem
        pr += 1
        p = int(pr * 100 / tot)
        print("\r{}".format(f"{p}%"+"|["+"="*(p - 1)+">"+" "*(w - p) + "]|"
                            + f"Progress: {p}/{tot}"), end="")
