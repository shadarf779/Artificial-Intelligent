#8 Puzzle Challenge with out assistent of AI

#First Goad get the 0 to the [1 , 1 ]
#Second Goal get 1 to the [0],[0] 

board = [
        [0 , 2 , 3],
        [4 , 1 , 5],
        [7 , 8 , 6]
    ]

def find(value):
    global board
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
def take_the_value_to11(m,n):
    global board
    if(m>1):
        up(board ,m ,n)
        m=m-1
    elif(m<1):
        down(board , m , n)
        m=m+1
    if(n>1):
        left(board , m , n)
        n=n-1
    elif(n<1):
        right(board , m , n)
        n=n+1
    return  board
        


#first Goal
def first_goal():
    global board
    if(board[1][1] == 0):
        return (board[1][1])
    else:
        m , n = find(0)
        print(m ,n)
        board = take_the_value_to11(m,n)
        print (board)
    return (board[1][1])
        # m1 , n1 = find(board , 1)
        # print(m ,n)
        # right(board , 0,0)
        # print (board)
        # leng = m1
        # for i in range(leng):
        #     board = up(board ,  m, n)
        #     m= m -1
        # leng = n1
        # for j in range(leng):
        #     board = left(board , m , n)
        #     n = n-1


        # return board[0][0]

       

# First Goal Should be Done 

assert first_goal() == 0


