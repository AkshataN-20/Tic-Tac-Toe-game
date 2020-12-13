from IPython.display import clear_output
board = {'7': ' ' , '8': ' ' , '9': ' ' ,
         '4': ' ' , '5': ' ' , '6': ' ' ,
         '1': ' ' , '2': ' ' , '3': ' ' }
def PrintBoard(board):
    print(board['7'] + '|' + board['8'] + '|' + board['9'])
    print('-+-+-')
    print(board['4'] + '|' + board['5'] + '|' + board['6'])
    print('-+-+-')
    print(board['1'] + '|' + board['2'] + '|' + board['3'])

def game():
    turn = 'O'
    count= 0
    while True:
        PrintBoard(board)
        move= input("It's your turn "+turn+". Which place do you want to move?")
        clear_output()
        if board[move] ==' ':
            board[move] =turn
            count+=1
        else:
            print("The place is already occupied. Try next one: ")
            continue
            
         #Now we will check if player X or Y won or not
        if board['7']==board['8']==board['9'] != ' ':
            print("\n Game over \n")
            print("** "+turn+" won. ***")
            break
        elif board['4']==board['5']==board['6'] != ' ':
            print("\n Game over \n")
            print("** " +turn+" won. ***")
            break
        elif board['1']==board['2']==board['3'] != ' ':
            print("\n Game over \n")
            print("** "+turn+" won. ***")
            break
        elif board['1']==board['4']==board['7'] != ' ':
            print("\n Game over \n")
            print("** "+turn+" won. ***")
            break
        elif board['2']==board['5']==board['8'] != ' ':
            print("\n Game over \n")
            print("** "+turn+" won. ***")
            break
        elif board['3']==board['6']==board['9'] != ' ':
            print("\n Game over \n")
            print("** "+turn+" won. ***")
            break
        elif board['7']==board['5']==board['3'] != ' ':
            print("\n Game over \n")
            print("** "+turn+" won. ***")
            break
        elif board['1']==board['5']==board['9'] != ' ':
            print("\n Game over \n")
            print("** "+turn+" won. ***")
            break
            
        #incase neither X or O get won
        if count==9:
            print("Game over!! \n")
            print("The game is Draw!!")
            break
            
        #changing the player
        if turn == 'O':
            turn='X'
        else:
            turn='O'
game()