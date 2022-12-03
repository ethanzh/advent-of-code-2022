from functools import reduce
from more_itertools import batched

print(
    sum(
        [
            (lambda x: ord(x) - (38 if x.isupper() else 96))(
                reduce(
                    lambda x, y: x & y, [{c for c in items} for items in group]
                ).pop()
            )
            for group in batched(
                [line.strip() for line in open("input").readlines()], 3
            )
        ]
    )
)
