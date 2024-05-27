def NULL_not_found(object : any) -> int:
    if object is None:
        print("Nothing: None", type(object))
    elif type(object) is float and object != object:
        print("Cheese: nan", type(object))
    elif object is False:
        print("Fake: False", type(object))
    elif object == 0:
        print("Zero: 0", type(object))
    elif object == "":
        print("Empty: ", type(object))
    else:
        print("Type not found")
        return 1
    return 0

