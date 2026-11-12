from collections.abc import Sequence


def my_product_recursive(*seq: Sequence, repeat: int = 1):
    pools = [tuple(pool) for pool in seq if pool] * repeat
    n = len(pools)
    if n == 0:
        yield ()
        return 
    
    def _walk(i: int, acc: list):
        if i == n:
            yield tuple(acc)
            return
        for item in pools[i]:
            acc.append(item)
            yield from _walk(i + 1, acc)
            acc.pop()
            
    yield from _walk(0, [])


if __name__ == "__main__":
    from pprint import pprint

    seq = ["ab", (1, 2, 3)]
    pprint(list(my_product_recursive(*seq)))

    seq = "AB"
    pprint(list(my_product_recursive(seq, repeat=3)))

    pprint(list(my_product_recursive()))

    seq = ""
    pprint(list(my_product_recursive(seq)))