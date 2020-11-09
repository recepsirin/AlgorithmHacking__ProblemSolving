def perfect_number(attained_list: list) -> list:
    """Method signature will be updated asap"""
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
