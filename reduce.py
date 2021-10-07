from functools import reduce

if __name__ == '__main__':
    integer = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    sumcum = reduce(lambda a,b : a + b, integer)
    print(sumcum)