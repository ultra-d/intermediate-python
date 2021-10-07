from math import sqrt

'''
def opperation(x, funct):
    return funct(x)

def sqrt(x):
    return x**0.5


def squared(x):
    return x**2

if __name__ == "__main__":
    result_1 = opperation(16, squared)
    print(result_1)
'''
#filter(function, iterable)

integer = [1, 2, 3, 4, 5, 6, 7, 8, 9 , 10]
even = list(filter(lambda x: x%2 == 0, integer))
print(even)