# Testing

board_1 = ["O", "X", " ", " ", "X", " ", "X", "O", " "]
width = 3
board_2 = ["O", "X", " ", " ", "X", " ", "X", "O", " ", "O"]
width = 5

# Function

def display_board(board, width):

    start = 0
    end = 0
    toe = ''

    for i in range(int(len(board)/width)):
        end += width
        tic = '|'.join([f' {i} ' for i in board][start:end])
        tac = ''.join(['-' for i in range(len(tic))])
        start += width
        toe = (toe + tic + '\n' + tac + '\n') \
            if i!= (len(board)/width - 1) else (toe + tic)

    return toe

print(display_board(board_1, 3))
print('')
print(display_board(board_2, 5))
