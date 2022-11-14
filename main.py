import sys

from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QPixmap
import random
from PIL import Image, ImageDraw
from UI import Ui_MainWindow


class MyWidget(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.label.clicked.connect(self.update)

    def update(self) -> None:
        x, y = self.size().width(), self.size().height()
        x1, y1 = random.randint(1, x), random.randint(1, y)
        im = Image.new('RGB', (x, y), (255, 255, 255))
        draw = ImageDraw.Draw(im)
        a = random.randint(1, (x + y) / 4)
        draw.ellipse((x1, y1, x1 + a, y1 + a), fill='yellow', outline=(0, 0, 0))
        im.save('img.png')
        pixmap = QPixmap('img.png')
        self.label.setPixmap(pixmap)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())
