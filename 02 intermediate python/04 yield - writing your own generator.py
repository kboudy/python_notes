def simple_gen():
    yield "Oh"
    yield "Hello"
    yield "There"


CORRECT_COMBO = (3, 8, 1)


def combo_gen():
    for c1 in range(10):
        for c2 in range(10):
            for c3 in range(10):
                yield (c1, c2, c3)


for c1, c2, c3 in combo_gen():
    print(c1, c2, c3)
    if (c1, c2, c3) == CORRECT_COMBO:
        print(f"Found the combo: {c1,c2,c3}")
        break