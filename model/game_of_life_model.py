import numpy as np

class GameOfLifeModel:
    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        self.board = np.zeros((rows, cols))
        self.generation = 0

    def initialize_board(self):
        self.board = np.random.choice([0, 1], size=(self.rows, self.cols), p=[0.7, 0.3])

    def update_board(self):
        new_board = self.update(self.board)
        self.board[:, :] = new_board[:, :]
        self.generation += 1

    def update(self, board):
        new_board = board.copy()

        for i in range(board.shape[0]):
            for j in range(board.shape[1]):
                neighbors = board[max(0, i - 1):min(board.shape[0], i + 2), max(0, j - 1):min(board.shape[1], j + 2)]
                live_neighbors = np.sum(neighbors) - board[i, j]

                if board[i, j] == 1:
                    if live_neighbors < 2 or live_neighbors > 3:
                        new_board[i, j] = 0
                else:
                    if live_neighbors == 3:
                        new_board[i, j] = 1

        return new_board
