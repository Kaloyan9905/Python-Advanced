from collections import deque


def naughty_or_nice_list(items, *args, **kwargs):
    nice = []
    naughty = []
    not_found = []
    counter = 0



print(naughty_or_nice_list(
    [
        (3, "Amy"),
        (1, "Tom"),
        (7, "George"),
        (3, "Katy"),
    ],
    "3-Nice",
    "1-Naughty",
    Amy="Nice",
    Katy="Naughty",
))
