import sys
import csv
from random import choice
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QMainWindow, QLabel, QTableWidgetItem, QInputDialog
from Main import Ui_MainWindow as Ui_MainWindow
from PROJECT2 import Ui_MainWindow as Ui_Session


with open('stress.csv', encoding='windows-1251') as csvfile:
    reader = csv.reader(csvfile, delimiter=';', quotechar='"')
    words = [(i[0], i[1]) for i in reader]


class MainForm(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.start_training_btn.clicked.connect(self.open_project)
        self.about_box_btn.clicked.connect(self.open_about_box)

    def open_session(self):
        self.session_form = SessionForm()
        self.session_form.show()

    def open_about_box(self):
        if self.about_box_btn.text() == 'О программе':
            self.about_box_btn.setText('by VKRLV')
        else:
            self.about_box_btn.setText('О программе')


class SessionForm(QMainWindow, Ui_Session):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.answer_btn.clicked.connect(self.true_or_false_counter)
        self.finish_btn.clicked.connect(self.finish)
        self.true_ans = 0
        self.false_ans = 0
        self.random_word_to_check()

    def random_word_to_check(self):
        self.word = choice(words)
        self.question_lbl.setText(self.word[1])

    def true_or_false_counter(self):
        self.error_lbl.clear()
        if self.answer_field.text() == '':
            self.error_lbl.setText('Введите Ваш ответ в поле!!!')
        elif self.answer_field.text() == self.word[0]:
            self.true_ans += 1
            self.random_word_to_check()
            self.answer_field.clear()
        else:
            self.false_ans += 1
            self.error_lbl.setText(f'Правильный ответ: {self.word[0]}')
            self.random_word_to_check()

        self.true_counter.setText(f'ПРАВИЛЬНЫХ ОТВЕТОВ: {self.true_ans}')
        self.false_counter.setText(f'НЕПРАВИЛЬНЫХ ОТВЕТОВ: {self.false_ans}')

    def finish(self):
        self.close()
        self.destroy()



if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MainForm()
    ex.show()
    sys.exit(app.exec())