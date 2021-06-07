def make_abs(seq):
    return [abs(el) for el in seq]


def make_abs_map(seq):
    return map(map(abs, seq))


nums = [float(el) for el in input().split()]
print(make_abs(nums))
# generators are different than lists in the way that once you cycle trough them they are empty
# nums_gen = map(float, input().split())
