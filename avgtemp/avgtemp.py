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
            dict_france[num[3][0:4]] = int(num[0])
            dict_sweden[num[3][0:4]] = int(num[1])
            dict_germany[num[3][0:4]] = int(num[2]
)
    def temp_max_min(args):
        max_temp = 0
        min_temp = 40
        new_max= {}
        new_min = {}
        for k, v in args.items():
            if v > max_temp:
                max_temp = v
                new_max[k] = v
                break
        for k, v in args.items():
            if v < min_temp:
                min_temp = v
                new_min[k] = v
                break
        return new_max, new_min

    france_temp = temp_max_min(dict_france)
    sweden_temp = temp_max_min(dict_sweden)
    german_temp = temp_max_min(dict_germany)

    return f"France => {france_temp} /n Sweden = > {sweden_temp} /n Germany = > {german_temp}"


print(temperature(file_name))