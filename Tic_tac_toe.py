"""
Game Logic:
1- run program.
2- main manu.
3- game start, quit game.
4- Player1 (name, symbol), Player2 (name, symbol).
5- board display.
6- game loops until win or draw.
7- restart game, quit game.

"""
import os

#this function to clear screen,

def clear_screen():
    os.system("cls" if os.name == "nt" else "clear" )
class Player:

    def __init__(self): 
        self.name = ""
        self.symbol = ""

    def choose_name(self):
        while True:
            name = input("Enter your name (only letters): ")
            if name.isalpha():
                self.name = name
                break
            else:
                print("Please enter only letter")


    def choose_symbol(self):
        while True:
            symbol = input(f"Hello! {self.name} Choose one symbol to play (X or O): ")
            if symbol.isalpha() and len(symbol) == 1:
                self.symbol = symbol.upper()
                break
            print("Invalid symbol. Please choose one symbol. ")

class Menu:

    def disply_main_menu(self):
        print("Welcome to X_O game!")
        print("1. Start Game: ")
        print("2. Quit Game: ")
        while True:
            choice = input("Enter your choice(1 or 2): ")
            if choice.isdigit() and len(choice) == 1:
                return choice
                break
            print("Invalid input. Please enter 1 or 2")
    

    def disply_endgame_manu(self):
        menu_txt = """
        Game Over!
        1. Restart Game.
        2. Quit Game.
        Enter your choice (1 or 2).
        """
        while True:
            choice = input(menu_txt)
            if choice.isdigit() and len(choice) == 1:
                return choice
                break
            print("Invalid input. Please enter 1 or 2")


class Board:

    def __init__(self):
        self.board = [str(i) for i in range(1,10)] #["1","2",....,"9"]

    def display_board(self):
        for i in range(0, 9 , 3): #(start, stop, step)
            print("|".join(self.board[i:i+3]))
            if i < 6:
                print("-"*5)


    def update_board(self, choice, symbol):
        #this method update the user choice based on the number presented in the displayed board
        if self.is_valide(choice):
            self.board[choice -1] = symbol
            return True
        return False
    def is_valide(self, choice):
        #this method check is the position is not occupied
        return self.board[choice -1].isdigit() 


    def reset_board(self):
        self.board = [str(i) for i in range(1, 10)]


#this class is where the game start. it compile all the class in this class
class Game:

    def __init__(self):
        self.Players = [Player(), Player()]
        self.Board = Board()
        self.Menu = Menu()
        self.current_player_index = 0

    def start_game(self):
        choice = self.Menu.disply_main_menu()
        if choice == "1":
            self.setup_players()
            self.play_game()

        else:
            self.quit_game()


    def setup_players(self):
        #loop through the two players
        for number, ply in enumerate(self.Players, start=1):
            print(f"Player {number} Please enter your details: ")
            ply.choose_name()
            ply.choose_symbol()
            print("-"*20)
            #clear_screen()


    def play_game(self):
        while True:
            self.play_turn()
            if self.check_win() or self.check_draw():
                choice = self.Menu.disply_endgame_manu()
                if choice == "1":
                    self.restart_game()
                else:
                    self.quit_game()
                    break


    def play_turn(self):
        player = self.Players[self.current_player_index]
        self.Board.display_board()
        print(f"{player.name}'s turn({player.symbol})")
        #while loop to check the validation of the input
        while True:
            try:
                cell_choice = int(input("Choice a cell: "))
                if 1<= cell_choice <=9 and self.Board.update_board(cell_choice, player.symbol):
                    break
                else:
                    print("Invalid Move. try again.")
            except ValueError:
                print("Please choice a number between 1-9")
        self.switch_palyer()


    def switch_palyer(self):
        
        self.current_player_index = 1 - self.current_player_index

    def check_win(self):
        wining_combination = [
            [0,1,2], [3,4,5], [6,7,8], #rows
            [0,3,6], [1,4,7], [2,5,8], #column
            [0,4,8], [2,4,6]          #diagonal
        ]
      
        for como in wining_combination:
            if self.Board.board[como[0]] == self.Board.board[como[1]] == self.Board.board[como[2]]:
                print("Congrats! You win!.")
                return True
        return False

    def check_draw(self):
        #check if all the cells in board object is not digits
        return all(not cell.isdigit() for cell in self.Board.board)

    def restart_game(self):
        self.Board.reset_board()
        self.current_player_index = 0
        self.play_game()


    def quit_game(self):
        print("Thank you for playing.")


obj = Game()
obj.start_game()
