import sys
import os
import pickle
from math import sqrt
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtWidgets import QWidget, QPushButton, QApplication, QLabel, QLineEdit, QDialog, QFileDialog
from PyQt5.QtCore import QCoreApplication
from PyQt5.QtGui import QPalette
from PyQt5.QtCore import Qt

class Example(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # ------------------------------------------------------------------------
        self.setGeometry(10, 45, 535, 680)
        self.setWindowTitle('Calculator')
        self.setWindowIcon(QIcon('web.png'))

        self.label = QLabel(self)
        self.label.setText("Введите значения данные в задаче:")
        self.label.move(10, 10)
        # ------------------------------------------------------------------------
        self.btn = QPushButton('Рассчитать', self)
        self.btn.setToolTip('Нажмите для произведения расчетов')
        self.btn.resize(self.btn.sizeHint())
        self.btn.move(10, 350)
        self.btn.clicked.connect(self.logicCalculations)
        # ------------------------------------------------------------------------
        self.btn_Image = QPushButton('Задача', self)
        self.btn_Image.setToolTip('Нажмите для загрузки условия и чертежа')
        self.btn_Image.resize(self.btn.sizeHint())
        self.btn_Image.move(100, 350)
        self.btn_Image.clicked.connect(self.openSecondForm)
        # ------------------------------------------------------------------------
        self.quit_btn = QPushButton('Выход', self)
        self.quit_btn.setToolTip('Нажмите для выхода из калькулятора')
        self.quit_btn.resize(self.quit_btn.sizeHint())
        self.quit_btn.move(190, 350)
        self.quit_btn.clicked.connect(QCoreApplication.instance().quit)
        # ------------------------------------------------------------------------
        self.btn_Image = QPushButton('Бетон', self)
        self.btn_Image.setToolTip('Нажмите для вывода таблицы классов бетона')
        self.btn_Image.resize(self.btn.sizeHint())
        self.btn_Image.move(280, 350)
        self.btn_Image.clicked.connect(self.openThirdForm)
        # ------------------------------------------------------------------------
        self.btn_Image = QPushButton('Арматура', self)
        self.btn_Image.setToolTip('Нажмите для вывода таблицы классов арматуры')
        self.btn_Image.resize(self.btn.sizeHint())
        self.btn_Image.move(370, 350)
        self.btn_Image.clicked.connect(self.openFourthForm)
        # ------------------------------------------------------------------------
        self.btn_save = QPushButton('Сохранить', self)
        self.btn_save.setToolTip('Нажмите для сохранения расчетов')
        self.btn_save.resize(self.btn.sizeHint())
        self.btn_save.move(460, 350)
        self.btn_save.clicked.connect(self.SaveLogic)
        # ------------------------------------------------------------------------
        self.btn_load = QPushButton('Загрузить', self)
        self.btn_load.setToolTip('Нажмите для загрузки последних расчетов')
        self.btn_load.resize(self.btn.sizeHint())
        self.btn_load.move(460, 380)
        self.btn_load.clicked.connect(self.LoadLogic)
        # ------------------------------------------------------------------------
        self.name_slope = QLabel(self)  # уклон прогона кровли
        self.name_slope.setText("Введите уклон прогона кровли:")
        self.name_slope.move(10, 35)
        self.input_slope = QLineEdit("4", self)
        self.input_slope.move(175, 35)
        # ------------------------------------------------------------------------
        self.R_b = QLabel(self)  # R_b
        self.R_b.setText("Введите R_b тяжелого бетона данного класса:")
        self.R_b.move(10, 60)
        self.input_R_b = QLineEdit("14.5", self)
        self.input_R_b.move(260, 60)
        # ------------------------------------------------------------------------
        self.R_s = QLabel(self)  # R_s
        self.R_s.setText("ВВведите R_s растянутой арматуры данного класса:")
        self.R_s.move(10, 85)
        self.input_R_s = QLineEdit("350", self)
        self.input_R_s.move(280, 85)
        # ------------------------------------------------------------------------
        self.A_s = QLabel(self)  # A_s
        self.A_s.setText("Введите A_s:")
        self.A_s.move(10, 110)
        self.input_A_s = QLineEdit("763", self)
        self.input_A_s.move(85, 110)
        # ------------------------------------------------------------------------
        self.M = QLabel(self)  # M
        self.M.setText("Введите M изгибающий момент в вертикальной плоскости:")
        self.M.move(10, 135)
        self.input_M = QLineEdit("82.6", self)
        self.input_M.move(320, 135)
        # ------------------------------------------------------------------------1
        self.h0 = QLabel(self)  # M
        self.h0.setText("Введите h0:")
        self.h0.move(10, 160)
        self.input_h0 = QLineEdit("369.5", self)
        self.input_h0.move(90, 160)
        # ------------------------------------------------------------------------2
        self.h0_i = QLabel(self)  # M
        self.h0_i.setText("Введите h0_i:")
        self.h0_i.move(10, 185)
        self.input_h0_i = QLineEdit("370", self)
        self.input_h0_i.move(90, 185)
        # ------------------------------------------------------------------------3
        self.b0 = QLabel(self)  # M
        self.b0.setText("Введите b0:")
        self.b0.move(10, 210)
        self.input_b0 = QLineEdit("90", self)
        self.input_b0.move(90, 210)
        # ------------------------------------------------------------------------4
        self.b0_i = QLabel(self)  # M
        self.b0_i.setText("Введите b0_i:")
        self.b0_i.move(10, 235)
        self.input_b0_i = QLineEdit("30", self)
        self.input_b0_i.move(90, 235)
        # ------------------------------------------------------------------------5
        self.b_ov = QLabel(self)  # M
        self.b_ov.setText("Введите b_ov:")
        self.b_ov.move(10, 260)
        self.input_b_ov = QLineEdit("75", self)
        self.input_b_ov.move(90, 260)
        # ------------------------------------------------------------------------6
        self.b = QLabel(self)  # M
        self.b.setText("Введите b:")
        self.b.move(10, 285)
        self.input_b = QLineEdit("150", self)
        self.input_b.move(90, 285)
        # ------------------------------------------------------------------------7
        self.h_f_sht = QLabel(self)  # M
        self.h_f_sht.setText("Введите h_f':")
        self.h_f_sht.move(10, 310)
        self.input_h_f_sht = QLineEdit("95", self)
        self.input_h_f_sht.move(90, 310)
        # ------------------------------------------------------------------------
        # текстовые вставки для условий из цикла
        self.conditionOne = QLabel(self)
        self.conditionOne.setText("Расчет производится как для таврового сечения")
        self.conditionOne.move(-300, -30)
        self.conditionTwo = QLabel(self)
        self.conditionTwo.setText("Расчет продолжается по формулам косого изгиба")
        self.conditionTwo.move(-300, -30)
        self.conditionThree = QLabel(self)
        self.conditionThree.setText("Условие соблюлось!")
        self.conditionThree.move(-300, -30)
        # блок else
        self.conditionOneElse = QLabel(self)
        self.conditionOneElse.setText("Условие A_b > A_ov не выполнено!")
        self.conditionOneElse.move(-300, -30)
        self.conditionTwoElse = QLabel(self)
        self.conditionTwoElse.setText("Условие (1.5 * A_web/(b + b_ov)) < x1 не выполнено!")
        self.conditionTwoElse.move(-300, -30)
        self.conditionThreeElseValues = QLabel(self)
        self.conditionThreeElseValues.setText(
            "Вывод значений не возможен, так как выше перечисленные условие(я) не выполнились!")
        self.conditionThreeElseValues.move(-300, -30)
        # ------------------------------------------------------------------------
        self.messageError = QLabel(self)
        self.messageError.setText("Введенные(-ое) значения(-е) не корректны(-о) (см. значения данные в чертеже)!")
        self.messageError.move(-300, -30)
        # ------------------------------------------------------------------------
        # текстовые вставки для переменных расчитаных из цикла, которые получились в итоге
        self.string_M_x = QLabel(self)
        self.string_A_web = QLabel(self)
        self.string_S_ov_x = QLabel(self)
        self.string_S_ov_y = QLabel(self)

        self.string_M_x.setText("\nM_x = " + str(1111111111111111111111111111111.111111111111111111111111111111111111))
        self.string_M_x.move(-300, -30)
        self.string_A_web.setText(
            "A_web = " + str(1111111111111111111111111111111.111111111111111111111111111111111111))
        self.string_A_web.move(-300, -30)
        self.string_S_ov_x.setText(
            "S_ov_x = " + str(1111111111111111111111111111111.111111111111111111111111111111111111))
        self.string_S_ov_x.move(-300, -30)
        self.string_S_ov_y.setText(
            "S_ov_y = " + str(1111111111111111111111111111111.111111111111111111111111111111111111))
        self.string_S_ov_y.move(-300, -30)

    def logicCalculations(self):
        self.Epsilant_R = 0.533
        self.slope_obj = 0
        self.R_b_obj = 0
        self.R_S_obj = 0
        self.A_s_obj = 0
        self.M_obj = 0
        self.h0 = 0
        self.h0_i = 0
        self.b0 = 0
        self.b = 0
        self.b0_i = 0
        self.b_ov = self.b_ov_sht = 0
        self.h_f_sht = 0
        self.A_b = 0
        self.A_ov = 0
        self.S_ov_y = 0
        self.S_ov_x = 0
        self.A_web = 0
        self.t = 0
        self.x1 = 0
        self.tg_oth = 0
        self.Epsilant_i = 0
        self.sigma_s = 0
        self.sigma_s_part = 0
        self.M_x = 0
        self.isRunning = True
        self.textFlag = False

        slope_obj = self.input_slope.text()
        R_b_obj = self.input_R_b.text()
        R_s_obj = self.input_R_s.text()
        A_s_obj = self.input_A_s.text()
        M_obj = self.input_M.text()
        h0 = self.input_h0.text()
        h0_i = self.input_h0_i.text()
        b0 = self.input_b0.text()
        b = self.input_b.text()
        b0_i = self.input_b0_i.text()
        b_ov = self.input_b_ov.text()
        h_f_sht = self.input_h_f_sht.text()


        # выше представлено присваивание по нажатию
        if slope_obj == '' or R_b_obj == '' or R_s_obj == '' or A_s_obj == '' or M_obj == '' or h0 == ''\
                or h0_i == '' or h_f_sht == '' or b0 == '' or b0_i == '' or b == '' or b_ov == '':
            self.string_M_x.move(-300, -30)
            self.string_A_web.move(-300, -30)
            self.string_S_ov_x.move(-300, -30)
            self.string_S_ov_y.move(-300, -30)
            self.conditionThree.move(-300, -30)

            self.conditionOne.move(-300, -30)
            self.conditionTwo.move(-300, -30)
            self.conditionThree.move(-300, -30)

            self.conditionOneElse.move(-300, -30)
            self.conditionTwoElse.move(-300, -30)
            self.conditionThreeElseValues.move(-300, -30)

            self.messageError.move(10, 395)
        else:

            self.slope_obj = float(slope_obj)
            self.R_b_obj = float(R_b_obj)
            self.R_s_obj = float(R_s_obj)
            self.A_s_obj = float(A_s_obj)
            self.M_obj = float(M_obj)

            self.h0 = float(h0)
            self.h0_i = float(h0_i)
            self.b0 = float(b0)
            self.b0_i = float(b0_i)
            self.b_ov = float(b_ov)
            self.b_ov_sht = self.b_ov
            self.b = float(b)
            self.h_f_sht = float(h_f_sht)
            # ------------------------------------------------------------------------
            if self.h0 > self.b0 and self.h0_i > self.b0_i and self.R_b_obj != 0 and self.R_s_obj !=0 and self.A_s_obj !=0 and self.M_obj !=0\
                    and self.h0 !=0 and self.h0_i !=0 and self.b0 != 0 and self.b0_i !=0 and self.b_ov != 0 and self.b_ov_sht != 0\
                    and self.b != 0 and self.h_f_sht != 0 and self.slope_obj != 0:
                self.messageError.move(-300, -30)

                self.A_b = self.R_s_obj * self.A_s_obj / self.R_b_obj
                self.A_b = round(self.A_b, -1)
                self.A_ov = self.b_ov_sht * self.h_f_sht
                self.S_ov_y = self.A_ov * (self.b0 + self.b_ov_sht / 2)
                self.S_ov_x = self.A_ov * (self.h0 - self.h_f_sht / 2)

                while self.isRunning:
                    if self.A_b > self.A_ov:
                        self.conditionOneElse.move(-300, -30)
                        self.conditionTwoElse.move(-300, -30)
                        self.conditionThreeElseValues.move(-300, -30)
                        self.conditionOne.move(10, 380)
                        self.A_web = self.A_b - self.A_ov
                        self.t = 1.5 * ((self.S_ov_y * self.slope_obj - self.S_ov_x) / self.A_web + self.b0 * self.slope_obj - self.h0)
                        self.t = round(self.t, 0)
                        self.x1 = -self.t + sqrt(self.t * self.t + 2 * self.slope_obj * self.A_web)
                        self.x1 = round(self.x1, 0)
                        if (1.5 * self.A_web / (self.b + self.b_ov)) < self.x1:
                            self.conditionTwoElse.move(-300, -30)
                            self.conditionTwo.move(10, 395)
                            self.tg_oth = self.x1 * self.x1 / (2 * self.A_web)
                            self.tg_oth = round(self.tg_oth, 3)
                            self.Epsilant_i = (self.b_ov_sht * self.tg_oth + self.x1) / ((self.b0_i + self.b_ov_sht) * self.tg_oth + self.h0_i)
                            if (self.Epsilant_i <= self.Epsilant_R):
                                self.conditionThreeElseValues.move(-300, -30)
                                self.conditionThree.move(10, 410)
                                self.textFlag = True
                                self.isRunning = False
                            else:
                                self.sigma_s = (700 * (0.8 / self.Epsilant_i - 1) + 2 * self.R_s_obj) / 3
                                self.sigma_s = round(self.sigma_s, 0)
                                self.sigma_s_part = self.sigma_s / self.R_s_obj
                                self.A_b = self.sigma_s * self.A_s_obj / self.R_b_obj
                                self.b0 = (2 * 120 + self.sigma_s_part * 30) / (2 + self.sigma_s_part)
                                self.h0 = 400 - 30 - 1 * 45 / (2 + self.sigma_s_part)
                                self.S_ov_y = self.A_ov * (self.b0 + self.b_ov_sht / 2)
                                self.S_ov_x = self.A_ov * (self.h0 - self.h_f_sht / 2)
                                self.A_web = self.A_b - self.A_ov
                                self.t = 1.5 * ((
                                                            self.S_ov_y * self.slope_obj - self.S_ov_x) / self.A_web + self.b0 * self.slope_obj - self.h0)
                                self.x1 = -self.t + sqrt(self.t * self.t + 2 * self.slope_obj * self.A_web)
                                self.x1 = round(self.x1, 0)
                                self.M_x = self.M_obj * self.slope_obj / sqrt(1 + self.slope_obj * self.slope_obj)
                                self.M_x = round(self.M_x, -1)
                        else:
                            self.conditionTwo.move(-300, -30)
                            self.conditionThree.move(-300, -30)
                            self.conditionTwoElse.move(10, 395)
                            self.isRunning = False
                    else:
                        self.conditionOne.move(-300, -30)
                        self.conditionTwo.move(-300, -30)
                        self.conditionThree.move(-300, -30)
                        self.conditionOneElse.move(10, 380)
                        self.isRunning = False
                # ------------------------------------------------------------------------
                if self.textFlag:
                    self.string_M_x.setText("M_x = " + str(self.M_x))
                    self.string_M_x.move(10, 425)
                    self.string_A_web.setText("A_web = " + str(self.A_web))
                    self.string_A_web.move(10, 445)
                    self.string_S_ov_x.setText("S_ov_x = " + str(self.S_ov_x))
                    self.string_S_ov_x.move(10, 460)
                    self.string_S_ov_y.setText("S_ov_y = " + str(self.S_ov_y))
                    self.string_S_ov_y.move(10, 475)
                    self.conditionThreeElseValues.move(-300, -30)
                else:
                    self.string_M_x.move(-300, -30)
                    self.string_A_web.move(-300, -30)
                    self.string_S_ov_x.move(-300, -30)
                    self.string_S_ov_y.move(-300, -30)
                    self.conditionThree.move(-300, -30)
                    self.conditionThreeElseValues.move(10, 410)
            else:
                self.string_M_x.move(-300, -30)
                self.string_A_web.move(-300, -30)
                self.string_S_ov_x.move(-300, -30)
                self.string_S_ov_y.move(-300, -30)
                self.conditionThree.move(-300, -30)

                self.conditionOne.move(-300, -30)
                self.conditionTwo.move(-300, -30)
                self.conditionThree.move(-300, -30)

                self.conditionOneElse.move(-300, -30)
                self.conditionTwoElse.move(-300, -30)
                self.conditionThreeElseValues.move(-300, -30)

                self.messageError.move(10, 395)

    def SaveLogic(self):
        fi = QFileDialog.getSaveFileName(None, "QFileDialog.getOpenFileName()", "", "pickle (*.pkl)")
        fi = fi[0]
        fi = os.path.basename(fi)
        with open(fi, 'wb') as f:
                pickle.dump(self.input_slope.text(), f)
                pickle.dump(self.input_R_b.text(), f)
                pickle.dump(self.input_R_s.text(), f)
                pickle.dump(self.input_A_s.text(), f)
                pickle.dump(self.input_M.text(), f)
                pickle.dump(self.input_h0.text(), f)
                pickle.dump(self.input_h0_i.text(), f)
                pickle.dump(self.input_b0.text(), f)
                pickle.dump(self.input_b0_i.text(), f)
                pickle.dump(self.input_b_ov.text(), f)
                pickle.dump(self.input_b.text(), f)
                pickle.dump(self.input_h_f_sht.text(), f)
    '''     with open("savePc.pkl", 'wb') as f:
            pickle.dump(self.input_slope.text(), f)
            pickle.dump(self.input_R_b.text(), f)
            pickle.dump(self.input_R_s.text(), f)
            pickle.dump(self.input_A_s.text(), f)
            pickle.dump(self.input_M.text(), f)
            pickle.dump(self.input_h0.text(), f)
            pickle.dump(self.input_h0_i.text(), f)
            pickle.dump(self.input_b0.text(), f)
            pickle.dump(self.input_b0_i.text(), f)
            pickle.dump(self.input_b_ov.text(), f)
            pickle.dump(self.input_b.text(), f)
            pickle.dump(self.input_h_f_sht.text(), f)'''

    def LoadLogic(self):
        fi = QFileDialog.getOpenFileName(None, "QFileDialog.getOpenFileName()", "", "pickle (*.pkl)")
        fi = fi[0]
        fi = os.path.basename(fi)
        with open(fi, 'rb') as f:
            self.input_slope.setText(pickle.load(f))
            self.input_R_b.setText(pickle.load(f))
            self.input_R_s.setText(pickle.load(f))
            self.input_A_s.setText(pickle.load(f))
            self.input_M.setText(pickle.load(f))
            self.input_h0.setText(pickle.load(f))
            self.input_h0_i.setText(pickle.load(f))
            self.input_b0.setText(pickle.load(f))
            self.input_b0_i.setText(pickle.load(f))
            self.input_b_ov.setText(pickle.load(f))
            self.input_b.setText(pickle.load(f))
            self.input_h_f_sht.setText(pickle.load(f))



    def openSecondForm(self):
        self.second_form = SecondForm(self)
        self.second_form.show()

    def openThirdForm(self):
        self.third_form = ThirdForm(self)
        self.third_form.show()

    def openFourthForm(self):
        self.fourth_form = FourthForm(self)
        self.fourth_form.show()



#gljkhbjkfdgfgfg

class SecondForm(QWidget):

    def __init__(self, *args):
        super().__init__()
        self.initUI(args)

    def initUI(self, args):
        self.setGeometry(545, 45, 714, 138)
        self.setWindowTitle('Задание')
        self.pixmap = QPixmap("cwImage.png")
        self.lbl = QLabel(self)
        self.lbl.setPixmap(self.pixmap)


class ThirdForm(QWidget):

    def __init__(self, *args):
        super().__init__()
        self.initUI(args)

    def initUI(self, args):
        self.setGeometry(400, 45, 955, 499)
        self.setWindowTitle('Классы бетона')
        self.pixmap = QPixmap("classbet.jpg")
        self.lbl = QLabel(self)
        self.lbl.setPixmap(self.pixmap)


class FourthForm(QWidget):

    def __init__(self, *args):
        super().__init__()
        self.initUI(args)

    def initUI(self, args):
        self.setGeometry(545, 45, 453, 478)
        self.setWindowTitle('Классы арматуры')
        self.pixmap = QPixmap("classarm.jpeg")
        self.lbl = QLabel(self)
        self.lbl.setPixmap(self.pixmap)

# ------------------------------------------------------------------------


if __name__ == '__main__':
    app = QApplication(sys.argv)
    palette = QPalette()
    palette.setColor(QPalette.Background, Qt.lightGray)
    ex = Example()
    ex.setPalette(palette)
    ex.show()
    sys.exit(app.exec_())