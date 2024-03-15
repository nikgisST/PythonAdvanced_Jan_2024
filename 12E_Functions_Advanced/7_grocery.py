def grocery_store(**kwargs):
    products = sorted(kwargs.items(), key=lambda x: (-x[1], -len(x[0]), x[0]))
    return "\n".join(f"{p}: {q}" for p, q in products)
    # products.items() => [(bread, 2), (pasta, 2), ...]

def grocery_store(**kwargs):
    products = sorted(kwargs.items(), key=lambda x: (-x[1], -len(x[0]), x[0]))   # съдържа list от tuples (SORTED връща LIST)

    result = []

    for each_product, each_quantity in products:
        result.append(f"{each_product}: {each_quantity}")

    return "\n".join(result)


print(grocery_store(
    bread=2,
    pasta=2,
    eggs=20,
    carrot=1,
))

