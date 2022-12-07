def rockpaperscissors(mode):
    with open("input.txt") as file:
        summation = 0
        rock_p = 1
        paper_p = 2
        scissors_p = 3
        lost_p = 0
        draw_p = 3
        win_p = 6

        x = "X"  # Rock
        y = "Y"  # Paper
        z = "Z"  # Scissors

        if mode == 2:
            x = "lose"
            y = "draw"
            z = "win"

        for line in file:
            data = line.replace("\n", "").split()
            try:
                # Rock, Rock/draw
                if data[0] == "A":
                    if len(x) == 1 and data[1] == x or len(y) == 4 and data[1] == "Y":
                        summation += (draw_p + rock_p)
                    # Rock, Paper/win
                    elif len(y) == 1 and data[1] == y or len(z) == 3 and data[1] == "Z":
                        summation += (win_p + paper_p)
                    # Rock, Scissors/lose
                    elif len(z) == 1 and data[1] == z or len(x) == 4 and data[1] == "X":
                        summation += (lost_p + scissors_p)

                # Paper, Rock/lose
                elif data[0] == "B":
                    if len(x) == 1 and data[1] == x or len(x) == 4 and data[1] == "X":
                        summation += (lost_p + rock_p)
                    # Paper, Paper/draw
                    elif len(y) == 1 and data[1] == y or len(y) == 4 and data[1] == "Y":
                        summation += (draw_p + paper_p)
                    # Paper, Scissors/win
                    elif len(z) == 1 and data[1] == z or len(z) == 3 and data[1] == "Z":
                        summation += (win_p + scissors_p)

                # Scissors, Rock/win
                elif data[0] == "C":
                    if len(x) == 1 and data[1] == x or len(z) == 3 and data[1] == "Z":
                        summation += (win_p + rock_p)
                    # Scissors, Paper/lose
                    elif len(y) == 1 and data[1] == y or len(x) == 4 and data[1] == "X":
                        summation += (lost_p + paper_p)
                    # Scissors, Scissors/draw
                    elif len(z) == 1 and data[1] == z or len(y) == 4 and data[1] == "Y":
                        summation += (draw_p + scissors_p)
            except ValueError:
                pass

        return summation


print(rockpaperscissors(1))  # part 1 (11906)
print(rockpaperscissors(2))  # part 2 (11186)
