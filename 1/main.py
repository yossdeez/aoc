from idlelib.editor import keynames


def return_sum(f):
    total_sum = 0
    for line in f:
        line = "".join([c for c in line if c.isdigit()])
        total_sum += int(line[0])*10 + int(line[-1])

    return total_sum

def return_sum_and_words(f):
    total_sum = 0
    numberdict = {
        "one": '1',
        "two": '2',
        "three": '3',
        "four": '4',
        "five": '5',
        "six": '6',
        "seven": '7',
        "eight": '8',
        "nine": '9'
    }
    for line in f:
        i = 0

        while i < len(line):

            if line[i].isdigit():
                break

            for word, number in numberdict.items():
                if line[i:].startswith(word):
                    line = line.replace(word, number, 1)
                    break
                else:
                    continue

            i += 1

        i = len(line) - 1

        while i >= 0:

            if line[i].isdigit():
                break

            for word, number in numberdict.items():
                if line[i:].startswith(word):
                    line = line.replace(word, number, 1)
                    break
                else:
                    continue

            i -= 1

        line = "".join([c for c in line if c.isdigit()])
        total_sum += int(line[0]) * 10 + int(line[-1])

    return total_sum
f = open("source.txt", "r")
done = return_sum_and_words(f)
print(done)
