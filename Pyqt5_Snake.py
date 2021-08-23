# __Author__ __Lencof__
# Pyqt5_Snake.py

from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
import random

class SnakeGame(QMainWindow):
    def __init__(self):
        super(SnakeGame, self).__init__()
        self.sboard = Board(self)

        self.statusbar = self.statusBar()
        self.sboard.msg2statusbar[str].connect(self.statusbar.showMessage)

        self.setCentralWidget(self.sboard)
        self.setWindowTitle('Snake game')
        self.resize(600, 400)
        screen = QDesktopWidget().screenGeometry()
        size = self.geometry()
        self.move((screen.width()-size.width())/2, (screen.height()-size.height())/2)

        self.sboard.start()
        self.show()

class Board(QFrame):
    msg2statusbar = pyqtSignal(str)
    SPEED = 70 
    WIDTHINBLOCKS = 60 
    HEIGHTINBLOCKS = 30 

    def __init__(self, parent):
        super(Board, self).__init__(parent)
        self.timer = QBasicTimer()
        self.snake = [[5, 10], [5, 11]]
        self.current_x_head = self.snake[0][0]
        self.current_y_head = self.snake[0][1]
        self.food = []
        self.grow_snake = False
        self.board = []
        self.direction = 1
        self.drop_food()
        self.setFocusPolicy(Qt.StrongFocus)

    def square_width(self):
        return self.contentsRect().width() / Board.WIDTHINBLOCKS

    def square_height(self):
        return self.contentsRect().height() / Board.HEIGHTINBLOCKS

    def start(self):
        self.msg2statusbar.emit(str(len(self.snake) - 2))
        self.timer.start(Board.SPEED, self)

    def paintEvent(self, event):
        painter = QPainter(self)
        rect = self.contentsRect()
        boardtop = rect.bottom() - Board.HEIGHTINBLOCKS * self.square_height()

        for pos in self.snake:
            self.draw_square(painter, rect.left() + pos[0] * self.square_width(),
                             boardtop + pos[1] * self.square_height())
        for pos in self.food:
            self.draw_square(painter, rect.left() + pos[0] * self.square_width(),
                             boardtop + pos[1] * self.square_height())

    def draw_square(self, painter, x, y):
        color = QColor(0xCC66CC)
        painter.fillRect(x + 1, y + 1, self.square_width() - 2,
                         self.square_height() - 2, color)

    def keyPressEvent(self, event):
        key = event.key()
        if key == Qt.Key_Left:
            if self.direction != 2:
                self.direction = 1
        elif key == Qt.Key_Right:
            if self.direction != 1:
                self.direction = 2
        elif key == Qt.Key_Down:
            if self.direction != 4:
                self.direction = 3
        elif key == Qt.Key_Up:
            if self.direction != 3:
                self.direction = 4

    def move_snake(self):
        if self.direction == 1:
            self.current_x_head, self.current_y_head = self.current_x_head - 1, self.current_y_head
            if self.current_x_head < 0:
                self.current_x_head = Board.WIDTHINBLOCKS - 1
        if self.direction == 2:
            self.current_x_head, self.current_y_head = self.current_x_head + 1, self.current_y_head
            if self.current_x_head == Board.WIDTHINBLOCKS:
                self.current_x_head = 0
        if self.direction == 3:
            self.current_x_head, self.current_y_head = self.current_x_head, self.current_y_head + 1
            if self.current_y_head == Board.HEIGHTINBLOCKS:
                self.current_y_head = 0
        if self.direction == 4:
            self.current_x_head, self.current_y_head = self.current_x_head, self.current_y_head - 1
            if self.current_y_head < 0:
                self.current_y_head = Board.HEIGHTINBLOCKS

        head = [self.current_x_head, self.current_y_head]
        self.snake.insert(0, head)
        if not self.grow_snake:
            self.snake.pop()
        else:
            self.msg2statusbar.emit(str(len(self.snake)-2))
            self.grow_snake = False

    def timerEvent(self, event):
        if event.timerId() == self.timer.timerId():
            self.move_snake()
            self.is_food_collision()
            self.is_suicide()
            self.update()

    def is_suicide(self):  # If snake collides with itself, game is over
        for i in range(1, len(self.snake)):
            if self.snake[i] == self.snake[0]:
                self.msg2statusbar.emit(str("TRUP"))
                self.snake = [[x, y] for x in range(0, 61) for y in range(0, 41)]
                self.timer.stop()
                self.update()

    def is_food_collision(self):
        for pos in self.food:
            if pos == self.snake[0]:
                self.food.remove(pos)
                self.drop_food()
                self.grow_snake = True

               
    def drop_food(self):
        x = random.randint(3, 58)
        y = random.randint(3, 38)
        for pos in self.snake:  # Do not drop food on snake
            if pos == [x, y]:
                self.drop_food()
        self.food.append([x, y])

# create def main():
def main():
    app = QApplication([])
    launch_game = SnakeGame()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main() 
