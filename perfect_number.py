def perfect_number(attained_list: list) -> list:
    """Calculates perfect numbers according to the given list items and returns them as list"""
    p_numbers = list()

    for n in attained_list:

        if n == 1:
            continue

        total = 1

        m = 2
        while m * m <= n:
            if n % m == 0:
                total += m + n / m
            m += 1

        if total == n:
            p_numbers.append(n)

    return p_numbers

# try it out with sample numbers
# following list contains sample perfect numbers [6, 25, 26, 28, 39, 60, 80, 99, 125, 468]
