import time
import timeit

# simple way of measuring seconds (float)
start = time.time()
# ...
total = time.time() - start


# with timeit, you can ask how long (in seconds) it takes to run a snippet of code 500000 times
print(
    timeit.timeit(
        """
input_list = range(100)


def div_by_five(num):
    return num % 5 == 0


xyz = (i for i in input_list if div_by_five(i))
        """,
        number=500000,
    )
)
