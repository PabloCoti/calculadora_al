from PyQt5 import uic  # Lanza error, pero es por el pycharm, no porque no funcione
from PyQt5.QtWidgets import QMainWindow, QFileDialog
import utils

class MainView(QMainWindow):
    def __init__(self):
        super().__init__()

        # Cargar archivo .ui
        uic.loadUi("views/designs/main_view.ui", self)

        # Mostrar interfaz
        self.show()

        # Default actions
        self.frame_matrices_matrizc.hide()
        self.frame_matrices_matrizd.hide()
        self.frame_matrices_matrizb.hide()

        # User interactions
        self.pushButton_calcular.clicked.connect(self.calculate_result)
        self.spinBox_matrices_numeromatrices.valueChanged.connect(self.increase_shown_matrix)
        self.spinBox_matrices_numeromatrices.valueChanged.connect(self.increase_hidden_matrix)
        self.pushButton_matrices_calcular.clicked.connect(self.calculate_matrix_result)

    def calculate_matrix_result(self):
        a = utils.matrix_convertion(self.textEdit_ma.toPlainText())

        if self.frame_matrices_matrizb.isVisible():
            b = utils.matrix_convertion(self.textEdit_mb.toPlainText())

            operand = self.comboBox_matrix_ab_op.currentText()

            if operand == '*':
                m_result = utils.matrix_mult(a, b)

                self.update_matrix_results(m_result)

            elif operand == '+':
                m_result = utils.matrix_sum(a, b)

                self.update_matrix_results(m_result)

            elif operand == '-':
                m_result = utils.matrix_sub(a, b)

                self.update_matrix_results(m_result)

        if self.comboBox_matrix_a_op.isVisible():
            opt = self.comboBox_matrix_a_op.currentText()

            if opt == 'Traspuesta':
                m_result = utils.matrix_traspose(a)

                self.update_matrix_results(m_result)

            elif opt == 'Inversa':
                m_result = utils.matrix_invert(a)

                self.update_matrix_results(m_result)

            elif opt == 'Determinante':
                m_result = utils.matrix_determinant(a)

                self.update_matrix_results(m_result)

    def update_matrix_results(self, m_result):
        result = ''
        if isinstance(m_result, list):
            for r in m_result:
                for n in r:
                    result += f"{n}   "
                result += '\n'

            self.textBrowser_matrix_result.setText(result)

        else:
            self.textBrowser_matrix_result.setText(str(m_result))

    def increase_shown_matrix(self, value):
        if value == 2:
            self.frame_matrices_matrizb.show()
            self.comboBox_matrix_a_op.hide()

        elif value == 3:
            self.frame_matrices_matrizc.show()

        elif value == 4:
            self.frame_matrices_matrizd.show()

    def increase_hidden_matrix(self, value):
        if value == 1:
            self.frame_matrices_matrizb.hide()
            self.comboBox_matrix_a_op.show()

        elif value == 2:
            self.frame_matrices_matrizc.hide()

        elif value == 3:
            self.frame_matrices_matrizd.hide()

    def calculate_result(self):
        op_string = self.textEdit_input.toPlainText()

        if 'i' in op_string:
            result = utils.compound_parse(op_string)
            answer = f"{op_string} = {result}"

            self.update_results(answer)

        else:
            result = utils.equation_parse(op_string)
            answer = f"{op_string} \n=\n {result}"

            self.update_results(answer)

    def update_results(self, string):
        self.textBrowser_result.append(string)
