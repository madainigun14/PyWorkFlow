import os
import sys
from PyQt5.QtWidgets import QApplication
from PyQt5.QtSvg import QSvgWidget


class AnimatedSvgExample(QSvgWidget):
    def __init__(self):
        super().__init__()
        self.__initUi()

    def __initUi(self):
        r = self.renderer()
        r.setFramesPerSecond(60)
        ico_filename = os.path.join(os.path.dirname(__file__), 'ico/rolling.svg')
        r.load(ico_filename)


def run():
    app = QApplication(sys.argv)
    mainWindow = AnimatedSvgExample()

    mainWindow.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    try:
        run()
    except Exception as e:
        print("!!!!!!!!!!!!!!!!!!!!!!!!!!!")
        print(str(e))
    finally:
        pass