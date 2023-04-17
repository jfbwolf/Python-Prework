# 5 Finding numbers in a consecutive list.

def is_consecutive(x):
    ls = list(map(int, x.split('-')))
    diffs = set(x-y for x, y in zip(ls, ls[1:]))
    print (len(diffs) == 1 and diffs.pop() in (1, -1))

is_consecutive("1-2-3-4")
is_consecutive("1-2-4-5")