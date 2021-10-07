from math import sqrt
def run():
    '''
    my_dict = {
    }

    for i in range(1, 101):
        if i % 3 != 0:
            my_dict[i] = i**3

    print(my_dict)
    '''
    #i: i**3 => first i = key , i**3 value
    my_dict = {i: i**3 for i in range (1, 101) if i % 3 != 0}
    print(my_dict)

    challenge = {i: round(sqrt(i),3) for i in range (1, 101) }
    print(challenge)

if __name__ == '__main__':
    run()