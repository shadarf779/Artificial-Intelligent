#8 Puzzle Challenge with out AI


#First Goal in 8 Puzzle try to get 1 to the [0],[0] 

def find(board , value):
    m=0
    n=0
    for i in board:
        for j in i:
            if (board[m][n] == value ):
                return m , n 
            n = n+1
        m = m+1
        n=0
def left(board , m , n):
    if(board[m][n]==0):
        board[m][n] = board[m][n-1] 
        board[m][n-1] =0
        return board
    else:
        return None
def up(board , m , n):
    if(board[m][n]==0):
        board[m][n] = board[m-1][n] 
        board[m-1][n] = 0
        return board
    else:
        return None
def right(board , m , n):
    if(board[m][n]==0):
        board[m][n] = board[m][n+1] 
        board[m][n+1] =0
        return board
    else:
        return None
    
def down(board , m , n):
    if(board[m][n]==0):
        board[m][n] = board[m+1][n] 
        board[m+1][n] =0
        return board
    else:
        return None
def take_the_empty_cell_to00(board,m,n):
    leng = m
    for i in range(leng):
        board = up(board ,  m, n)
        m= m -1
    leng = n
    for j in range(leng):
        board = left(board , m , n)
        n = n-1
def first_goal(board):
    if(board[0][0] == 1):
        return (board[0][0])
    else:
        m , n = find(board , 0)
        print(m ,n)
        take_the_empty_cell_to00(board,m,n)
        print (board)
        
        m1 , n1 = find(board , 1)
        print(m ,n)
        right(board , 0,0)
        leng = m1
        for i in range(leng):
            board = up(board ,  m, n)
            m= m -1
        leng = n1
        for j in range(leng):
            board = left(board , m , n)
            n = n-1


        return board[0][0]

       

# Assert is 1 in the [0][0]?

assert first_goal(
board = [
        [1 , 2 , 3],
        [4 , 0 , 5],
        [7 , 8 , 6]
    ]
) == 1
assert first_goal(
board = [
        [2 , 1 , 3],
        [4 , 5 , 6],
        [7 , 0 , 8]
    ]
) == 1

# assert first_goal(
# board = [
#         [2 , 3 , 1],
#         [4 , 5 , 6],
#         [7 , 8 , 0]
#     ]
# ) == 1