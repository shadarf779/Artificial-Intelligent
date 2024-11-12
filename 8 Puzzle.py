#8 Puzzle Challenge with out assistent of AI

#First Goad get the 0 to the [1 , 1 ]
#Then get the 0 to the [next to 1 ]
#third Goal get 1 to the [0],[0] 

board = [
        [2 , 8 , 1],
        [4 , 0 , 5],
        [7 , 6 , 3]
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
def left(m , n):
    if(board[m][n]==0):
        board[m][n] = board[m][n-1] 
        board[m][n-1] =0
        return board
    else:
        return None
def up( m , n):
    if(board[m][n]==0):
        board[m][n] = board[m-1][n] 
        board[m-1][n] = 0
        return board
    else:
        return None
def right(m , n):
    global board
    if(board[m][n]==0):

        board[m][n] = board[m][n+1] 
        board[m][n+1] =0
        return board
    else:
        return None  
def down( m , n):
    if(board[m][n]==0):
        board[m][n] = board[m+1][n] 
        board[m+1][n] =0
        return board
    else:
        return None
def take_the_empity_value_to11(m,n):
    global board
    if(m>1):
        up( m ,n)
        m=m-1
    elif(m<1):
        down(  m , n)
        m=m+1
    if(n>1):
        left(  m , n)
        n=n-1
    elif(n<1):
        right( m , n)
        n=n+1


#first Goal
def first_goal():
    global board
    if(board[1][1] == 0):
        return (board[1][1])
    else:
        m , n = find(0)
        print(m ,n)
        take_the_empity_value_to11(m,n)
        print (board)
    return (board[1][1])
 

def take_0_to_near_1(m , n):
    global board
    x = 1
    y= 1
    
    if(m!=1 or n!=1):
        
        if(m>1):
            down( x,y)
            x=x-1
            m=m-1
        elif(m<1):
            up( x,y)
            x=x+1
            m=m+1
        if(n>1):
            right( x,y)
            y=y-1
            n=n-1
        elif(n<1):
            left(x,y)
            y=y+1
            n=n+1
    print(board) 

#second Goal
def second_goal():
    global board
    if(board[0][0] == 1):
        return (board[0][0])
    else:
        m , n = find(1)
        print(m ,n)
        take_0_to_near_1(m,n)
        print (board)
    return (board[0][1])

def take_1_to_11(m,n,x,y):
    global board
    if(m==x):
        if(y<n):
            right(x,y)
            y=y+1
            n=n-1
            down(x,y)
            x=x+1
            left(x,y)
            y=y-1
            left(x,y)
            y=y-1
            up(x,y)
            x=x-1
            right(x,y)
            y=y+1
            n=n-1
    print(board)
    return board[0][0]

def third_goal():
    global board
    if(board[0][0] == 1):
        return (board[0][0])
    else:
        m , n = find(1)
        print(m ,n)
        x,y = find(0)
        take_1_to_11(m,n, x,y)
    return board[0][0]
# First Goal Should be Done 

def take_0_to_near_value(m,n,x,y):
    global board
    if(m!=1 or n!=1):
        if(m>1):
            down( x,y)
            x=x-1
            m=m-1
        elif(m<1):
            up( x,y)
            x=x+1
            m=m+1
        if(n>1):
            right( x,y)
            y=y-1
            n=n-1
        elif(n<1):
            left(x,y)
            y=y+1
            n=n+1
    print(board)

def forth_goal():
    global board
    if(board[2][1] == 0):
        return (board[2][1])
    else:
        m , n = find(3)
        print(m ,n)
        x,y = find(0)
        take_0_to_near_value(m,n,x,y)
    return board[2][1]

def take_the_value_to_01(m,n,x,y):
    global board
    if(m==x):
        if(y<n):
            right(x,y)
            y=y+1
            n=n-1
            up(x,y)
            x=x-1
            left(x,y)
            y=y-1
            down(x,y)
            x=x+1
            n=n-1
            right(x,y)
            y=y+1
            up(x,y)
            x=x-1
            up(x,y)
            x=x-1
            left(x,y)
            y=y-1
            down(x,y)
            y=y+1
            n=n-1
    print(board)
    return board[0][1]

def fifth_goal():
    global board
    if(board[0][2] == 3):
        return (board[0][1])
    else:
        m , n = find(3)
        print(m ,n)
        x,y = find(0)
        take_the_value_to_01(m,n,x,y)
    return board[0][1]

def sixth_goal():
    global board
    if(board[1][1] == 2):
        return (board[1][1])
    else:
        m , n = find(2)
        print(m ,n)
        take_0_to_near_1(m,n)
    return board[1][1]

def take_2_to_next_3(x,y):
    global board

    down(x,y)
    x=x+1
    right(x,y)
    y=y+1
    right(x,y)
    y=y+1
    up(x,y)
    x=x-1
    up(x,y)
    x=x-1
    left(x,y)
    y=y-1
    down(x,y)
    x=x+1
    print(board)


def seventh_goal():
    global board
    if(board[0][1] == 2 and board[0][2]==3):
        return ([board[0][1] , board[0][2]])
    else:
        x , y = find(0)
        print(x ,y)
        take_2_to_next_3(x,y)
    return ([board[0][1] , board[0][2]])

def eighth_goal():
    global board
    if(board[1][0] == 7):
        return (board[1][0])
    else:
        m , n = find(7)
        print(m ,n)
        x,y = find(0)
        take_0_to_near_value(m,n,x,y)
    return board[0][2]

def ninth_goal():
    global board
    if(board[1][1] == 4):
        return (board[1][1])
    else:
        m , n = find(4)
        print(m ,n)
        x,y = find(0)
        take_0_to_near_value(m,n,x,y)
    return board[1][1]

def fix_4_and_7(x,y):
    global board
    print (x,y)
    down(x,y)
    x=x+1
    left(x,y)
    y=y-1
    left(x,y)
    y=y-1
    up(x,y)
    x=x-1
    right(x,y)
    y=y+1

def tenth_goal():
    global board
    if(board[1][0] == 4 and board[2][0]==7):
        return ([board[1][0] , board[2][0]])
    else:
        x , y = find(0)
        print(x ,y)
        fix_4_and_7(x,y)
    print(board)
    return ([board[1][0] , board[2][0]])
def final_goal():
    global board
    if(board[2][2] == 0):
        return (board[2][2])
    else:
        m , n = find(0)
        print(m ,n)
        right(m,n)
        n=n+1
        down(m,n)
        m=m+1
        print (board)
    return (board[2][2])
assert first_goal() == 0


assert second_goal() == 0

assert third_goal() == 1 

assert first_goal() == 0

assert forth_goal() == 0

assert fifth_goal() == 3

assert first_goal() == 0

assert sixth_goal() == 2

assert seventh_goal() == [2,3]

assert first_goal() == 0

assert eighth_goal() == 7

assert ninth_goal() == 4

assert tenth_goal() == [4,7]

assert final_goal() == 0

for i in board:
        print(i)
print("All Goals are Done")









