def divisors(num):
    divisors = []
    try:
        if num < 0:
            raise ValueError("Please non negative numbers ")
        for i in range(1, num + 1):
            if num % i == 0:
                divisors.append(i)
        return divisors
    except ValueError as ve:
        print(ve)


def run():
    try:
        num = int(input("give me a number: "))
        print(divisors(num))
        print("IT'S OVER")
    except ValueError:
        print("It is not a valid input")


if __name__ == "__main__":
    run()