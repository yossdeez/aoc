def gameska(text):
    total_sum = 0
    total_sum_counter = 1
    max_values_dict = {
        'red' : 12, 'green' : 13, 'blue' : 14
    }

    for line in text:
        line = line.split(":")[1]

        next_line = 0
        i = 0
        while i < len(line):

            if line[i].isdigit() and line[i+1].isdigit():

                check = int(line[i])*10 + int(line[i+1])
                if check > 14:
                    next_line = 1
                    break
            i+=1

        if next_line == 1:
            total_sum_counter += 1
            continue
        sets = line.split(";")
        for set in sets:
            subsets = set.split(",")

            if next_line == 1:
                break

            for subset in subsets:
                for key, max_value in max_values_dict.items():

                    if key == subset.split()[1]:
                        if max_value < int(subset.split()[0]):
                            print(subset.split()[0] + " " + subset.split()[1])
                            next_line = 1

        if next_line == 1:
            total_sum_counter += 1
            continue

        total_sum += total_sum_counter
        total_sum_counter += 1

    return total_sum

def gameska2(text):
    total_sum = 0
    max_values_dict = {
        'red' : 0, 'green' : 0, 'blue' : 0
    }

    for line in text:
        line = line.split(":")[1]

        sets = line.split(";")
        for set in sets:

            subsets = set.split(",")
            for subset in subsets:

                for key, max_value in max_values_dict.items():

                    if key == subset.split()[1]:
                        if max_value < int(subset.split()[0]):
                            max_values_dict.update({subset.split()[1]:int(subset.split()[0])})


        total_sum += int(max_values_dict['red'])*int(max_values_dict['green'])*int(max_values_dict['blue'])
        max_values_dict = {
            'red': 0, 'green': 0, 'blue': 0
        }
    return total_sum

f = open("source.txt", "r")
print(gameska2(f))