"""Count valid passwords in given range."""

from collections import Counter

RANGE = (240920, 789857)

def num_valid_passwords(lo, hi, strict):
    return sum(is_valid(pw, strict) for pw in range(lo, hi))

def is_valid(password, strict):
    digits = [int(n) for n in list(str(password))]
    if strict:
        return is_non_decreasing(digits) and has_strict_duplicate(digits)
    else:
        return is_non_decreasing(digits) and has_duplicate(digits)

def is_non_decreasing(digits):
    for i in range(len(digits) - 1):
        if digits[i] > digits[i + 1]:
            return False
    return True

def has_duplicate(digits):
    for i in range(len(digits) - 1):
        if digits[i] == digits[i + 1]:
            return True
    return False

def has_strict_duplicate(digits):
    counts = Counter(digits)
    return any(count == 2 for count in counts.values())

if __name__ == '__main__':
    print(f'part 1: {num_valid_passwords(*RANGE, strict=False)}')
    print(f'part 2: {num_valid_passwords(*RANGE, strict=True)}')
