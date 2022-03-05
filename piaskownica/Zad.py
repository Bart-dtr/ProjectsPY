# import required module
import chess
 
# create board object
board=chess.Board()
 
# display chess board
print(board)


x = (input(" Enter your move example: e4: "))
#row = int(input("Enter a number of row: "))


# moving players
board.push_san((x))
# It means moving the particular piece at
# e place to 4th position
  
# Display chess board 
print(board)
    





