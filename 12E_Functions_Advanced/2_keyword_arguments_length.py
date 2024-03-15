def kwargs_length(**kwargs) -> int:
    # {'name': 'Peter', 'age': 25}   packing them again here
    return len(kwargs)



dictionary = {'name': 'Peter', 'age': 25}
print(kwargs_length(**dictionary))  # ** => kwargs_length(name="Peter", age=25) unpacking


print(kwargs_length(name="Peter", age=25))   # the same result as above one