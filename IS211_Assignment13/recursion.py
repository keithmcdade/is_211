def fibonacci(n):
    if n < 0:
        print("error.")
    elif n == 0:
        return 0
    elif n == 1:
        return 1
    else:
       return fibonacci(n-1) + fibonacci(n-2) 


def gcd(a, b):
    if a == 0:
        return b
    if b == 0:
        return a
    else:
        return gcd(b, (a % b))    


def compare_to(s1, s2):
    if s1[1:] and not s2[1:]:
        return len(s1[1:])
    if s2[1:] and not s1[1:]:
        return - len(s2[1:])
    if not s1[1:] and not s2[1:]:
        return 0
    else:
        return compare_to(s1[1:], s2[1:])


def compare_test(a, b):
    if a == b:
        return True
    else:
        return False


if __name__ == "__main__":
    print(fibonacci(10))    
    print(gcd(36, 120))
    print(compare_to("string", "STRING"), compare_to("longer string", "string"), compare_to("string", "longer string"))

    s1 = "longer string"
    s2 = "string"
    a = compare_to(s1, s2)
    b = len(s1) - len(s2)
    print(compare_test(a, b))
