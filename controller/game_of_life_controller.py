from PyQt5.QtWidgets import QColorDialog
import numpy as np
class GameOfLifeController:
    def __init__(self, model, view):
        self.model = model
        self.view = view

        # Connect signals and slots
        self.view.start_button.clicked.connect(self.start_game)
        self.view.stop_button.clicked.connect(self.stop_game)
        self.view.reset_button.clicked.connect(self.reset_game)
        self.view.clear_button.clicked.connect(self.clear_board)
        self.view.generate_button.clicked.connect(self.generate_board)
        self.view.color_button.clicked.connect(self.choose_color)

    def start_game(self):
        self.view.animation_timer.start(100)

    def stop_game(self):
        self.view.animation_timer.stop()

    def reset_game(self):
        self.stop_game()
        self.model.generation = 0
        self.model.initialize_board()
        self.view.draw_board()
        self.view.update_generation_label()

    def clear_board(self):
        self.stop_game()
        self.model.generation = 0
        self.model.board = np.zeros((self.model.rows, self.model.cols))
        self.view.draw_board()
        self.view.update_generation_label()

    def generate_board(self):
        self.stop_game()
        self.model.generation = 0
        self.model.initialize_board()
        self.view.draw_board()
        self.view.update_generation_label()

    def choose_color(self):
        color_dialog = QColorDialog(self.view)
        new_color = color_dialog.getColor()

        if new_color.isValid():
            self.view.live_cell_color = new_color.name()
            self.view.draw_board()


