def read():
    numbers = []
    with open("./FILES/numbers.txt", "r", encoding="utf-8") as f:
        for line in f:
            numbers.append(int(line))
    print(numbers)

def write():
    names = ["Daniela", "Juan", "Roco", "Milo", "Pablo"]
    with open("./FILES/names.txt", "a", encoding="utf-8") as f:
        for name in names:
            f.write(name)
            f.write("\n")


def run():
    read()
    write()

if __name__ == "__main__":
    run()