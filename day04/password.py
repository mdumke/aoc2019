"""Count valid passwords in given range."""

from collections import Counter

RANGE = (240920, 789857)


def count_valid_passwords(lo: int, hi: int, strict: bool) -> int:
    """Return number of passwords in range that are valid."""
    return sum(is_valid_password(str(pw), strict) for pw in range(lo, hi))


def is_valid_password(pw: str, strict: bool) -> bool:
    """Return True if password fulfills specified criteria."""
    # check non-decreasing condition
    if any(i > j for i, j in zip(pw[:-1], pw[1:])):
        return False

    digit_counts = Counter(pw).values()

    if strict:
        # check for strict duplicates
        return any(c == 2 for c in digit_counts)
    else:
        # check for duplicates
        return any(c >= 2 for c in digit_counts)


if __name__ == '__main__':
    print(f'part 1: {count_valid_passwords(*RANGE, strict=False)}')
    print(f'part 2: {count_valid_passwords(*RANGE, strict=True)}')
