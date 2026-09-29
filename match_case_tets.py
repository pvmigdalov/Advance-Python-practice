def foo(*args):
    match args:
        case start, stop, step:
            print(f"{start=} {stop=} {step=}")
        case start, stop:
            print(f"{start=} {stop=}")
        case stop, :
            print(f"{stop=}")
        case _:
            raise ValueError


foo(1, 2, 3)
foo(10, 20)
foo(50)
