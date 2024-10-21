from PySide6.QtWidgets import QMainWindow


class Window(QMainWindow):
    def __init__(self, title: str) -> None:
        super().__init__()
        self.setWindowTitle(title)
        self.setMinimumSize(300, 300)
        self.show()
