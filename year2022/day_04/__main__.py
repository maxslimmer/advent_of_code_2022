def parse_range(s):
    return tuple(map(int, s.split("-")))


with open("y2022\\day_4\\data.txt") as _file:
    lines = _file.readlines()

part1_count = 0
part2_count = 0
for line in lines:
    assignment1, assignment2 = [parse_range(_range) for _range in line.split(",")]
    if (
        assignment1[0] >= assignment2[0]
        and assignment1[1] <= assignment2[1]
        or assignment2[0] >= assignment1[0]
        and assignment2[1] <= assignment1[1]
    ):
        part1_count += 1

    # ------------------------- part 2 ------------------------
    if (
        assignment2[0] <= assignment1[0] <= assignment2[1]
        or assignment2[0] <= assignment1[1] <= assignment2[1]
        or assignment1[0] <= assignment2[0] <= assignment1[1]
        or assignment1[0] <= assignment2[1] <= assignment1[1]
    ):
        part2_count += 1

print(part1_count)
print(part2_count)

