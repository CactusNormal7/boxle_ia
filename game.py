import copy
import os

board = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 4, 0, 0, 0, 2, 0, 1],
    [1, 0, 0, 0, 4, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 3, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 3, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
]

def print_board(board):
    for row in board:
        for cell in row:
            print(cell, end=" ")
        print()


class Player:
    def __init__(self, name):
        self.name = name
        
    def play(self):
        values = "zqsd"
        a = str(input("zqsd for move : "))
        if not values.__contains__(a) or len(a) < 1 and len(a) > 1:
            print("incorrect input")
            self.play()
        return a
    
class Game:
    def __init__(self, level, p1, isTraining=False):
        self.board = level
        self.players = [p1]
        self.isTraining = isTraining
        self.currentTurn = 0;
        self.positions = {'x' : 0, 'y' : 0}
        self.posof4 = []
        self.oldpos = {'x' : 0, 'y' : 0}
    
    def find_position_of_2(self):
        for i in range(len(self.board)):
            for j in range(len(self.board[i])):
                if self.board[i][j] == 2:
                    self.positions["x"] = i
                    self.positions["y"] = j
    
    def find_positions_of_4(self):
        positions = []
        for i in range(len(self.board)):
            for j in range(len(self.board[i])):
                if self.board[i][j] == 4:
                    positions.append((i, j))
        self.posof4 = positions
        
    def update_board(self):
        for pos in self.posof4:
            x, y = pos
            self.board[x][y] = 4
    
    def play(self):
        action = self.players[self.currentTurn].play()
        self.oldpos = copy.copy(self.positions)
        moved = False
        hitBox = False
        
        self.update_board()
        
        if action == 'z':
            if self.board[self.positions["x"] - 1][self.positions["y"]] == 0 or self.board[self.positions["x"] - 1][self.positions["y"]] == 4:
                self.positions["x"] -= 1
                moved = True
            if self.board[self.positions["x"] - 1][self.positions["y"]] == 3:
                if self.board[self.positions["x"] - 2][self.positions["y"]] == 0:
                    self.positions["x"] -= 1
                    hitBox = True
                    moved = True
        elif action == "q":
            if self.board[self.positions["x"]][self.positions["y"] - 1] == 0 or self.board[self.positions["x"]][self.positions["y"] - 1] == 4:
                self.positions["y"] -= 1
                moved = True
            if self.board[self.positions["x"]][self.positions["y"] - 1] == 3:
                if self.board[self.positions["x"]][self.positions["y"] - 2] == 0:
                    self.positions["y"] -= 1
                    hitBox = True
                    moved = True

        elif action == "s":
            if self.board[self.positions["x"] + 1][self.positions["y"]] == 0:
                self.positions["x"] += 1
                moved = True
            if self.board[self.positions["x"] + 1][self.positions["y"]] == 3:
                if self.board[self.positions["x"] + 2][self.positions["y"]] == 0:
                    self.positions["x"] += 1
                    hitBox = True
                    moved = True
        elif action == "d":
            if self.board[self.positions["x"]][self.positions["y"] + 1] == 0:
                self.positions["y"] += 1
                moved = True
            if self.board[self.positions["x"]][self.positions["y"] + 1] == 3:
                if self.board[self.positions["x"]][self.positions["y" ]+ 2] == 0:
                    self.positions["y"] += 1
                    hitBox = True
                    moved = True
        if moved:
            rara = self.positions["x"] - self.oldpos["x"], self.positions["y"] - self.oldpos["y"]
            rara = "x+" if rara[0] == -1 else "x-" if rara[0] == 1 else "y-" if rara[1] == -1 else "y+"
            print(rara)
            self.board[self.positions["x"]][self.positions["y"]] = 2
            self.board[self.oldpos["x"]][self.oldpos["y"]] = 0
        
            if hitBox:
                if rara == "x+":
                    self.board[self.positions["x"] - 1][self.positions["y"]] = 3
                elif rara == "x-":
                    self.board[self.positions["x"] + 1][self.positions["y"]] = 3
                elif rara == "y+":
                    self.board[self.positions["x"]][self.positions["y"] + 1] = 3
                elif rara == "y-":
                    self.board[self.positions["x"]][self.positions["y"] - 1] = 3
                    
                
        print_board(board=self.board)
            
        
    def run(self):
        self.find_positions_of_4()
        self.find_position_of_2()
        print(self.positions)
        print_board(self.board)
        while True:
            self.play()
            
            
            
p1 = Player("ratio")
p2 = Player("ratio")
partie1 = Game(board, p1,False)
partie1.run()