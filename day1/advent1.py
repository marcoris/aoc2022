def get_largest(arr, n):
    harr = []
    m = len(arr)

    for i in range(0, n):
        mx = arr[0]
        for j in range(1, m):
            if arr[j] > mx and arr[j] not in harr:
                mx = arr[j]
        harr.append(mx)

    return sum(harr)


def num_larger():
    summation = 0
    array = []
    with open("input.txt") as file:
        for line in file:
            number = line.replace("\n", "")
            try:
                if number:
                    summation += int(number)
                else:
                    array.append(summation)
                    summation = 0
            except ValueError:
                pass

    return array


data = num_larger()

print(get_largest(data, 1))  # part 1 (72017)
print(get_largest(data, 3))  # part 2 (212520)
