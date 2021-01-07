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

def F(prime = False):
    global faces
    if not prime:
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

def R(prime = False):
    global faces
    if not prime:
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
    
def U(prime = False):
    global faces
    if not prime:
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

def L(prime = False):
    global faces
    if not prime:
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
    
def B(prime = False):
    global faces
    if not prime:
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
    
def D(prime = False):
    global faces
    if not prime:
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
        F(True)
    elif move == "R'":
        R(True)
    elif move == "U'":
        U(True)
    elif move == "L'":
        L(True)
    elif move == "B'":
        B(True)
    elif move == "D'":
        D(True)

scramble = deepcopy(faces)

#region unused and unfinished functions

def E(prime = False):
    cache = [faces[1][7],faces[1][8],faces[1][3]]
    for i  in range(1,4):
        faces[i][7] = faces[i+1][7]
        faces[i][8] = faces[i+1][8]
        faces[i][3] = faces[i+1][3]
    faces[4][7] = cache[0]
    faces[4][8] = cache[1]
    faces[4][3] = cache[2]
    

def M(prime = False):
    cache = [faces[1][1],faces[1][8],faces[1][5]]
    faces[1][1] = faces[5][1]
    faces[1][8] = faces[5][8]
    faces[1][5] = faces[5][5]
    faces[5][1] = faces[3][5]
    faces[5][8] = faces[3][8]
    faces[5][5] = faces[3][1]
    faces[3][1] = faces[0][5]
    faces[3][8] = faces[0][8]
    faces[3][5] = faces[0][1]
    faces[0][1] = cache[0]
    faces[0][8] = cache[1]
    faces[0][5] = cache[2]

def S(prime = False):
    cache = [faces[0][7],faces[0][8],faces[0][3]]
    faces[0][7] = faces[4][5]
    faces[0][8] = faces[4][8]
    faces[0][3] = faces[4][1]
    faces[4][1] = faces[5][7]
    faces[4][8] = faces[5][8]
    faces[4][5] = faces[5][3]
    faces[5][7] = faces[2][5]
    faces[5][8] = faces[2][8]
    faces[5][3] = faces[2][1]
    faces[2][5] = cache[0]
    faces[2][8] = cache[1]
    faces[2][1] = cache[2]
    
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

def changeMoves(Debug = False):
    global moves
    numberOfMoves = 12
    rmoves = moves[::-1]
    for move in range(len(rmoves)):
        if rmoves[move] == numberOfMoves - 1:
            rmoves[move] = 0
            if move > 1:
                if rmoves[move] == rmoves[move - 1] and rmoves[move] == rmoves[move - 2]:
                    rmoves[move - 2] += 1
            continue
        else:
            rmoves[move] += 1
            if move < len(rmoves) - 1:
                if rmoves[move] == rmoves[move + 1] + 6 or rmoves[move] == rmoves[move + 1] - 6:
                    rmoves[move] += 1
            if move < len(rmoves) - 2:
                if rmoves[move] == rmoves[move + 1] and rmoves[move] == rmoves[move + 2]:
                    rmoves[move] += 1
            if move > 0:
                if rmoves[move] == rmoves[move - 1] + 6 or rmoves[move] == rmoves[move - 1] - 6:
                    rmoves[move - 1] += 1
            if rmoves[move] > numberOfMoves - 1:
                rmoves[move] = 0
                continue
            break
    else:
        rmoves.insert(0,0)
        if len(rmoves) > 1:
            if rmoves[0] == rmoves[1] + 6 or rmoves[0] == rmoves[1] - 6:
                rmoves[0] += 1
        if len(rmoves) > 2:
            if rmoves[0] == rmoves[1] and rmoves[0] == rmoves[2]:
                rmoves[0] += 1
    moves = rmoves[::-1]

print(f"Start time: {ctime()}")

# U D L' D L'
while not checkSolve() and len(moves) < 30:
    prevmoves = deepcopy(moves)
    moves2 = []
    changeMoves()
    for i in range(len(prevmoves)):
        if prevmoves[i] != moves[i]:
            if i > ceil(len(prevmoves)/2):
                for j in prevmoves[i:][::-1]:
                    if j == 0:
                        moves2.append(6)
                    elif j == 1:
                        moves2.append(7)
                    elif j == 2:
                        moves2.append(8)
                    elif j == 3:
                        moves2.append(9)
                    elif j == 4:
                        moves2.append(10)
                    elif j == 5:
                        moves2.append(11)
                    elif j == 6:
                        moves2.append(0)
                    elif j == 7:
                        moves2.append(1)
                    elif j == 8:
                        moves2.append(2)
                    elif j == 9:
                        moves2.append(3)
                    elif j == 10:
                        moves2.append(4)
                    elif j == 11:
                        moves2.append(5)
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
            F(True)
        elif move == 7:
            R(True)
        elif move == 8:
            U(True)
        elif move == 9:
            L(True)
        elif move == 10:
            B(True)
        elif move == 11:
            D(True)
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
            solution += "F' "
        elif move == 7:
            solution += "R' "
        elif move == 8:
            solution += "U' "
        elif move == 9:
            solution += "L' "
        elif move == 10:
            solution += "B' "
        elif move == 11:
            solution += "D' "
    print(f"Scramble algorithm: {scrambleAlgStr}")
    print(f"Solve algorithm: {solution}")
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