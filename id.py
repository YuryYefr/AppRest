from PyQt5.QtWidgets import (QWidget, QPushButton, QLineEdit,
                             QInputDialog)


class AgentName(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.btn = QPushButton('Dialog', self)
        self.btn.move(20, 20)
        self.btn.clicked.connect(self.define_user)

        self.le = QLineEdit(self)
        self.le.move(130, 22)

        self.setGeometry(300, 300, 290, 150)
        self.setWindowTitle('you should not see this')
        self.show()

    def define_user(self):
        text, ok = QInputDialog.getText(self, 'name_surname',
                                        'Type here:',)

        if ok:
            self.le.setText(str(text))

        return text
