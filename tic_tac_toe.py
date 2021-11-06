def get_coordinates():
    global cell_array
    coordinates = input("Enter the coordinates: ")
    coordinates = coordinates.split()
    if not coordinates[0].isnumeric() or not coordinates[1].isnumeric():
        print("You should enter numbers!")
        get_coordinates()
    elif int(coordinates[0]) < 1 or int(coordinates[0]) > 3 or int(coordinates[1]) < 1 or int(coordinates[1]) > 3:
        print("Coordinates should be from 1 to 3!")
        get_coordinates()
    elif cell_array[int(coordinates[0]) - 1][int(coordinates[1]) - 1] == "X" or cell_array[int(coordinates[0]) - 1][int(coordinates[1]) - 1] == "O":
        print("This cell is occupied! Choose another one!")
        get_coordinates()
    else:
        cell_array[int(coordinates[0]) - 1][int(coordinates[1]) - 1] = player

def print_cells():
    print("---------")
    print("| " + cell_array[0][0] + " " + cell_array[0][1] + " " + cell_array[0][2] + " |")
    print("| " + cell_array[1][0] + " " + cell_array[1][1] + " " + cell_array[1][2] + " |")
    print("| " + cell_array[2][0] + " " + cell_array[2][1] + " " + cell_array[2][2] + " |")
    print("---------")


def who_wins():
    zeroes = cells.count(x)
    xs = cells.count(o)
    winner = []
    count_empty = 0
    for row in cell_array:
        count_empty += row.count("_")

    if 'X' == cell_array[0][0] == cell_array[0][1] == cell_array[0][2] or 'O' == cell_array[0][0] == cell_array[0][1] == cell_array[0][2]:
        winner.append(cells[0][0])
    if 'X' == cell_array[1][0] == cell_array[1][1] == cell_array[1][2] or 'O' == cell_array[1][0] == cell_array[1][1] == cell_array[1][2]:
        winner.append(cells[1][0])
    if 'X' == cell_array[2][0] == cell_array[2][1] == cell_array[2][2] or 'O' == cell_array[2][0] == cell_array[2][1] == cell_array[2][2]:
        winner.append(cell_array[2][0])
    if 'X' == cell_array[0][0] == cell_array[1][1] == cell_array[2][2] or 'O' == cell_array[0][0] == cell_array[1][1] == cell_array[2][2]:
        winner.append(cell_array[0][0])
    if 'X' == cell_array[0][2] == cell_array[1][1] == cell_array[2][0] or 'O' == cell_array[0][2] == cell_array[1][1] == cell_array[2][0]:
        winner.append(cell_array[0][2])
    if 'X' == cell_array[0][0] == cell_array[1][0] == cell_array[2][0] or 'O' == cell_array[0][0] == cell_array[1][0] == cell_array[2][0]:
        winner.append(cell_array[0][0])
    if 'X' == cell_array[0][1] == cell_array[1][1] == cell_array[2][1] or 'O' == cell_array[0][1] == cell_array[1][1] == cell_array[2][1]:
        winner.append(cell_array[0][1])
    if 'X' == cell_array[0][2] == cell_array[1][2] == cell_array[2][2] or 'O' == cell_array[0][2] == cell_array[1][2] == cell_array[2][2]:
        winner.append(cell_array[0][2])

    if abs(zeroes - xs) > 1 or len(winner) > 1:
        print_cells()
        print("Impossible")
    elif len(winner) == 1:
        print_cells()
        print(winner[0] + " wins")
    elif count_empty == 0:
        print_cells()
        print("Draw")
    else:
        return 0


x = "X"
o = "O"
cells = "_________"
cell_array = [[cells[0], cells[1],cells[2]],
              [cells[3], cells[4], cells[5]],
              [cells[6], cells[7], cells[8]]]
counter = 0
player = 'x'
while who_wins() == 0:
    print_cells()
    if counter % 2 == 0:
        player = "X"
    else:
        player = 'O'
    get_coordinates()
    counter += 1