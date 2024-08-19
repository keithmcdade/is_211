import time
import random


def random_ls(num):
    rand_list = random.sample(range(num), k=num)
    return rand_list


def sequential_search(a_list, item):
    start_time = time.time()

    sequential_search.__name__ = "Sequential Search"

    pos = 0
    found = False

    while pos < len(a_list) and not found:
        if a_list[pos] == item:
            found = True
        else:
            pos = pos+1

    end_time = time.time() - start_time
    return end_time, found


def ordered_sequential_search(b_list, item):
    start_time = time.time()

    ordered_sequential_search.__name__ = "Ordered Sequential Search"

    pos = 0
    found = False
    stop = False

    while pos < len(b_list) and not found and not stop:
        if b_list[pos] == item:
            found = True
        else:
            if b_list[pos] > item:
                stop = True
            else:
                pos = pos + 1

    end_time = time.time() - start_time
    return end_time, found


def binary_search_iterative(c_list, item):
    start_time = time.time()

    binary_search_iterative.__name__ = "Binary Search"

    first = 0
    last = len(c_list) - 1
    found = False

    while first <= last and not found:
        midpoint = (first + last) // 2
        if c_list[midpoint] == item:
            found = True
        else:
            if item < c_list[midpoint]:
                last = midpoint - 1
            else:
                first = midpoint + 1

    end_time = time.time() - start_time
    return end_time, found


def binary_search_recursive(d_list, item, t=0):
    binary_search_recursive.__name__ = "Binary Recursive Search"
    if t == 0:
        start_time = time.time()
    else:
        start_time = t

    if len(d_list) == 0:
        end_time = time.time() - start_time
        return end_time, False
    else:
        midpoint = len(d_list)//2
        if d_list[midpoint] == item:
            end_time = time.time() - start_time
            return end_time, True
        else:
            if item < d_list[midpoint]:
                return binary_search_recursive(d_list[:midpoint], item, start_time)
            else:
                return binary_search_recursive(d_list[midpoint + 1:], item, start_time)


def perform_search(func, size, item, sample_sz):
    searched = []
    for i in range(sample_sz):
        rand_ls = random_ls(size)
        searched = func(rand_ls, item)
    return searched


def main():
    sample_sz = 100
    item = 99999999
    ls_size = [500, 1000, 5000]
    ls_func = [sequential_search, ordered_sequential_search, binary_search_iterative, binary_search_recursive]

    for x in ls_func:
        for y in ls_size:
            z = perform_search(x, y, item, sample_sz)
            print(f"{x.__name__} of list size {y} took{z[0]:10.7f} seconds to run, on average")


if __name__ == "__main__":
    main()
