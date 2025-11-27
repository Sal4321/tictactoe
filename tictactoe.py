#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
TIc Tac Toe with Value Iteration

Created on Mon Oct  6 22:40:32 2025

@author: nazmussalehin
"""
from pprint import pprint
import itertools
import random

class TicTacToe: 
    def __init__(self):
        # Initialize an empty list when the object is created
        # self.board = []
        symbols = ['X', 'O', ' ']
        # generate an empty board
        self.board = [" " for _ in range(9)]
        # self.printboard()
        # Generate all possible combinations (3^9) for state values
        self.boards = list(itertools.product(symbols, repeat=9))
        self.statevalues = []
        self.validstates =[]

    def check_winner(self,board):
        """
        board: 1D list of 9 elements representing a 3x3 tic-tac-toe board
        Index layout:
            0 | 1 | 2
            3 | 4 | 5
            6 | 7 | 8
            """
            # All possible winning combinations (indices)
        wins = [
            [0, 1, 2],  # rows
            [3, 4, 5],
            [6, 7, 8],
            [0, 3, 6],  # columns
            [1, 4, 7],
            [2, 5, 8],
            [0, 4, 8],  # diagonals
            [2, 4, 6]
            ]

        for combo in wins:
            a, b, c = combo
            if board[a] == board[b] == board[c] != ' ':
                return True # Return 'X' or 'O'

        return False
    
    def det_winner(self,board):
            wins = [
                [0, 1, 2],  # rows
                [3, 4, 5],
                [6, 7, 8],
                [0, 3, 6],  # columns
                [1, 4, 7],
                [2, 5, 8],
                [0, 4, 8],  # diagonals
                [2, 4, 6]
                ]

            for combo in wins:
                a, b, c = combo
                if board[a] == board[b] == board[c] != ' ':
                    return board[a] # Return 'X' or 'O'

            
    def update_state_value(self, current_state, next_state, reward, alpha=0.1):
        current_idx = self.validstates.index(current_state)
        next_idx = self.validstates.index(next_state)
    
        # TD update: old_value + learning_rate * (reward + next_value - old_value)
        self.statevalues[current_idx] += alpha * (
        reward + self.statevalues[next_idx] - self.statevalues[current_idx]
        )
    
    def initializestatevalues(self):
      for i in range(len(self.boards)):
          if self.boards[i].count('X') < 6 and self.boards[i].count('O') < 6:
              self.validstates.append(self.boards[i])
              if self.check_winner(self.boards[i]):
                  self.statevalues.append(1)
              else:
                  self.statevalues.append(0.5)
                  
#   def updatestatevalues(self,boardcondition,winner):
        
    def currentstatevalues(self):
        return self.statevalues
        
                      

    def clearboard(self):
        self.board =[" " for _ in range(9)]

    # Print current state of the board
    def printboard(self):
        for i in range(0, 9, 3):
            if(i<9 and i >0):
                print('-' * 5)
            print(self.board[i], self.board[i+1], self.board[i+2])
        print("Above is the current board state")
    def updateboard(self, x, move):
        if x >= 1 and x <= 9 and self.board[x - 1] == ' ':
            self.board[x - 1] = move
            self.printboard()
            return 1
        else:
            print("Not a valid move! Please restart!")
            return -1
     
        
    
    def pickbest(self,board):
        maxval = 0
        # create a shallow copy so modifications to boardcopy
        # don't mutate the original self.board
        boardcopy = self.board.copy()
        #find available options:
        for i in range(len(boardcopy)):
            if boardcopy[i] == ' ':
                boardcopy[i] = 'O'
                try:
                    state_index = self.validstates.index(tuple(boardcopy))
                    curval = self.statevalues[state_index]
                    if curval >= maxval:
                        maxval = curval
                        best_move = i
                except ValueError:
                    pass
                boardcopy[i] = ' '
        return best_move + 1 if 'best_move' in locals() else 1          
                    
                    
        
    def print_initialstatevalues(self):
        for i in range(len(self.statevalues)):
            print(self.statevalues[i])
    #check if a game is over        
 #   def gameover():        
 #       if check_winner(board)==True:
 #           return True
 #       elif   
    
    # this finishes an entire game
#    def gameplay(playermove):
#        #check available options:
            

        
    #sdef update statevalues():
        
                
                   
                
     #Initialize crappy state values at the biginning            
 #   def initialize_statevalues():
        

if __name__ == "__main__":
    tictac = TicTacToe()
    tictac.initializestatevalues()
 #   sv = tictac.statevalues
 # vs = tictac.validstates
    movexo = []
    episodes = 1000
    # for i in range(1,episodes):  
    for i in range(1, episodes):
        print("Starting a new game")
        tictac.clearboard()
        movexo.clear()
        print("\n")
        prev_state = tictac.board.copy()
        while True:
            try:
                available = [n for n in range(1, 10) if n not in movexo]
                if available:
                    user_input = input("Please enter a number between 1 and 9: ")
                    number = int(user_input)
                    print(f"You entered: {number}")
                    ub = tictac.updateboard(number, 'X')
                    if ub == -1:
                        available.clear()
                        break
                    movexo.append(number)
                    available = [n for n in range(1, 10) if n not in movexo]
                    if tictac.check_winner(tictac.board):
                        i = i + 1
                        print("Winner is: ", tictac.det_winner(tictac.board))
                        # Final TD update for human win
                        tictac.update_state_value(tuple(prev_state), tuple(tictac.board), reward=-1)
                        available.clear()
                        break
                else:
                    print("It's a draw!")
                    # Final TD update for draw
                    tictac.update_state_value(tuple(prev_state), tuple(tictac.board), reward=0.5)
                    available.clear()
                    break
            except ValueError:
                print("Invalid input. Please enter a whole number.")
            # Computer move
            if available:
                prev_state = tictac.board.copy()
                chosen = tictac.pickbest(tictac.board)
                movexo.append(chosen)
                available = [n for n in range(1, 10) if n not in movexo]
                print("The computer randomly chosen ", chosen)
                ub = tictac.updateboard(chosen, 'O')
                # TD update after computer move (reward=0 for ongoing)
                tictac.update_state_value(tuple(prev_state), tuple(tictac.board), reward=0)
                if ub == -1:
                    available.clear()
                    break
                movexo.append(chosen)
                if tictac.check_winner(tictac.board):
                    i = i + 1
                    print("Winner is: ", tictac.det_winner(tictac.board))
                    # Final TD update for computer win
                    tictac.update_state_value(tuple(prev_state), tuple(tictac.board), reward=1)
                    available.clear()
                    break
            else:
                print("It's a draw!")
                # Final TD update for draw
                tictac.update_state_value(tuple(prev_state), tuple(tictac.board), reward=0.5)
                available.clear()
                break
    # tictac.makemove(2,2,'O')