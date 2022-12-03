print(
    sum(
        [
            (lambda x: ord(x) - (38 if x.isupper() else 96))((x & y).pop())
            for x, y in [
                (
                    {c for c in items[: len(items) // 2]},
                    {c for c in items[len(items) // 2 :]},
                )
                for items in open("input").read().splitlines()
            ]
        ]
    )
)
