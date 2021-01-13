import sys

file_name = "text.txt"

def temperature(file_name):
    try:
        with open(file_name, 'r') as f:
            lines = f.readlines()

    except IOError:
        print("Error occurred opening the file")

    dict_france = {}
    dict_sweden = {}
    dict_germany = {}
    for i, k in enumerate(lines):
        num = k.split(" ")
        if i != 0:
            dict_france[num[3][0:4]] = num[0]
            dict_sweden[num[3][0:4]] = num[1]
            dict_germany[num[3][0:4]] = num[2]

    def temp_max_min(args):
        max_temp = None
        min_temp = None
        for k, v in args.items():
            if v > max_temp:
                max_temp = v
                break
        for k, v in args.items():
            if v < min_temp:
                min_temp = v
                break
        return max_temp, min_temp

    for

    return dict_france, dict_sweden, dict_germany





print(temperature(file_name))