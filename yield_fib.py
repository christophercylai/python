"""
Generate fibonacci sequences
Can generate multiple sequences simultaneously using coroutine
"""
import argparse


def fib(loop_num):
    """
    generate fibonacci sequence
    """
    # handle special cases
    origin_loop_num = loop_num
    assert loop_num > 0, f'The number provided ({loop_num}) is not greater then zero'
    if loop_num == 1:
        print(f'The Fibonacii number after {origin_loop_num} loops is: 0')
        return
    if loop_num == 2:
        print(f'The Fibonacii number after {origin_loop_num} loops is: 1')
        return

    loop_num -= 2
    head_num = 0
    fib_num = 1

    while loop_num > 0:
        next_head = fib_num
        fib_num += head_num
        head_num = next_head

        loop_num -= 1
        yield

    print(f'The Fibonacii number after {origin_loop_num} loops is: {fib_num}')


def get_args():
    """
    get command line arguments or display help
    """
    parser = argparse.ArgumentParser(description='Get Fibonacci Sequences')
    parser.add_argument('--stops', '-s', nargs='+', type=int, help='how many fibonacci loops to do - you can multiple loops such as -s 5 11 29')
    return parser.parse_args()


if __name__ == "__main__":
    ARGS = get_args()

    FIBS = []
    for each_stop in ARGS.stops:
        FIBS.append(fib(each_stop))

    FIBS_TO_REMOVE = []
    while FIBS:
        for fib_pos in range(len(FIBS)):
            try:
                FIBS[fib_pos].__next__()
            except StopIteration:
                FIBS_TO_REMOVE.append(fib_pos)

        # clean up the exited coroutine
        MINUS_POS = 0  # need to adjust for the position already removed
        for each_pos in FIBS_TO_REMOVE:
            FIBS.remove(FIBS[fib_pos - MINUS_POS])
            MINUS_POS += 1
        FIBS_TO_REMOVE = []
