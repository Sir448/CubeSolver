import tkinter as tk
from copy import deepcopy
from time import time, ctime

scrambleAlgStr = input("What is the scramble algorithm? ")
print(scrambleAlgStr)
scrambleAlg = scrambleAlgStr.split()

start = update = time()


#region backup solve state
faces = [
    [0,0,0,0,0,0,0,0,0],
    [1,1,1,1,1,1,1,1,1],
    [2,2,2,2,2,2,2,2,2],
    [3,3,3,3,3,3,3,3,3],
    [4,4,4,4,4,4,4,4,4],
    [5,5,5,5,5,5,5,5,5]
    ]
#endregion

#region colour/side/moves legend

# yellow = 0
# green = 1
# orange = 2
# blue = 3
# red = 4
# white = 5

# bottom = 0
# front = 1
# left = 2
# back = 3
# right = 4
# top = 5

# F = 0
# R = 1
# U = 2
# L = 3
# B = 4
# D = 5
# E = 6
# M = 7
# S = 8
# F' = 9
# R' = 10
# U' = 11
# L' = 12
# B' = 13
# D' = 14
# E' = 15
# M' = 16
# S' = 17
# F2 = 18
# R2 = 19
# U2 = 20
# L2 = 21
# B2 = 22
# D2 = 23
# E2 = 24
# M2 = 25
# S2 = 26

#endregion

#region moves

def F(prime = False, double = False):
    global faces
    if double:
        faces[1] = faces[1][-5:-1] + faces[1][:-5] + [faces[1][8]]
        cache = [faces[0][0],faces[0][1],faces[0][2], faces[4][6],faces[4][7],faces[4][0]]
        faces[0][0] = faces[5][4]
        faces[0][1] = faces[5][5]
        faces[0][2] = faces[5][6]
        faces[4][6] = faces[2][2]
        faces[4][7] = faces[2][3]
        faces[4][0] = faces[2][4]
        faces[5][4] = cache[0]
        faces[5][5] = cache[1]
        faces[5][6] = cache[2]
        faces[2][2] = cache[3]
        faces[2][3] = cache[4]
        faces[2][4] = cache[5]
    elif not prime:
        faces[1] = faces[1][-3:-1] + faces[1][:-3] + [faces[1][8]]
        cache = [faces[0][0],faces[0][1],faces[0][2]]
        faces[0][0] = faces[4][6]
        faces[0][1] = faces[4][7]
        faces[0][2] = faces[4][0]
        faces[4][6] = faces[5][4]
        faces[4][7] = faces[5][5]
        faces[4][0] = faces[5][6]
        faces[5][4] = faces[2][2]
        faces[5][5] = faces[2][3]
        faces[5][6] = faces[2][4]
        faces[2][2] = cache[0]
        faces[2][3] = cache[1]
        faces[2][4] = cache[2]
    else:
        faces[1] = faces[1][2:-1] + faces[1][:2] + [faces[1][8]]
        cache = [faces[0][0],faces[0][1],faces[0][2]]
        faces[0][0] = faces[2][2]
        faces[0][1] = faces[2][3]
        faces[0][2] = faces[2][4]
        faces[2][2] = faces[5][4]
        faces[2][3] = faces[5][5]
        faces[2][4] = faces[5][6]
        faces[5][4] = faces[4][6]
        faces[5][5] = faces[4][7]
        faces[5][6] = faces[4][0]
        faces[4][6] = cache[0]
        faces[4][7] = cache[1]
        faces[4][0] = cache[2]

def R(prime = False, double = False):
    global faces
    if double:
        faces[4] = faces[4][-5:-1] + faces[4][:-5] + [faces[4][8]]
        cache = [faces[0][2],faces[0][3],faces[0][4], faces[1][2],faces[1][3],faces[1][4]]
        faces[0][2] = faces[5][2]
        faces[0][3] = faces[5][3]
        faces[0][4] = faces[5][4]
        faces[1][2] = faces[3][6]
        faces[1][3] = faces[3][7]
        faces[1][4] = faces[3][0]
        faces[5][2] = cache[0]
        faces[5][3] = cache[1]
        faces[5][4] = cache[2]
        faces[3][6] = cache[3]
        faces[3][7] = cache[4]
        faces[3][0] = cache[5]
    elif not prime:
        faces[4] = faces[4][-3:-1] + faces[4][:-3] + [faces[4][8]]
        cache = [faces[0][2],faces[0][3],faces[0][4]]
        faces[0][2] = faces[3][6]
        faces[0][3] = faces[3][7]
        faces[0][4] = faces[3][0]
        faces[3][6] = faces[5][2]
        faces[3][7] = faces[5][3]
        faces[3][0] = faces[5][4]
        faces[5][2] = faces[1][2]
        faces[5][3] = faces[1][3]
        faces[5][4] = faces[1][4]
        faces[1][2] = cache[0]
        faces[1][3] = cache[1]
        faces[1][4] = cache[2]
    else:
        faces[4] = faces[4][2:-1] + faces[4][:2] + [faces[4][8]]
        cache = [faces[0][2],faces[0][3],faces[0][4]]
        faces[0][2] = faces[1][2]
        faces[0][3] = faces[1][3]
        faces[0][4] = faces[1][4]
        faces[1][2] = faces[5][2]
        faces[1][3] = faces[5][3]
        faces[1][4] = faces[5][4]
        faces[5][2] = faces[3][6]
        faces[5][3] = faces[3][7]
        faces[5][4] = faces[3][0]
        faces[3][6] = cache[0]
        faces[3][7] = cache[1]
        faces[3][0] = cache[2]
    
def U(prime = False, double = False):
    global faces
    if double:
        faces[5] = faces[5][-5:-1] + faces[5][:-5] + [faces[5][8]]
        cache = [faces[1][0],faces[1][1],faces[1][2], faces[2][0],faces[2][1],faces[2][2]]
        for i in range(3):
            faces[1][i] = faces[3][i]
            faces[2][i] = faces[4][i]
            faces[3][i] = cache[i]
            faces[4][i] = cache[i+3]

    elif not prime:
        faces[5] = faces[5][-3:-1] + faces[5][:-3] + [faces[5][8]]
        cache = [faces[4][0],faces[4][1],faces[4][2]]
        for i in range(3):
            for j in range(3):
                faces[4-i][j] = faces[4-i-1][j]
        for i in range(3):
            faces[1][i] = cache[i]
    else:
        faces[5] = faces[5][2:-1] + faces[5][:2] + [faces[5][8]]
        cache = [faces[1][0],faces[1][1],faces[1][2]]
        for i in range(1,4):
            for j in range(3):
                faces[i][j] = faces[i+1][j]
        for i in range(3):
            faces[4][i] = cache[i]

def L(prime = False, double = False):
    global faces
    if double:
        faces[2] = faces[2][-5:-1] + faces[2][:-5] + [faces[2][8]]
        cache = [faces[0][6],faces[0][7],faces[0][0], faces[1][6],faces[1][7],faces[1][0]]
        faces[0][6] = faces[5][6]
        faces[0][7] = faces[5][7]
        faces[0][0] = faces[5][0]
        faces[1][6] = faces[3][2]
        faces[1][7] = faces[3][3]
        faces[1][0] = faces[3][4]
        faces[5][6] = cache[0]
        faces[5][7] = cache[1]
        faces[5][0] = cache[2]
        faces[3][2] = cache[3]
        faces[3][3] = cache[4]
        faces[3][4] = cache[5]

    elif not prime:
        faces[2] = faces[2][-3:-1] + faces[2][:-3] + [faces[2][8]]
        cache = [faces[0][6],faces[0][7],faces[0][0]]
        faces[0][6] = faces[1][6]
        faces[0][7] = faces[1][7]
        faces[0][0] = faces[1][0]
        faces[1][6] = faces[5][6]
        faces[1][7] = faces[5][7]
        faces[1][0] = faces[5][0]
        faces[5][6] = faces[3][2]
        faces[5][7] = faces[3][3]
        faces[5][0] = faces[3][4]
        faces[3][2] = cache[0]
        faces[3][3] = cache[1]
        faces[3][4] = cache[2]
    else:
        faces[2] = faces[2][2:-1] + faces[2][:2] + [faces[2][8]]
        cache = [faces[0][6],faces[0][7],faces[0][0]]
        faces[0][6] = faces[3][2]
        faces[0][7] = faces[3][3]
        faces[0][0] = faces[3][4]
        faces[3][2] = faces[5][6]
        faces[3][3] = faces[5][7]
        faces[3][4] = faces[5][0]
        faces[5][6] = faces[1][6]
        faces[5][7] = faces[1][7]
        faces[5][0] = faces[1][0]
        faces[1][6] = cache[0]
        faces[1][7] = cache[1]
        faces[1][0] = cache[2]
    
def B(prime = False, double = False):
    global faces
    if double:
        faces[3] = faces[3][-5:-1] + faces[3][:-5] + [faces[3][8]]
        cache = [faces[0][4],faces[0][5],faces[0][6], faces[2][6],faces[2][7],faces[2][0]]
        faces[0][4] = faces[5][0]
        faces[0][5] = faces[5][1]
        faces[0][6] = faces[5][2]
        faces[2][6] = faces[4][2]
        faces[2][7] = faces[4][3]
        faces[2][0] = faces[4][4]
        faces[5][0] = cache[0]
        faces[5][1] = cache[1]
        faces[5][2] = cache[2]
        faces[4][2] = cache[3]
        faces[4][3] = cache[4]
        faces[4][4] = cache[5]
        
    elif not prime:
        faces[3] = faces[3][-3:-1] + faces[3][:-3] + [faces[3][8]]
        cache = [faces[0][4],faces[0][5],faces[0][6]]
        faces[0][4] = faces[2][6]
        faces[0][5] = faces[2][7]
        faces[0][6] = faces[2][0]
        faces[2][6] = faces[5][0]
        faces[2][7] = faces[5][1]
        faces[2][0] = faces[5][2]
        faces[5][0] = faces[4][2]
        faces[5][1] = faces[4][3]
        faces[5][2] = faces[4][4]
        faces[4][2] = cache[0]
        faces[4][3] = cache[1]
        faces[4][4] = cache[2]
    else:
        faces[3] = faces[3][2:-1] + faces[3][:2] + [faces[3][8]]
        cache = [faces[0][4],faces[0][5],faces[0][6]]
        faces[0][4] = faces[4][2]
        faces[0][5] = faces[4][3]
        faces[0][6] = faces[4][4]
        faces[4][2] = faces[5][0]
        faces[4][3] = faces[5][1]
        faces[4][4] = faces[5][2]
        faces[5][0] = faces[2][6]
        faces[5][1] = faces[2][7]
        faces[5][2] = faces[2][0]
        faces[2][6] = cache[0]
        faces[2][7] = cache[1]
        faces[2][0] = cache[2]
    
def D(prime = False, double = False):
    global faces
    if double:
        faces[0] = faces[0][-5:-1] + faces[0][:-5] + [faces[0][8]]
        cache = [faces[1][4],faces[1][5],faces[1][6], faces[2][4],faces[2][5],faces[2][6]]
        for i in range(4,7):
            faces[1][i] = faces[3][i]
            faces[2][i] = faces[4][i]
            faces[3][i] = cache[i-4]
            faces[4][i] = cache[i-1]
    elif not prime:
        faces[0] = faces[0][-3:-1] + faces[0][:-3] + [faces[0][8]]
        cache = [faces[1][4],faces[1][5],faces[1][6]]
        for i in range(1,4):
            for j in range(4,7):
                faces[i][j] = faces[i+1][j]
        for i in range(3):
            faces[4][i+4] = cache[i]
    else:
        faces[0] = faces[0][2:-1] + faces[0][:2] + [faces[0][8]]
        cache = [faces[4][4],faces[4][5],faces[4][6]]
        for i in range(3):
            for j in range(4,7):
                faces[4-i][j] = faces[4-i-1][j]
        for i in range(3):
            faces[1][i+4] = cache[i]

#endregion

# time it takes to solve = 2ms * pow(12,moves - 1)

for move in scrambleAlg:
    if move == "F":
        F()
    elif move == "R":
        R()
    elif move == "U":
        U()
    elif move == "L":
        L()
    elif move == "B":
        B()
    elif move == "D":
        D()
    elif move == "F'":
        F(prime = True)
    elif move == "R'":
        R(prime = True)
    elif move == "U'":
        U(prime = True)
    elif move == "L'":
        L(prime = True)
    elif move == "B'":
        B(prime = True)
    elif move == "D'":
        D(prime = True)

scramble = deepcopy(faces)

#region unused and unfinished functions

def E(prime = False, double = False):
    if double:
        cache = [faces[1][3],faces[1][7],faces[1][8],faces[2][3],faces[2][7],faces[2][8]]
        faces[1][3] = faces[3][3]
        faces[1][7] = faces[3][7]
        faces[1][8] = faces[3][8]
        faces[3][3] = cache[0]
        faces[3][7] = cache[1]
        faces[3][8] = cache[2]
        faces[2][3] = faces[4][3]
        faces[2][7] = faces[4][7]
        faces[2][8] = faces[4][8]
        faces[4][3] = cache[3]
        faces[4][7] = cache[4]
        faces[4][8] = cache[5]
    elif not prime:
        cache = [faces[1][3],faces[1][7],faces[1][8]]
        for i in range(1,4):
            faces[i][3] = faces[i+1][3]
            faces[i][7] = faces[i+1][7]
            faces[i][8] = faces[i+1][8]
        faces[4][3] = cache[0]
        faces[4][7] = cache[1]
        faces[4][8] = cache[2]
    else:
        cache = [faces[4][3],faces[4][7],faces[4][8]]
        for i in range(3):
            faces[4-i][3] = faces[3-i][3]
            faces[4-i][7] = faces[3-i][7]
            faces[4-i][8] = faces[3-i][8]
        faces[1][3] = cache[0]
        faces[1][7] = cache[1]
        faces[1][8] = cache[2]

def M(prime = False, double = False):
    if double: 
        cache = [faces[0][1],faces[0][5],faces[0][8],faces[1][1],faces[1][5],faces[1][8]]
        faces[0][1] = faces[5][1]
        faces[0][5] = faces[5][5]
        faces[0][8] = faces[5][8]
        faces[5][1] = cache[0]
        faces[5][5] = cache[1]
        faces[5][8] = cache[2]
        faces[1][1] = faces[3][5]
        faces[1][5] = faces[3][1]
        faces[1][8] = faces[3][8]
        faces[3][1] = cache[4]
        faces[3][5] = cache[3]
        faces[3][8] = cache[5]
    elif not prime:
        cache = [faces[0][1],faces[0][5],faces[0][8]]
        faces[0][1] = faces[1][1]
        faces[0][5] = faces[1][5]
        faces[0][8] = faces[1][8]
        faces[1][1] = faces[5][1]
        faces[1][5] = faces[5][5]
        faces[1][8] = faces[5][8]
        faces[5][1] = faces[3][5]
        faces[5][5] = faces[3][1]
        faces[5][8] = faces[3][8]
        faces[3][1] = cache[1]
        faces[3][5] = cache[0]
        faces[3][8] = cache[2]
    else:
        cache = [faces[0][1],faces[0][5],faces[0][8]]
        faces[0][1] = faces[3][5]
        faces[0][5] = faces[3][1]
        faces[0][8] = faces[3][8]
        faces[3][1] = faces[5][5]
        faces[3][5] = faces[5][1]
        faces[3][8] = faces[5][8]
        faces[5][1] = faces[1][1]
        faces[5][5] = faces[1][5]
        faces[5][8] = faces[1][8]
        faces[1][1] = cache[0]
        faces[1][5] = cache[1]
        faces[1][8] = cache[2]
    

def S(prime = False, double = False):
    if double: 
        cache = [faces[0][3],faces[0][7],faces[0][8],faces[2][1],faces[2][5],faces[2][8]]
        faces[0][3] = faces[5][7]
        faces[0][7] = faces[5][3]
        faces[0][8] = faces[5][8]
        faces[5][3] = cache[1]
        faces[5][7] = cache[0]
        faces[5][8] = cache[2]
        faces[2][1] = faces[4][5]
        faces[2][5] = faces[4][1]
        faces[2][8] = faces[4][8]
        faces[4][1] = cache[4]
        faces[4][5] = cache[3]
        faces[4][8] = cache[5]
    elif not prime:
        cache = [faces[0][3],faces[0][7],faces[0][8]]
        faces[0][3] = faces[4][1]
        faces[0][7] = faces[4][5]
        faces[0][8] = faces[4][8]
        faces[4][1] = faces[5][7]
        faces[4][5] = faces[5][3]
        faces[4][8] = faces[5][8]
        faces[5][3] = faces[2][1]
        faces[5][7] = faces[2][5]
        faces[5][8] = faces[2][8]
        faces[2][1] = cache[1]
        faces[2][5] = cache[0]
        faces[2][8] = cache[2]
    else:
        cache = [faces[0][3],faces[0][7],faces[0][8]]
        faces[0][3] = faces[2][5]
        faces[0][7] = faces[2][1]
        faces[0][8] = faces[2][8]
        faces[2][1] = faces[5][3]
        faces[2][5] = faces[5][7]
        faces[2][8] = faces[5][8]
        faces[5][3] = faces[4][5]
        faces[5][7] = faces[4][1]
        faces[5][8] = faces[4][8]
        faces[4][1] = cache[0]
        faces[4][5] = cache[1]
        faces[4][8] = cache[2]
    
    
#endregion

def checkSolve():
    global faces
    for face in faces:
        for piece in range(len(face)-1):
            if face[piece] == face[piece+1]:
                continue
            break
        else:
            continue
        break
    else:
        return True
    return False

moves = []

# F = 0
# R = 1
# U = 2
# L = 3
# B = 4
# D = 5
# E = 6
# M = 7
# S = 8
# F' = 9
# R' = 10
# U' = 11
# L' = 12
# B' = 13
# D' = 14
# E' = 15
# M' = 16
# S' = 17
# F2 = 18
# R2 = 19
# U2 = 20
# L2 = 21
# B2 = 22
# D2 = 23
# E2 = 24
# M2 = 25
# S2 = 26

def canBeSlice(rmoves,move):
    if rmoves[move] == 0 and rmoves[move+1] == 13:
        return True
    elif rmoves[move] == 1 and rmoves[move+1] == 12:
        return True
    elif rmoves[move] == 2 and rmoves[move+1] == 14:
        return True
    elif rmoves[move] == 3 and rmoves[move+1] == 10:
        return True
    elif rmoves[move] == 4 and rmoves[move+1] == 9:
        return True
    elif rmoves[move] == 5 and rmoves[move+1] == 11:
        return True
    elif rmoves[move + 1] == 0 and rmoves[move] == 13:
        return True
    elif rmoves[move + 1] == 1 and rmoves[move] == 12:
        return True
    elif rmoves[move + 1] == 2 and rmoves[move] == 14:
        return True
    elif rmoves[move + 1] == 3 and rmoves[move] == 10:
        return True
    elif rmoves[move + 1] == 4 and rmoves[move] == 9:
        return True
    elif rmoves[move + 1] == 5 and rmoves[move] == 11:
        return True
    elif rmoves[move] == 18 and rmoves[move + 1] == 22:
        return True
    elif rmoves[move] == 19 and rmoves[move + 1] == 21:
        return True
    elif rmoves[move] == 20 and rmoves[move + 1] == 23:
        return True
    elif rmoves[move + 1] == 18 and rmoves[move] == 22:
        return True
    elif rmoves[move + 1] == 19 and rmoves[move] == 21:
        return True
    elif rmoves[move + 1] == 20 and rmoves[move] == 23:
        return True
    else:
        return False

def changeMoves(Debug = False):
    global moves
    numberOfMoves = 27
    rmoves = moves[::-1]
    for move in range(len(rmoves)):
        if rmoves[move] == numberOfMoves - 1:
            rmoves[move] = 0
            if move > 0:
                if rmoves[move] == rmoves[move - 1]:
                    rmoves[move - 1] += 1
            continue
        else:
            rmoves[move] += 1
            if move < len(rmoves) - 1:
                if rmoves[move] == rmoves[move + 1] + 9 or rmoves[move] == rmoves[move + 1] - 9 or rmoves[move] == rmoves[move + 1] + 18 or rmoves[move] == rmoves[move + 1] - 18 or rmoves[move] == rmoves[move + 1] or canBeSlice(rmoves,move):
                    rmoves[move] += 1
            if move > 0:
                if rmoves[move] == rmoves[move - 1] + 9 or rmoves[move] == rmoves[move - 1] - 9 or rmoves[move] == rmoves[move - 1] + 18 or rmoves[move] == rmoves[move - 1] - 18 or canBeSlice(rmoves,move - 1):
                    rmoves[move - 1] += 1
            if rmoves[move] > numberOfMoves - 1:
                rmoves[move] = 0
                continue
            break
    else:
        rmoves.insert(0,0)
        if len(rmoves) > 1:
            if rmoves[0] == rmoves[1] + 9 or rmoves[0] == rmoves[1] - 9 or rmoves[0] == rmoves[1] + 18 or rmoves[0] == rmoves[1] - 18 or rmoves[0] == rmoves[1] or canBeSlice(rmoves,0):
                rmoves[0] += 1
    moves = rmoves[::-1]

print(f"Start time: {ctime()}")

# U R' F' B B R R U'
while not checkSolve() and len(moves) < 30:
    prevmoves = deepcopy(moves)
    moves2 = []
    changeMoves()
    for i in range(len(prevmoves)):
        if prevmoves[i] != moves[i]:
            if i > ceil(len(prevmoves)/2):
                for j in prevmoves[i:][::-1]:
                    if j == 0:
                        moves2.append(9)
                    elif j == 1:
                        moves2.append(10)
                    elif j == 2:
                        moves2.append(11)
                    elif j == 3:
                        moves2.append(12)
                    elif j == 4:
                        moves2.append(13)
                    elif j == 5:
                        moves2.append(14)
                    elif j == 6:
                        moves2.append(15)
                    elif j == 7:
                        moves2.append(16)
                    elif j == 8:
                        moves2.append(17)
                    elif j == 9:
                        moves2.append(0)
                    elif j == 10:
                        moves2.append(1)
                    elif j == 11:
                        moves2.append(2)
                    elif j == 12:
                        moves2.append(3)
                    elif j == 13:
                        moves2.append(4)
                    elif j == 14:
                        moves2.append(5)
                    elif j == 15:
                        moves2.append(6)
                    elif j == 16:
                        moves2.append(7)
                    elif j == 17:
                        moves2.append(8)
                    elif move == 18:
                        moves2.append(18)
                    elif move == 19:
                        moves2.append(19)
                    elif move == 20:
                        moves2.append(20)
                    elif move == 21:
                        moves2.append(21)
                    elif move == 22:
                        moves2.append(22)
                    elif move == 23:
                        moves2.append(23)
                    elif move == 24:
                        moves2.append(24)
                    elif move == 25:
                        moves2.append(25)
                    elif move == 26:
                        moves2.append(26)
                moves2 += moves[i:]
            else:
                faces = deepcopy(scramble)
                moves2 = deepcopy(moves)
            break
        
    for move in moves2:
        if move == 0:
            F()
        elif move == 1:
            R()
        elif move == 2:
            U()
        elif move == 3:
            L()
        elif move == 4:
            B()
        elif move == 5:
            D()
        elif move == 6:
            E()
        elif move == 7:
            M()
        elif move == 8:
            S()
        elif move == 9:
            F(prime = True)
        elif move == 10:
            R(prime = True)
        elif move == 11:
            U(prime = True)
        elif move == 12:
            L(prime = True)
        elif move == 13:
            B(prime = True)
        elif move == 14:
            D(prime = True)
        elif move == 15:
            E(prime = True)
        elif move == 16:
            M(prime = True)
        elif move == 17:
            S(prime = True)
        elif move == 18:
            F(double = True)
        elif move == 19:
            R(double = True)
        elif move == 20:
            U(double = True)
        elif move == 21:
            L(double = True)
        elif move == 22:
            B(double = True)
        elif move == 23:
            D(double = True)
        elif move == 24:
            E(double = True)
        elif move == 25:
            M(double = True)
        elif move == 26:
            S(double = True)
    if time() - update > 600:
        print(ctime())
        print(f"Moves: {moves}")
        update = time()

if len(moves) == 0:
    print("Already Solved")
elif len(moves) >= 40:
    print("Cube unsolveable")
else:
    solution = ""
    for move in moves:
        if move == 0:
            solution += "F "
        elif move == 1:
            solution += "R "
        elif move == 2:
            solution += "U "
        elif move == 3:
            solution += "L "
        elif move == 4:
            solution += "B "
        elif move == 5:
            solution += "D "
        elif move == 6:
            solution += "E "
        elif move == 7:
            solution += "M "
        elif move == 8:
            solution += "S "
        elif move == 9:
            solution += "F' "
        elif move == 10:
            solution += "R' "
        elif move == 11:
            solution += "U' "
        elif move == 12:
            solution += "L' "
        elif move == 13:
            solution += "B' "
        elif move == 14:
            solution += "D' "
        elif move == 15:
            solution += "E' "
        elif move == 16:
            solution += "M' "
        elif move == 17:
            solution += "S' "
        elif move == 18:
            solution += "F2 "
        elif move == 19:
            solution += "R2 "
        elif move == 20:
            solution += "U2 "
        elif move == 21:
            solution += "L2 "
        elif move == 22:
            solution += "B2 "
        elif move == 23:
            solution += "D2 "
        elif move == 24:
            solution += "E2 "
        elif move == 25:
            solution += "M2 "
        elif move == 26:
            solution += "S2 "
    print(f"Scramble algorithm: {scrambleAlgStr}")
    print(f"Solve algorithm: {solution}")
    print(f"Moves: {moves}")
    period = time() - start
    period2 = period
    timeMsg = "Found solution in "
    if period2 >= 86400:
        timeMsg += str(int(period//86400)) + "d "
        period %= 86400
    if period2 >= 3600:
        timeMsg += str(int(period//3600)) + "h "
        period %= 3600
    if period2 >= 60:
        timeMsg += str(int(period//60)) + "m "
        period %= 60
    timeMsg += str(int(period//1)) + "s "
    period %= 1
    timeMsg += str(int(period//0.001)) + "ms "
    print(timeMsg)


input()