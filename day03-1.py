SYMBOLS = {"/", "+", "#", "$", "-", "&", "%", "=", "@", "*"}


def get_part_numbers_sum(lines: list[str]):
    schema_height = len(lines) - 1
    schema_length = len(lines[0]) - 1

    def _get_nearest_symbols(self_x: int, self_y: int, self_l: int) -> set[str]:
        x_0 = max(0, self_x - self_l)
        y_0 = max(0, self_y - 1)
        x_1 = min(schema_length, self_x + 1)
        y_1 = min(schema_height, self_y + 1)

        return set(lines[y_0][x_0:x_1 + 1] + lines[self_y][x_0:x_1 + 1] + lines[y_1][x_0:x_1 + 1])

    part_numbers_sum = 0

    for y, line in enumerate(lines):
        number_chunk = ""
        for x, char in enumerate(line):
            if char.isdigit():
                number_chunk += char

                if x == schema_length or not line[x + 1].isdigit():
                    nearest_symbols = _get_nearest_symbols(x, y, len(number_chunk))

                    if SYMBOLS.intersection(nearest_symbols):
                        part_numbers_sum += int(number_chunk)

                    number_chunk = ""
    return part_numbers_sum


def main() -> None:
    with open("input03.txt", "r", encoding="utf-8") as f:
        print("Part 1:", get_part_numbers_sum(f.readlines()))


if __name__ == "__main__":
    main()