import time
import random


def random_ls(num):
    rand_list = random.sample(range(num), k=num)
    return rand_list


def insertion_sort(alist):
    insertion_sort.__name__ = 'Insertion Sort'
    start_time = time.time()

    for index in range(1, len(alist)):
        current_value = alist[index]
        position = index

        while position > 0 and alist[position-1] > current_value:
            alist[position] = alist[position-1]
            position = position-1

        alist[position] = current_value

    end_time = time.time() - start_time
    return end_time, alist


def shell_sort(alist):
    shell_sort.__name__ = 'Shell Sort'
    start_time = time.time()
    sublist_count = len(alist)//2

    while sublist_count > 0:
        for start_position in range(sublist_count):
            gap_insertion_sort(alist, start_position, sublist_count)

        sublist_count = sublist_count // 2

    end_time = time.time() - start_time
    return end_time, alist


def gap_insertion_sort(alist, start, gap):
    for i in range(start + gap, len(alist), gap):
        current_value = alist[i]
        position = i

        while position > gap and alist[position - gap] > current_value:
            alist[position] = alist[position - gap]
            position = position - gap

        alist[position] = current_value


def python_sort(alist):
    python_sort.__name__ = 'Python Sort'
    start_time = time.time()
    list.sort(alist)
    end_time = time.time() - start_time
    return end_time, alist


def main():
    ls_size = [500, 1000, 5000]
    ls_func = [insertion_sort, shell_sort, python_sort]

    for x in ls_func:
        for y in ls_size:
            z, a = x(random_ls(y))
            print(f"{x.__name__} of list size {y} took{z:10.7f} seconds to run, on average")


if __name__ == "__main__":
    main()
