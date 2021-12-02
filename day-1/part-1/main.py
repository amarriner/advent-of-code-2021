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

        increase = False
        if int(line) > int(last):
            increased += 1
            increase = True

        print(f"{line} > {last} ? {increase}")

        last = line

    print(f"Depth increased {increased} times")


if __name__ == "__main__":
    sys.exit(main())
