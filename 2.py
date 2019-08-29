import re


def is_number(num):
    pattern = re.compile(r'^[-+]?[0-9]+\.[0-9]+$')
    result = pattern.match(num)
    if result:
        return True
    else:
        return False


n = 1.1
a = is_number(str(n))
if a == 1:
    print(a)
