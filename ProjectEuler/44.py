import math
def is_pentagonal(number: int) -> bool:
    s = int(round(math.sqrt(1 + 24 * number)))
    return s**2 == 1 + 24 * number and (1 + s) % 6 == 0

def iter_pentagonal_numbers():
    p = 1
    d = 4
    while True:
        yield p
        p += d
        d += 3

def solution_sum_lower() -> int:
    for p_sum in iter_pentagonal_numbers():
        for p_lower in iter_pentagonal_numbers():
            upper = p_sum - p_lower
            if upper < p_lower:
                break
            diff = upper - p_lower
            if is_pentagonal(upper) and is_pentagonal(diff):
                return diff
print(solution_sum_lower())