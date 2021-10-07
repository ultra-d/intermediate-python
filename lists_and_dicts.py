def run():
    my_list = [1, "hello", True, 4.5]
    my_dict = {"firstname": "Daniela", "lastname": "Melo"}

    super_list = [
        {"firstname": "Daniela", "lastname": "Melo"},
        {"firstname": "Juan", "lastname": "Cruz"},
        {"firstname": "Rocco", "lastname": "Melo"},
    ]

    super_dict = {
        "natural_nums" : [1,2,3,4,5],
        "interger_numer" : [-1, -2, 0, 1, 2],
        "floating_nums" : [1.1, 4.5, 6.43]
    }

    for key, value in super_dict.items():
        print(key, "-", value)

        
if __name__ == "__main__":
    run()