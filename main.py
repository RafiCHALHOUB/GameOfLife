import sys
from PyQt5.QtWidgets import QApplication
from model.game_of_life_model import GameOfLifeModel
from view.game_of_life_view import GameOfLifeView
from controller.game_of_life_controller import GameOfLifeController

if __name__ == "__main__":
    app = QApplication(sys.argv)
    model = GameOfLifeModel(rows=30, cols=30)
    view = GameOfLifeView(model)
    controller = GameOfLifeController(model, view)

    view.show()
    sys.exit(app.exec_())
