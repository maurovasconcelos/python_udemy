import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QGridLayout
from PyQt5.QtWidgets import QPushButton, QLineEdit, QSizePolicy


class Calculadora(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle('Calculadora do Mauro')  # seta nome do titulo
        self.setFixedSize(400, 400)  # seta tamanho da janela
        self.cw = QWidget()
        self.grid = QGridLayout(self.cw)

        self.display = QLineEdit()
        self.grid.addWidget(self.display, 0, 0, 1, 5)  # criando display
        self.display.setDisabled(True)
        self.display.setStyleSheet(
            '* {background: #FFF; color: #000; font-size: 30px;}'
        )

        # Comando pra expandir a barra de calculos/
        # não se assustar, vai sendo empurrada pra cima com implementação de botoes
        self.display.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)

        self.add_bnt(QPushButton('7'), 1, 0, 1, 1)
        self.add_bnt(QPushButton('8'), 1, 1, 1, 1)
        self.add_bnt(QPushButton('9'), 1, 2, 1, 1)
        self.add_bnt(QPushButton('-'), 1, 3, 1, 1)
        self.add_bnt(
            QPushButton('C'), 1, 4, 1, 1,
            lambda: self.display.setText(''),
            'background: #d5580d; color: #fff; font-weight: 700'
        )

        self.add_bnt(QPushButton('4'), 2, 0, 1, 1)
        self.add_bnt(QPushButton('5'), 2, 1, 1, 1)
        self.add_bnt(QPushButton('6'), 2, 2, 1, 1)
        self.add_bnt(QPushButton('+'), 2, 3, 1, 1)
        self.add_bnt(
            QPushButton('<-'), 2, 4, 1, 1,
            lambda: self.display.setText(
                self.display.text()[:-1]
            ),
            'background: #13823a; color: #fff; font-weight: 700'
        )

        self.add_bnt(QPushButton('1'), 3, 0, 1, 1)
        self.add_bnt(QPushButton('2'), 3, 1, 1, 1)
        self.add_bnt(QPushButton('3'), 3, 2, 1, 1)
        self.add_bnt(QPushButton('/'), 3, 3, 1, 1)
        self.add_bnt(QPushButton(''), 3, 4, 1, 1)

        self.add_bnt(QPushButton('.'), 4, 0, 1, 1)
        self.add_bnt(QPushButton('0'), 4, 1, 1, 1)
        self.add_bnt(QPushButton(''), 4, 2, 1, 1)
        self.add_bnt(QPushButton('*'), 4, 3, 1, 1)
        self.add_bnt(
            QPushButton('='), 4, 4, 1, 1,
            self.eval_igual,
            'background: #095177; color: #fff; font-weight: 700'
        )

        self.setCentralWidget(self.cw)

    def add_bnt(self, btn, row, col, rowspan, colspan, funcao=None, style=None):
        self.grid.addWidget(btn, row, col, rowspan, colspan)

        if not funcao:
            btn.clicked.connect(
                lambda: self.display.setText(
                    self.display.text() + btn.text()
                )
            )
        else:
            btn.clicked.connect(funcao)

        if style:
            btn.setStyleSheet(style)

        btn.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)

    def eval_igual(self):
        try:
            self.display.setText(
                str(eval(self.display.text()))
            )
        except Exception as e:
            self.display.setText('Conta invalida!')

if __name__ == '__main__':
    qt = QApplication(sys.argv)
    calc = Calculadora()
    calc.show()
    qt.exec_()
