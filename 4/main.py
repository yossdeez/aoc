import sys

def main(lines:list[str]) -> int:
    total = 0
    def parse_line(line: str) -> tuple[set[int], set[int]]:
        # Card   1: 69 24 51 87  9 49 17 16 21 48 |  5 52 86 35 57 18 60 84 50 76 96 47 38 41 34 36 55 20 25 37  6 70 66 45  3
        line = line.split(":")[1].strip().split("|")
        #  [69 24 51 87  9 49 17 16 21 48, 5 52 86 35 57 18 60 84 50 76 96 47 38 41 34 36 55 20 25 37  6 70 66 45  3]

        return set(map(int, line[0].split())), set(map(int, line[1].split()))

    def score_numbers(winning:set, selected:set) -> int:
        score = 0
        for w_number in winning:
            if w_number in selected:
                if score == 0:
                    score+= 1
                else:
                    score *= 2
        return score

    for line in lines:
        winning_numbers, selected_numbers = parse_line(line)

        total += score_numbers(winning_numbers, selected_numbers)

    return total
if __name__ == "__main__":
    with open("source.txt", "r") as f:
        lines = f.readlines()
    #lines = sys.stdin.read().splitlines()
    print(main(lines))


