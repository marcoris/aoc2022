with open("input.txt", "r") as file:
    datas = file.read().strip()

data = datas.split("\n")

counter = 0

for sections in data:
    section = sections.split(",")
    elves1 = section[0]
    elves2 = section[1]
    elve1 = elves1.split("-")
    elve2 = elves2.split("-")
    fullycontained = False

    assignment1 = []
    assignment2 = []

    for i in range(int(elve1[0]), int(elve1[1]) + 1):
        assignment1.append(i)

    for i in range(int(elve2[0]), int(elve2[1]) + 1):
        assignment2.append(i)

    if len(assignment1) < len(assignment2):
        for item in assignment1:
            if item in assignment2:
                fullycontained = True
            else:
                fullycontained = False
                break
    else:
        for item in assignment2:
            if item in assignment1:
                fullycontained = True
            else:
                fullycontained = False
                break

    counter += 1 if fullycontained else 0

print(counter)  # part 1 (562)

counter2 = 0

for sections in data:
    section = sections.split(",")
    elves1 = section[0]
    elves2 = section[1]
    elve1 = elves1.split("-")
    elve2 = elves2.split("-")
    fullycontained = False

    assignment1 = []
    assignment2 = []

    for i in range(int(elve1[0]), int(elve1[1]) + 1):
        assignment1.append(i)

    for i in range(int(elve2[0]), int(elve2[1]) + 1):
        assignment2.append(i)

    if len(assignment1) < len(assignment2):
        for item in assignment1:
            if item in assignment2:
                fullycontained = True
                break
    else:
        for item in assignment2:
            if item in assignment1:
                fullycontained = True
                break

    counter2 += 1 if fullycontained else 0

print(counter2)  # part 2 (924)
