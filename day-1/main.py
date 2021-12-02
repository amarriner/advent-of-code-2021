import sys


def main():

    with open("input.txt") as f:
        input = f.read().split("\n")

    last = -1
    increased = 0
    for line in input:
        if line == "":
            continue

        if last == -1:
            last = line
            continue

        if line > last:
            increased += 1

        last = line

    print(f"Depth increased {increased} times")


if __name__ == "__main__":
    sys.exit(main())
