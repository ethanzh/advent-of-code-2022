def contains(first, second) -> bool:
    first_lhs, first_rhs = (int(n) for n in first.split("-"))
    second_lhs, second_rhs = (int(n) for n in second.split("-"))

    first_range = range(first_lhs, first_rhs + 1)
    second_range = range(second_lhs, second_rhs + 1)

    return (first_lhs in second_range and first_rhs in second_range) or (
        second_lhs in first_range and second_rhs in first_range
    )


print(
    sum([int(contains(*line.split(","))) for line in open("input").read().splitlines()])
)
