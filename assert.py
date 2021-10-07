def divisors(num):
    divisors = []
    for i in range(1, num + 1):
        if num % i == 0:
            divisors.append(i)
    return divisors

def run():
    num = input("give me a number: ")
    assert num.isnumeric(), "Please cant be anything else"
    print(divisors(int(num)))
    print("IT'S OVER")


if __name__ == "__main__":
    run()