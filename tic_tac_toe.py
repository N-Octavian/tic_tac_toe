def get_coordinates(cell_array, player):
    coordinates = input("Enter the coordinates: ")
    coordinates = coordinates.split()
    if len(coordinates) < 2:
        print("Enter coordinates in this format: row column")
    elif not coordinates[0].isnumeric() or not coordinates[1].isnumeric():
        print("You should enter numbers!")
        get_coordinates(cell_array, player)
    elif int(coordinates[0]) < 1 or int(coordinates[0]) > 3 or int(coordinates[1]) < 1 or int(coordinates[1]) > 3:
        print("Coordinates should be from 1 to 3!")
        get_coordinates(cell_array, player)
    elif cell_array[int(coordinates[0]) - 1][int(coordinates[1]) - 1] == "X" or cell_array[int(coordinates[0]) - 1][int(coordinates[1]) - 1] == "O":
        print("This cell is occupied! Choose another one!")
        get_coordinates(cell_array, player)
    else:
        cell_array[int(coordinates[0]) - 1][int(coordinates[1]) - 1] = player


def print_cells(cell_array):
    print("---------")
    print("| " + cell_array[0][0] + " " + cell_array[0][1] + " " + cell_array[0][2] + " |")
    print("| " + cell_array[1][0] + " " + cell_array[1][1] + " " + cell_array[1][2] + " |")
    print("| " + cell_array[2][0] + " " + cell_array[2][1] + " " + cell_array[2][2] + " |")
    print("---------")


def who_wins(cell_array):
    zeroes = 0
    xs = 0
    winner = []
    count_empty = 0
    for row in cell_array:
        zeroes += row.count("O")
        xs += row.count("X")
        count_empty += row.count("_")

    if 'X' == cell_array[0][0] == cell_array[0][1] == cell_array[0][2] or 'O' == cell_array[0][0] == cell_array[0][1] == cell_array[0][2]:
        winner.append(cell_array[0][0])
    if 'X' == cell_array[1][0] == cell_array[1][1] == cell_array[1][2] or 'O' == cell_array[1][0] == cell_array[1][1] == cell_array[1][2]:
        winner.append(cell_array[1][0])
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
        print_cells(cell_array)
        print("Impossible")
    elif len(winner) == 1:
        print_cells(cell_array)
        print(winner[0] + " wins")
    elif count_empty == 0:
        print_cells(cell_array)
        print("Draw")
    else:
        return 0


def main():

    cell_array = [["_", "_", "_"],
                  ["_", "_", "_"],
                  ["_", "_", "_"]]
    counter = 0
    while who_wins(cell_array) == 0:
        print_cells(cell_array)
        if counter % 2 == 0:
            player = "X"
        else:
            player = 'O'
        get_coordinates(cell_array, player)
        counter += 1


main()