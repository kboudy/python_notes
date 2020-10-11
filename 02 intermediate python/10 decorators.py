from functools import wraps


def add_wrapping(item):
    # if you care (for some reason) about the function's
    # __name__ being the original (instead of wrapped_item,
    # in this case), uncomment the next line
    # @wraps(item)
    def wrapped_item():
        return f"a wrapped up box of {str(item())}"

    return wrapped_item


@add_wrapping
def new_gpu():
    return "a new Tesla P100 GPU"


@add_wrapping
@add_wrapping
def new_bicycle():
    return "a new bicycle"


# notice that the function names both become "wrapped_item"
# (the name we assigned the wrapper fuction, on line 2)
print(new_gpu.__name__)  # wrapped_item
print(new_bicycle.__name__)  # wrapped_item

print(new_gpu())  # a wrapped up box of a new Tesla P100 GPU
print(new_bicycle())  # a wrapped up box of a wrapped up box of a new bicycle
