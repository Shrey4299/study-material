from abc import ABC


# Enums for Piece Type
class PieceType:
    X = "X"
    O = "O"


# Base Class for PlayingPiece
class PlayingPiece(ABC):
    def __init__(self, piece_type):
        self.piece_type = piece_type


# PlayingPieceX Class
class PlayingPieceX(PlayingPiece):
    def __init__(self):
        super().__init__(PieceType.X)


# PlayingPieceO Class
class PlayingPieceO(PlayingPiece):
    def __init__(self):
        super().__init__(PieceType.O)


# Player Class
class Player:
    def __init__(self, name, playing_piece):
        self.name = name
        self.playing_piece = playing_piece


# Board Class
class Board:
    def __init__(self, size):
        self.size = size
        self.board = [[None for _ in range(size)] for _ in range(size)]

    def add_piece(self, row, column, playing_piece):
        if self.board[row][column] is not None:
            return False
        self.board[row][column] = playing_piece
        return True

    def get_free_cells(self):
        free_cells = []
        for i in range(self.size):
            for j in range(self.size):
                if self.board[i][j] is None:
                    free_cells.append((i, j))
        return free_cells

    def print_board(self):
        for i in range(self.size):
            row = []
            for j in range(self.size):
                if self.board[i][j]:
                    row.append(self.board[i][j].piece_type)
                else:
                    row.append(" ")
            print(" | ".join(row))
            print("-" * (self.size * 4 - 3))


# Game Class
class TicTacToeGame:
    def __init__(self):
        self.players = []
        self.game_board = None

    def initialize_game(self):
        # Create two players
        self.players.append(Player("Player1", PlayingPieceX()))
        self.players.append(Player("Player2", PlayingPieceO()))
        # Initialize a 3x3 board
        self.game_board = Board(3)

    def start_game(self):
        no_winner = True

        while no_winner:
            # Get current player and re-add to the queue
            player_turn = self.players.pop(0)

            # Display the current board
            self.game_board.print_board()
            free_spaces = self.game_board.get_free_cells()

            if not free_spaces:
                print("It's a Tie!")
                return "Tie"

            # Read user input for the move
            print(f"Player {player_turn.name} ({player_turn.playing_piece.piece_type}), enter row,column (0-based): ")
            row, col = map(int, input().split(","))

            # Place the piece if valid
            if not self.game_board.add_piece(row, col, player_turn.playing_piece):
                print("Invalid move! Try again.")
                self.players.insert(0, player_turn)
                continue

            # Add player back to queue
            self.players.append(player_turn)

            # Check for winner
            if self.is_there_winner(row, col, player_turn.playing_piece.piece_type):
                self.game_board.print_board()
                print(f"Player {player_turn.name} wins!")
                return player_turn.name

        return "Tie"

    def is_there_winner(self, row, col, piece_type):
        size = self.game_board.size

        # Check row
        if all(self.game_board.board[row][i] and self.game_board.board[row][i].piece_type == piece_type for i in range(size)):
            return True

        # Check column
        if all(self.game_board.board[i][col] and self.game_board.board[i][col].piece_type == piece_type for i in range(size)):
            return True

        # Check main diagonal
        if row == col and all(self.game_board.board[i][i] and self.game_board.board[i][i].piece_type == piece_type for i in range(size)):
            return True

        # Check anti-diagonal
        if row + col == size - 1 and all(self.game_board.board[i][size - 1 - i] and self.game_board.board[i][size - 1 - i].piece_type == piece_type for i in range(size)):
            return True

        return False


# Main function to run the game
if __name__ == "__main__":
    game = TicTacToeGame()
    game.initialize_game()
    winner = game.start_game()
    print(f"Game Over. Result: {winner}")
