# recreating range() by using a class
# and overriding the iterator methods:
class Range_by_overriding_iter_next:
    def __init__(self, end, step=1):
        self.current = 0
        self.end = end
        self.step = step

    def __iter__(self):
        return self

    def __next__(self):
        if self.current >= self.end:
            raise StopIteration()
        else:
            return_val = self.current
            self.current += self.step
            return return_val


for i in Range_by_overriding_iter_next(5):
    print(i)


# recreating range() as a generator function
def range_gen(end):
    current = 0
    while current < end:
        yield current
        current += 1


for i in range_gen(5):
    print(i)
