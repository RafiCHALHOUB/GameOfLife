from PyQt5.QtWidgets import QMainWindow, QFrame, QVBoxLayout, QPushButton, QLabel
from PyQt5.QtCore import QTimer, Qt
import matplotlib.pyplot as plt
import matplotlib.backends.backend_qt5agg as plt_backend
from controller.game_of_life_controller import GameOfLifeController
class GameOfLifeView(QMainWindow):
    def __init__(self, model):
        super().__init__()

        self.model = model
        self.live_cell_color = "red"
        self.drawing = False  # Added attribute to track drawing state
        self.controller=GameOfLifeController
        self.setup_ui()
        self.model.initialize_board()
        self.draw_board()

    def setup_ui(self):
        self.central_widget = QFrame()
        self.setCentralWidget(self.central_widget)

        self.layout = QVBoxLayout(self.central_widget)

        self.start_button = QPushButton("Start", self)
        self.stop_button = QPushButton("Stop", self)
        self.reset_button = QPushButton("Reset", self)
        self.clear_button = QPushButton("Clear", self)
        self.generate_button = QPushButton("Generate", self)
        self.color_button = QPushButton("Choose Color", self)

        self.generation_label = QLabel("Generation: 0", self)

        self.canvas = plt_backend.FigureCanvasQTAgg(plt.Figure())
        self.ax = self.canvas.figure.add_subplot(111)  # Create ax as a class attribute

        self.layout.addWidget(self.start_button)
        self.layout.addWidget(self.stop_button)
        self.layout.addWidget(self.reset_button)
        self.layout.addWidget(self.clear_button)
        self.layout.addWidget(self.generate_button)
        self.layout.addWidget(self.color_button)
        self.layout.addWidget(self.generation_label)
        self.layout.addWidget(self.canvas)

        self.animation_timer = QTimer(self)
        self.animation_timer.timeout.connect(self.update_board)



    def draw_board(self):
        self.ax.clear()

        for i in range(self.model.rows + 1):
            self.ax.axhline(-i, color='gray', linewidth=0.5, linestyle='--')
        for j in range(self.model.cols + 1):
            self.ax.axvline(j, color='gray', linewidth=0.5, linestyle='--')

        for i in range(self.model.rows):
            for j in range(self.model.cols):
                color = self.live_cell_color if self.model.board[i, j] == 1 else "white"
                self.ax.add_patch(plt.Rectangle((j, -i-1), 1, 1, fill=True, color=color, edgecolor='gray'))

        self.ax.set_xlim(0, self.model.cols)
        self.ax.set_ylim(-self.model.rows, 0)
        self.ax.axis("off")

        self.canvas.draw()

    def update_board(self):
        self.model.update_board()
        self.draw_board()
        self.update_generation_label()

    def update_generation_label(self):
        self.generation_label.setText(f"Generation: {self.model.generation}")



