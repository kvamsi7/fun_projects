import random

def start_game():
    mat = []
    for i in range(4):
        mat.append([0]*4)
    return mat


def add_new_2(mat):
    r = random.randint(0,3)
    c = random.randint(0,3)
    while(mat[r][c] != 0):
        r = random.randint(0,3)
        c = random.randint(0,3)
    mat[r][c] = 2

def compress(mat):
    new_mat = []
    for i in range(4):
        new_mat.append([0]*4)
    change = False
    for i in range(4):
        pos = 0 
        for j in range(4):
            if mat[i][j] != 0:
                new_mat[i][pos] = mat[i][j]
                if j != pos:
                    change = True
                pos += 1
    # print(new_mat)
    return new_mat,change

def merge(mat):
    change = False
    for i in range(4):
        for j in range(3):
            if mat[i][j] == mat[i][j+1] and mat[i][j] != 0:
                change = True
                mat[i][j] = mat[i][j] * 2
                mat[i][j+1] = 0
    return change

def reverse(mat):
    new_mat = []
    for i in range(4):
        new_mat.append([])
        for j in range(4):
            new_mat[i].append(mat[i][4-j-1])
    return new_mat

def transpose(mat):
    new_mat = []
    for i in range(4):
        new_mat.append([])
        for j in range(4):
            new_mat[i].append(mat[j][i])
    return new_mat

def move_left(mat):
    mat,change1 = compress(mat)
    change2 = merge(mat)
    change = change1 or change2
    mat,_ = compress(mat)
    return mat,change

def move_right(mat):
    mat = reverse(mat)
    mat,change1 = compress(mat)
    change2 = merge(mat)
    change = change1 or change2
    mat,_ = compress(mat)
    mat = reverse(mat)
    return mat,change
    
def move_up(mat):
    mat = transpose(mat)
    mat,change1 = compress(mat)
    change2 = merge(mat)
    change = change1 or change2
    mat,_ = compress(mat)
    mat = transpose(mat)
    return mat,change

def move_down(mat):
    mat = transpose(mat)
    mat = reverse(mat)
    mat,change1 = compress(mat)
    change2 = merge(mat)
    change = change1 or change2
    mat,_ = compress(mat)
    mat = reverse(mat)
    mat = transpose(mat)
    return mat,change
 
def get_current_state(mat):

    # anywhere 2048 is proesent
    for i in range(4):
        for j in range(4):
            if (mat[i][j] == 2048):
                return "WON"
    # anywhere 0 is present
    for i in range(4):
        for j in range(4):
            if(mat[i][j] == 0):
                return "GAME NOT OVER"
    # Every row and column except the last row and last column
    for i in range(3):
        for j in range(3):
            if(mat[i][j] == mat[i+1][j] or mat[i][j] == mat[i][j+1]):
                return "GAME NOT OVER"
    # last row
    for j in range(3):
        if mat[3][j] == mat[3][j+1]:
            return "GAME NOT OVER"

    # last column
    for i in range(3):
        if mat[i][3] == mat[i+1][3]:
            return "GAME NOT OVER"
            
    return "LOST"