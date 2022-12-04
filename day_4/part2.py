lines = open("input").read().splitlines()


def overlap(first, second) -> bool:
    first_lhs, first_rhs = [int(n) for n in first.split("-")]
    second_lhs, second_rhs = [int(n) for n in second.split("-")]

    return (second_lhs >= first_lhs and second_lhs <= first_rhs) or (
        first_lhs >= second_lhs and first_lhs <= second_rhs
    )


total = 0
for line in lines:
    first, second = line.split(",")
    if not overlap(first, second):
        continue
    total += 1

print(total)
