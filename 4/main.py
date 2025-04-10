import sys

def solve_part1(lines:list[str]) -> int:
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

def solve_part2(lines:list[str]) -> int:
    score_list = []
    cards_list = []

    def parse_line(row: str) -> tuple[set[int], set[int]]:
        # Card   1: 69 24 51 87  9 49 17 16 21 48 |  5 52 86 35 57 18 60 84 50 76 96 47 38 41 34 36 55 20 25 37  6 70 66 45  3
        row = row.split(":")[1].strip().split("|")
        #  [69 24 51 87  9 49 17 16 21 48, 5 52 86 35 57 18 60 84 50 76 96 47 38 41 34 36 55 20 25 37  6 70 66 45  3]

        return set(map(int, row[0].split())), set(map(int, row[1].split()))

    def score_numbers(winning:set, selected:set) -> int:
        score = 0
        for w_number in winning:
            if w_number in selected:
                score+= 1

        return score

    def list_to_total(first_list: list[int],second_list: list[int]) -> int:
        for j, number in enumerate(second_list):
            for s in range(first_list[j]):
                for i in range(number):
                    if j + i + 1 < len(first_list):
                        first_list[j + i + 1] += 1
                        i += 1

        return sum(first_list)

    for line in lines:

        winning_numbers, selected_numbers = parse_line(line)

        score_list.append(score_numbers(winning_numbers, selected_numbers))

        cards_list.append(1)

    return list_to_total(cards_list, score_list)

if __name__ == "__main__":
    with open("source.txt", "r") as f:
        lines = f.readlines()
    #lines = sys.stdin.read().splitlines()
    print(solve_part2(lines))


