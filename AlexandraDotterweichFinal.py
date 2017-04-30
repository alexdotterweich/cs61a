
# this is the data type that represents the board in this tic tac to game
class board():
	
    def __init__(self): 
        self.board = [[' ', ' ', ' '],
                      [' ', ' ', ' '],
	    			  [' ', ' ', ' ']]

    def get_board(self):
        return self.board

    def set_board(self, row, col, player):
        self.board[row][col] = player

    def get_square(self, row, col):
        return self.board[row][col]

    # this checks all possible cases that would result in "game over" 
    def end_game(self, player):
        if self.get_square(0,0) == player and self.get_square(0,1) == player and self.get_square(0,2) == player:
            return True
        elif self.get_square(1,0) == player and self.get_square(1,1) == player and self.get_square(1,2) == player:
            return True 
        elif self.get_square(2,0) == player and self.get_square(2,1) == player and self.get_square(2,2) == player:
            return True 
        elif self.get_square(0,0) == player and self.get_square(1,1) == player and self.get_square(2,2) == player:
            return True 
        elif self.get_square(2,0) == player and self.get_square(1,1) == player and self.get_square(0,2) == player:
            return True
        elif self.get_square(0,0) == player and self.get_square(1,0) == player and self.get_square(2,0) == player:
            return True
        elif self.get_square(0,1) == player and self.get_square(1,1) == player and self.get_square(2,1) == player:
            return True
        elif self.get_square(0,2) == player and self.get_square(1,2) == player and self.get_square(2,2) == player:
            return True
        else:
            return False

    # this is the graphical representation of the game        
    def print_board(self):
        print ('---------------------------')
        print ('   0 1 2   Cols')
        print ('')
        print ('0  ' + str(self.get_square(0, 0)) + '|' + str(self.get_square(0, 1)) + '|' + str(self.get_square(0, 2)))
        print ('   ------')
        print ('1  ' + str(self.get_square(1, 0)) + '|' + str(self.get_square(1, 1)) + '|' + str(self.get_square(1, 2)))
        print ('   ------')
        print ('2  ' + str(self.get_square(2, 0)) + '|' + str(self.get_square(2, 1)) + '|' + str(self.get_square(2, 2)))
        print ('')
        print ("Rows")
        print ('---------------------------')

    # this checks to see if the board is full, it does this because if 
    # no one has won the game but the board is full, the game needs to end

    def full(self):
        for i in range (0,3):
            for k in range (0,3):
                if self.get_square(i, k) == ' ':
                    return False
        return True

# this is the recursive function that represents the two players in the game, the AI and the human
# "X" represents the human, "O" represents the AI 
def player(board, player_type):
    

    if player_type == 'X':

    #this is the human playing, their input is always recorded

        board.print_board()
        # this checks to see if the end game is true for either player
        if board.end_game(player_type) or board.end_game(player_oposite(player_type)):
            print ("Game over")
            print ("type:")
            print ("b = board()")
            print ("player(b, 'X')")
            print ("to restart")
            return 

        # this checks to make sure input is valid and sets it to the variable "col" 
        def col_asker():
            print ('Choose the column you would like to select from 0 - 2')
            col = input()
            try:
                col = int(col)
                if col < 0 or col > 2:
                    raise ValueError
            except ValueError:
                print ('try again')
                return col_asker()
            return col

        col = col_asker()

        # this checks to make sure input is valid and sets it to the variable "row" 
        def row_asker():
            print ('Choose the row you would like to select from 0 - 2')
            row = input()
            try:
                row = int(row)
                if row < 0 or row > 2:
                    raise ValueError
            except ValueError:
                print ('try again')
                return row_asker()
            return row

        row = row_asker() 
        if board.get_square(row, col) != ' ':
            print ('Square already taken try again')
            player(board, 'X')
        # this sets the board for the player based on the player's input
        board.set_board(row, col, player_type)

        # tie game base case
        if board.full():
            board.print_board()
            print ('Tie game')
            print ("type:")
            print ("b = board()")
            print ("player(b, 'X')")
            print ("to restart")
            return
        
            
        return player(board, 'O')


    # the AI case of the player function
    if player_type == 'O':

        # this checks to see if the game is over
        if board.end_game(player_type) or board.end_game(player_oposite(player_type)):
            board.print_board()
            print ("Game over")
            print ("type:")
            print ("b = board()")
            print ("player(b, 'X')")
            print ("to restart")
            return

        # calls the AI function, which returns the board location it wants it to play
        ai_response = ai(board)
        board.set_board(ai_response[0], ai_response[1], player_type)
        return player(board, 'X')

# returns the opposite player
def player_oposite(player_type):
    if player_type == 'O':
        return 'X'
    else:
        return 'O'

# this is the "brain" of the AI, it defines what the AI will make based on what the board looks like
def ai(board):
    print (will_player_win(board, 'O'))
    if will_player_win(board, 'O') != None:
        return will_player_win(board, 'O')
    if will_player_win(board, 'X') != None:
        return will_player_win(board, 'X')

    for i in range (0,3):
        for k in range (0,3):
            if board.get_square(i, k) == ' ':
                return (i,k)


# checks to see if the move will make a player win 
def will_player_win(board, player_type):
    for i in range (0,3):
        for k in range (0,3):
            if board.get_square(i, k) == ' ':

                board.set_board(i, k, player_type)
                if board.end_game(player_type):
                    board.set_board(i, k, ' ')
                    return (i, k)
                board.set_board(i, k, ' ')
    return None


# initialization call 
b = board()
player(b, 'X')


