import sys


def main():

    with open("../input.txt") as f:
        input = f.read().split("\n")

    # I'm sure there's a better way to make everything an int, but this is easy
    for index, line in enumerate(input):
        if line == "":
            continue

        input[index] = int(line)

    increased = 0
    for index, line in enumerate(input):
        if line == "":
            continue

        if (index + 4) >= len(input):
            continue

        this_window = sum(input[index:index + 3])
        next_window = sum(input[index + 1:index + 4])
        if next_window > this_window:
            increased += 1

        print(f"{line} {this_window} {next_window}")

    print(f"Window increased {increased} times")


if __name__ == "__main__":
    sys.exit(main())
