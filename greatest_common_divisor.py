def gcd(n1, n2):

    if n2 is 0:
        return True

    while n2:
        # 0 is False, 'n2>0' is True
        n1, n2 = n2, n1 % n2

    return n1
