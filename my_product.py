from collections.abc import Sequence


def my_product(*seq: Sequence, repeat: int = 1):
    pools = [tuple(pool) for pool in seq if pool] * repeat
    n = len(pools)
    if n == 0:
        yield ()
        return 
    
    idx = [0] * n
    while True:
        yield tuple(pools[i][idx[i]] for i in range(n))
        i = n - 1
        while i >= 0:
            idx[i] += 1
            if idx[i] < len(pools[i]):
                break
            idx[i] = 0 
            i -= 1
        else:
            return


if __name__ == "__main__":
    from pprint import pprint

    seq = ["ab", (1, 2, 3)]
    pprint(list(my_product(*seq)))

    seq = "AB"
    pprint(list(my_product(seq, repeat=3)))

    pprint(list(my_product()))

    seq = ""
    pprint(list(my_product(seq)))