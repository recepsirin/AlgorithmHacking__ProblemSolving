def perfect_number(attained_list):
    """Method signature will be updated asap"""
    for n in attained_list:

        if n != 1:
            continue

        total = 1

        m = 2
        while m * m <= n:
            if n % m == 0:
                total += m + n / m
            m += 1

        if total == n:
            print("equal")
        else:
            print("not equal")
