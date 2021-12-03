import copy
import sys


def main():

    with open("../input.txt") as f:
        o2 = f.read().split("\n")

    co2 = copy.copy(o2)

    o2_binary = get_binary(o2, 1)
    co2_binary = get_binary(co2, 0)

    print(f"O2 binary   : {o2_binary}")
    print(f"O2 decimal  : {int(o2_binary, 2)}")

    print(f"CO2 binary  : {co2_binary}")
    print(f"CO2 decimal : {int(co2_binary, 2)}")

    print(f"Life Support: {int(o2_binary, 2) * int(co2_binary, 2)}")


def get_binary(input, equal):

    for i in range(0, len(input[0])):

        ones = 0
        zeroes = 0
        for line in input:

            if line == "":
                continue

            if int(line[i]) == 0:
                zeroes += 1
            if int(line[i]) == 1:
                ones += 1

        if ones > zeroes:
            keep = "1" if equal == 1 else "0"
        elif ones < zeroes:
            keep = "0" if equal == 1 else "1"
        else:
            keep = str(equal)

        j = len(input) - 1
        while j >= 0:
            num = input[j]

            if num == "":
                del input[j]

            elif num[i] != keep:
                del input[j]

            if len(input) == 1:
                return input[0]

            j -= 1

        # print(f"{i} keep {keep}  {'o2' if equal == 1 else 'co2'} {','.join(input)}")

    return input[0]


if __name__ == "__main__":
    sys.exit(main())
