import multiprocessing

# By default, python is single-threaded because of the GIL (Global Interpreter Lock)
# multiprocessing library launches separate python processes


def spawn(num):
    print(f"Spawned {num}")


if __name__ == "__main__":
    for i in range(5):
        # (i,) is the syntax for creating a tuple with a single element, and multiprocessing.Process expects args to be a tuple
        p = multiprocessing.Process(target=spawn, args=(i,))
        p.start()
        p.join()  # if you need to wait for the process to finish
