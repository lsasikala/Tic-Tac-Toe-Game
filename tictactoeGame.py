import sys
import os 
import random

"""
Firstname: Lavanya
Lastname: Sasikala
Username: lsasikala
StudentID: 156621211
Email: lsasikala@senecacollege.ca
"""

# This is my TicTacToe Class 
class TicTacToe:
    # Declare class variables 
    # players is a list of players (this game will have 2 players)
    # Winninggames is a list of all winning possibilities 
    # Player1entry is a list of entries of first players 
    # Player2 entry is a list of entries of second player 
    players = []
    winninggames = [[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0]] #This is just sample 
    player1entry = []
    player2entry = []
    board = [1,2,3,4,5,6,7,8,9] #Based on infromation given in the Final Exam Problem Statement

    # This is a constructor 
    """
    This is a constructor that prints an initialization statement
    Then call the getplayernames method to get the names and configure the list of players 
    Also call the printboard method to print the board, since this is a constructor the printboard is called first time here 
    Therefore printboard in this constructor will print initial brand new board ready to be played.
    """
    def __init__(self) -> None:
        print ("Initializing a 3X3 TicTacToe")          #Printing game initialization message
        self.getplayernames()                           #Calling the getplayer function to get the name of the players.
        self.printboard()                               #Calling the printboardgame function to print the initial status of the board.
        
        
    """
    This is getplayernames method 
    This method asks user to enter the name of the player 1 and 2 one by one and append the names to the players class variable
    """
    def getplayernames(self): 
        player1 = input("What is the name of the player 1: ")           #Prompting the user for the name of player1
        self.players.append(player1)                                    #Appending player1's name to the players list
        player2 = input("What is the name of the player 2: ")           #Prompting the user for the name of player1
        self.players.append(player2)                                    #Appending player1's name to the players list
        
        
    """
    This is a printboard method 
    This method prints current state of the board 
    """
    def printboard(self):
        print(f"|{self.board[0]}|{self.board[1]}|{self.board[2]}|")     #Printing the first row of the board
        print(f"|{self.board[3]}|{self.board[4]}|{self.board[5]}|")     #Printing the second row of the board
        print(f"|{self.board[6]}|{self.board[7]}|{self.board[8]}|")     #Printing the third row of the board

        
   
    """
    This method gets all available numbers to be played at the time this method is called 
    It returns these available numbers 
    :return availablenumbers 
    """
    def getavailablenumbers(self):              
        availablenumbers = []                                           #Initializing a list of availablenumbers 
        for entry in range(len(self.board)):                            #Checking each entry in the board
            if self.board[entry] != 'X' and self.board[entry] != 'O':   #If an entry is not equal to X and O....., 
                availablenumbers.append(self.board[entry])              #.....append the entry to the availablenumbers.
        return availablenumbers                                         # return the list of availablenumbers

        
  
    """
    This function goes through all the winning games and compare them against the each individual players entries
    By comparing the entries against winning game this method identifies the winner if there is one 
    If there is a winner this method returns the winner otherwise return None
    """
    def getwinner(self):
        for i in range (len(self.winninggames)):                    # For each entry in winninggames....
            if(self.winninggames[i].count(1) == 3 ):                #...checking if the entry corresponds to player1 who played X...
                return self.players[0]                              #...if the entry matches, return player1 as the winner
            elif (self.winninggames[i].count(2) == 3 ):             #...checking if the entry corresponds to player1 who played X...
                return self.players[1]                              #......if the entry matches, return player1 as the winner
        return None                                                 #if no match, return None
            
    


    """
    This is rungame method 
    This method continue to run a loop asking the user to enter the number to play and shows the available numbers as well
    If the user enter something otherthan the available number the prompt will continue to ask the same user to enter the correct values 
    This method assembles all the relevant method we have together, so that 
    First player one is asked to enter the number and then the second and then the first and it keep alternates 
    Until one player wins or the game finishes where there is no further numbers to enter. 
    Ultimately, if there is a winner it prints the winner. If ther eis no winner it prints No Winner. 
    """
    def rungame(self): 
        currentplayer = 0               #currentplayer set to 0 to represent player 1
        winner = None                   #winner set to 0
        while winner is None:           
            availablenumbers=self.getavailablenumbers()     #Calling the getavailablenumbers() to get the available slots in the board
            availablenumbers_str = ",".join(map(str, availablenumbers))   # Converting the list of available numbers to comma seperated strings for printing purpose 
            if not availablenumbers:             #If the list of available numbers is null, then the game ends... 
                print("No one win!")               #...with the message No one win!... 
                print("End of the game")            #...and End of the game....
                break
                
            if currentplayer == 0:              #If currentplayer = 0 which represent player1 then symmbol is X
                symbol = 'X'                    
            else:                               #For player2 symbol is O
                symbol = 'O'

            entry = input(f"{self.players[currentplayer]} Enter the number to play your symbol {symbol} (Available Numbers {availablenumbers_str}): ")  #Prompting player1 for selecting the availablenumber for the entry

            while True:                     # Keep asking the player untill a valid number is entered from the available numbers.
                if not entry.isdigit() or int(entry) >  max(availablenumbers): # If the input entered is not a digit or a number greater than the maximum of the number in the available list
                    print ("Enter available Number")        #Print the message for entering a number from the available numbers and again prompting for the input
                    entry = input(f"{self.players[currentplayer]} Enter the number to play your symbol {symbol} (Available Numbers {availablenumbers_str}): ")
                
                elif int(entry) not in availablenumbers :        #If the input is a number that is already chosen then print the message and again prompt for a valid input
                    print (f"Number already played, choose a different number from available numbers. (Available Numbers %s) {availablenumbers_str}")
                    entry = input(f"{self.players[currentplayer]} Enter the number to play your symbol {symbol} (Available Numbers {availablenumbers_str}): ")                   
            
                else:             # if valid input, exit fom while loop
                    break

            entry = int(entry)    # Converting entry (input) to integer
            self.board[entry-1]= symbol   # The corresonding position in the board is updated with the symbol
            row = (entry-1) // 3           #Calculating the corresponding position  to update the winninggames 2D list with number 1 or 2 to represent the player number
            column = (entry-1) % 3
            self.winninggames[row][column] = currentplayer + 1    #The winninggame postion is updated with 1 or 2 to represent the respective players
            if row == column:
                self.winninggames[6][row]= currentplayer + 1     #Checking for diagonal condition...
            if row + column == 2:
                self.winninggames[7][row]= currentplayer + 1       #Checking for diagonal condition...
            winner = self.getwinner()                       #Calling the getwinner function to check whether the winninggame 2D list has any entry with all 1's or 2's
            if winner is not None:
                print ("Player " + winner + " is the winner")   #Declaring the winner
            else:
                self.printboard()                       # If not a winning condition, calling printboard() to print the current sttae of the board
            
                   
           
                currentplayer = 1- currentplayer        #Updating the current player
        
                 
        
                



        

# My main method to test this code locally
if __name__ == "__main__":
    game = TicTacToe()
    game.rungame()
