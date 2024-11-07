items = ["Apple", "Banana", "Kiwi", "Orange"]
price = [22.3, 54.1, 13.6, 4.6]


def makeDict(given01 : list, given02: list) -> dict:
    result = dict()
    for each in range (0, len(given01)):
        result[given01[each]] = given02[each]

    return result
        



################## RUN ###################
print(makeDict(items, price))