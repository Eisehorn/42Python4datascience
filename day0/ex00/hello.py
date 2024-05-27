ft_list = ["Hello", "tata!"]
ft_tuple = ("Hello", "toto!")
ft_set = {"Hello", "tutu!"}
ft_dict = {"Hello": "titi!"}



ft_list[1] = "World"
my_list = list(ft_tuple)
my_list[1] = "Italy"
ft_tuple = tuple(my_list)
ft_set.remove("tutu!")
ft_set.add("Milan")
ft_dict["Hello"] = "42Milan"


print(ft_list)
print(ft_tuple)
print(ft_set)
print(ft_dict)
