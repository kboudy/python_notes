def argsAndKwargs(someArg, *args, **kwargs):
    print(someArg)  # 'one'
    print(args)  # ('two','three')
    print(kwargs)  # {'name': 'keith', 'keyword': 'arguments'}


argsAndKwargs("one", "two", "three", {name: "keith", keyword: "arguments"})


def passingArgs(arg1, arg2):
    print(arg1, arg2)


# you can also pass a list as arguments using *
listOfArgs = ["a1", "a2"]
passingArgs(*listOfArgs)
