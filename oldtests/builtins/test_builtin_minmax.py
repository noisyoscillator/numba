"""
>>> max1([100])
100
>>> max1([1,2.0,3])
3
>>> max1([-1,-2,-3.0])
-1
>>> max1(1)
Traceback (most recent call last):
    ...
TypeError: 'int' object is not iterable

>>> min1([100])
100
>>> min1([1,2,3.0])
1
>>> min1([-1,-2.0,-3])
-3
>>> min1(1)
Traceback (most recent call last):
    ...
TypeError: 'int' object is not iterable


>>> max2(1, 2)
2
>>> max2(1, -2)
1
>>> max2(10, 10.25)
10.25
>>> max2(10, 9.9)
10.0
>>> max2(0.1, 0.25)
0.25
>>> max2(1, 'a')
Traceback (most recent call last):
    ...
UnpromotableTypeError: Cannot promote types int and string

>>> min2(1, 2)
1
>>> min2(1, -2)
-2
>>> min2(10, 10.1)
10.0
>>> min2(10, 9.75)
9.75
>>> min2(0.25, 0.3)
0.25
>>> min2(1, 'a')
Traceback (most recent call last):
    ...
UnpromotableTypeError: Cannot promote types int and string

>>> max4(20)
20.0

>>> min4(-2)
-2.0

"""

from numba import autojit

@autojit
def max1(x):
    return max(x)

@autojit
def min1(x):
    return min(x)

@autojit
def max2(x, y):
    return max(x, y)

@autojit
def min2(x, y):
    return min(x, y)

@autojit
def max4(x):
    return max(1, 2.0, x, 14)

@autojit
def min4(x):
    return min(1, 2.0, x, 14)


if __name__ == '__main__':
    import doctest
    doctest.testmod()
