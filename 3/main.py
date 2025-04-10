def sum_numbers_adjacent_to_symbols(f):
    digit_index_dict = {}
    symbols_index_list = []
    previous_digit_index_dict = {}
    previous_symbols_index_list = []
    total_sum = 0

    for line in f:
        line = line.strip()
        i = 0
        while i < len(line):
            if not line[i].isalnum() and not line[i] == ".":
                symbols_index_list.append(i)
            i+=1

        i = 0
        while i < len(line):
            dict_value = ""
            if line[i].isdigit():
                j = 0
                while i + j < len(line) and line[i + j].isdigit():
                    dict_value = dict_value + str(dict_value.join(line[i+j]))
                    j += 1
                digit_index_dict.update({str(i) + "-" + str(i+j-1): int(dict_value)})
                i += j
            else:
                i += 1

        for key, value in digit_index_dict.items():
            for s_index in symbols_index_list:
                if (
                    int(s_index)+1 == int(key.split("-")[0]) or
                    int(s_index)-1 == int(key.split("-")[1])
                ):
                    total_sum += int(value)

        for key, value in previous_digit_index_dict.items():
            for s_index in symbols_index_list:
                if (
                    int(s_index) + 1 == int(key.split("-")[0]) or
                    int(s_index) - 1 == int(key.split("-")[1]) or
                    int(key.split("-")[0]) <= int(s_index) <= int(key.split("-")[1])
                ):
                    total_sum += int(value)

        for key, value in digit_index_dict.items():
            for s_index in previous_symbols_index_list:
                if (
                    int(s_index)+1 == int(key.split("-")[0]) or
                    int(s_index)-1 == int(key.split("-")[1]) or
                    int(key.split("-")[0]) <= int(s_index) <= int(key.split("-")[1])
                ):
                    total_sum += value

        previous_digit_index_dict = digit_index_dict
        previous_symbols_index_list = symbols_index_list
        digit_index_dict = {}
        symbols_index_list = []

    return total_sum

def sum_two_numbers_adjacent_to_star(text):
    digit_dict = {}
    star_index_list = []
    previous_digit_dict = {}
    previous_star_index_list = []
    p_previous_digit_dict = {}
    numbers_adjacent_to_stars_dict = {}

    total_sum = 0

    def count_occasions_and_multiply_values(occasion, base_value, multiplier) -> str:
        occasion += 1
        base_value *= multiplier
        return str(occasion) + "-" + str(base_value)

    def create_digit_dict(row, dict):
        i = 0
        j = 0
        dict_value = ""
        while i < len(row):
            if line[i].isdigit():
                j = 0
                while i + j < len(row) and row[i + j].isdigit():
                    dict_value = dict_value + str(row[i+j])
                    j += 1
                dict[str(i) + "-" + str(i+j-1)] =  int(dict_value)
                dict_value = ""
                i += j
            else:
                i += 1


    for line in text:
        line = line.strip()

        star_index_list = [i for i in range(len(line)) if line[i] == "*"]

        create_digit_dict(line, digit_dict)
        for s_index in previous_star_index_list:
            numbers_adjacent_to_stars_dict.update({s_index: "0-1"})
            o, v = map(int, numbers_adjacent_to_stars_dict[s_index].split("-"))
            for key, value in digit_dict.items():
                if int(s_index) + 1 == int(key.split("-")[0]):
                    numbers_adjacent_to_stars_dict[s_index] = count_occasions_and_multiply_values(o,v,value)
                    print(numbers_adjacent_to_stars_dict[s_index])
                if int(s_index) - 1 == int(key.split("-")[1]):
                    numbers_adjacent_to_stars_dict[s_index] = count_occasions_and_multiply_values(o,v,value)

                if int(key.split("-")[0]) <= int(s_index) <= int(key.split("-")[1]):
                    numbers_adjacent_to_stars_dict[s_index] = count_occasions_and_multiply_values(o,v,value)

            for key, value in previous_digit_dict.items():
                if int(s_index) + 1 == int(key.split("-")[0]):
                    numbers_adjacent_to_stars_dict[s_index] = count_occasions_and_multiply_values(o,v,value)

                if int(s_index) - 1 == int(key.split("-")[1]):
                    numbers_adjacent_to_stars_dict[s_index] = count_occasions_and_multiply_values(o,v,value)

            for key, value in p_previous_digit_dict.items():
                if int(s_index) + 1 == int(key.split("-")[0]):
                    numbers_adjacent_to_stars_dict[s_index] = count_occasions_and_multiply_values(o,v,value)

                if int(s_index) - 1 == int(key.split("-")[1]):
                    numbers_adjacent_to_stars_dict[s_index] = count_occasions_and_multiply_values(o,v,value)

                if int(key.split("-")[0]) <= int(s_index) <= int(key.split("-")[1]):
                    numbers_adjacent_to_stars_dict[s_index] = count_occasions_and_multiply_values(o,v,value)

            if o == 2:
                total_sum += v

        numbers_adjacent_to_stars_dict = {}

        p_previous_digit_dict = previous_digit_dict
        previous_digit_dict = digit_dict
        digit_dict = {}

        previous_star_index_list = star_index_list
        star_index_list = []

    return total_sum

f = open("source.txt", "r")
print(sum_two_numbers_adjacent_to_star(f))