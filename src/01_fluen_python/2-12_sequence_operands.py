from helpers.string_formatter import print_marked_string

# Using + and * with sequences
print_marked_string("+ & * with sequences")

l = [1, 2, 3]
print(f'l: {l}')
print(f'"l * 5": {l * 5}')

# Example 2-12. A list with 3 lists of length 3 can represent a Tic-tac-toe board.
print_marked_string("Example 2-12")
board = [["_"] * 3 for i in range(3)]
print(f"board: {board}")
board[1][2] = "0"
print(f"board: {board}")

# Example 2-12 is same as:
# board = []
# for i in range(3):
#     row = ['_'] * 3
#     board.append(row)

# Example 2-13. A list with with three references to the same list is useless.
print_marked_string("Example 2-13")
weird_board = [["_"] * 3] * 3
print(f"weird board: {weird_board}")
weird_board[1][2] = "0"
print(f"weird board: {weird_board}")

# Example 2-13 is same as:
# row = ['_'] * 3
# board = []
# for i in range(3):
#     board.append(row)