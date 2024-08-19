

def list_divide(numbers=[], divide=2):

    list_1 = [i for i in numbers if i % divide == 0]
    output = 0
    for i in list_1:
        output += 1
    print(output)


class ListDivideException(Exception):
    pass


def test_list_divide():

    try:
        list_divide([1, 2, 3, 4, 5])
        list_divide([2, 4, 6, 8, 10])
        list_divide([30, 54, 63, 98, 100], divide=10)
        list_divide([])
        list_divide([1, 2, 3, 4, 5], 1)

    except Exception as e:
        raise ListDivideException("There was a problem with your test:", e) from None


test_list_divide()
