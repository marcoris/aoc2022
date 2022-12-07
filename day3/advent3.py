with open("input.txt", "r") as file:
    datas = file.read().strip()

rucksacks = datas.split("\n")
summation = 0
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z']
lowercase = {}
uppercase = {}

for i in range(0, len(alphabet)):
    lowercase[alphabet[i]] = i + 1

for i in range(0, len(alphabet)):
    uppercase[alphabet[i].upper()] = i + 27

for data in rucksacks:
    first_item = data[:len(data) // 2]
    second_item = data[len(data) // 2:]

    for item in first_item:
        if item in second_item:
            if item.islower():
                summation += lowercase.get(item)
                break
            else:
                summation += uppercase.get(item)
                break

print(summation)  # part 1 (8202)

summation = 0
index = 0

while index < len(rucksacks):
    group1 = rucksacks[index]
    group2 = rucksacks[index + 1]
    group3 = rucksacks[index + 2]

    for badge in group1:
        if badge in group2 and badge in group3:
            if badge.islower():
                summation += lowercase.get(badge)
                break
            else:
                summation += uppercase.get(badge)
                break
    index += 3

print(summation)  # part 2 (2864)
