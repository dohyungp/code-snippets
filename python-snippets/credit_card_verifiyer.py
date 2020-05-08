def check_luhn(cc: str) -> bool:
    verify_code = int(cc[-1])
    reversed_cc = cc[::-1][1:]
    sum_cc = 0
    for i, c in enumerate(reversed_cc):
        if i % 2 == 0:
            v = int(c) * 2
        else:
            v = int(c)
        v = v // 10 + v % 10
        sum_cc += v

    if (sum_cc + verify_code) % 10 == 0:
        return True

    else:
        return False
