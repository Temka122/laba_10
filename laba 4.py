import sys
import math
from PyQt5.QtWidgets import (QApplication, QWidget, QLabel, QLineEdit, QPushButton,
                             QVBoxLayout, QHBoxLayout, QMessageBox, QTabWidget, QComboBox)
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt

def calculate_v(x, y, z, f):
    try:
        func = math.cos
        numerator = 1 + math.sin(x + y)**2
        denominator = abs(x - (2 * y / (1 + x**2 * y**2)))
        term1 = numerator / denominator * x**abs(y)
        term2 = func(math.atan(1/z))**2
        v = term1 + term2
        return f"Р РµР·СѓР»СЊС‚Р°С‚ v: {v:.4f}"
    except Exception as e:
        return f"РћС€РёР±РєР° РїСЂРё СЂР°СЃС‡РµС‚Рµ v: {e}"

def calculate_c(x, y, f):
    try:
        if f == 'cos':
            func = math.cos
        elif f == 'exp':
            func = math.exp
        elif f == 'sin':
            func = math.sin
        else:
            return "РќРµРІРµСЂРЅР°СЏ С„СѓРЅРєС†РёСЏ"

        if x * y > 12:
            c = func(x**3 + 1/math.tan(y))
        elif x * y < 7:
            c = math.sinh(x**3) + y**2
        else:
            c = math.cos(x - x**3)
        return f"Р РµР·СѓР»СЊС‚Р°С‚ c: {c:.4f}"
    except Exception as e:
        return f"РћС€РёР±РєР° РїСЂРё СЂР°СЃС‡РµС‚Рµ c: {e}"

class FormulaApp(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.setWindowTitle('РџСЂР°РєС‚РёС‡РµСЃРєР°СЏ СЂР°Р±РѕС‚Р° в„–6')
        self.setGeometry(100, 100, 500, 500)

        self.tabs = QTabWidget()
        self.tab1 = QWidget()
        self.tab2 = QWidget()

        self.tabs.addTab(self.tab1, "Р’С‹С‡РёСЃР»РµРЅРёРµ v")
        self.tabs.addTab(self.tab2, "Р’С‹С‡РёСЃР»РµРЅРёРµ c")

        self.create_tab1_ui()

        self.create_tab2_ui()

        main_layout = QVBoxLayout()
        main_layout.addWidget(self.tabs)
        self.setLayout(main_layout)

    def create_tab1_ui(self):
        layout = QVBoxLayout()

        img1_label = QLabel(self)
        img1_pixmap = QPixmap("1.png")  # РџСѓС‚СЊ Рє РїРµСЂРІРѕР№ РєР°СЂС‚РёРЅРєРµ
        img1_label.setPixmap(img1_pixmap.scaled(379, 64))

        layout.addWidget(img1_label, alignment=Qt.AlignCenter)

        # РџРѕР»СЏ РІРІРѕРґР° РґР»СЏ X, Y Рё Z
        self.x_input = QLineEdit(self)
        self.x_input.setPlaceholderText("Р’РІРµРґРёС‚Рµ Р·РЅР°С‡РµРЅРёРµ X")
        layout.addWidget(self.x_input)

        self.y_input = QLineEdit(self)
        self.y_input.setPlaceholderText("Р’РІРµРґРёС‚Рµ Р·РЅР°С‡РµРЅРёРµ Y")
        layout.addWidget(self.y_input)

        self.z_input = QLineEdit(self)
        self.z_input.setPlaceholderText("Р’РІРµРґРёС‚Рµ Р·РЅР°С‡РµРЅРёРµ Z")
        layout.addWidget(self.z_input)

        self.v_button = QPushButton('Р’С‹С‡РёСЃР»РёС‚СЊ v', self)
        self.v_button.clicked.connect(self.on_calculate_v)
        layout.addWidget(self.v_button)

        self.result_label_tab1 = QLabel('Р—РґРµСЃСЊ Р±СѓРґРµС‚ РІС‹РІРѕРґРёС‚СЊСЃСЏ СЂРµР·СѓР»СЊС‚Р°С‚', self)
        layout.addWidget(self.result_label_tab1)

        self.tab1.setLayout(layout)

    def create_tab2_ui(self):
        layout = QVBoxLayout()

        img2_label = QLabel(self)
        img2_pixmap = QPixmap("2.png")  # РџСѓС‚СЊ РєРѕ РІС‚РѕСЂРѕР№ РєР°СЂС‚РёРЅРєРµ
        img2_label.setPixmap(img2_pixmap.scaled(280, 93))

        layout.addWidget(img2_label, alignment=Qt.AlignCenter)

        self.x_input_tab2 = QLineEdit(self)
        self.x_input_tab2.setPlaceholderText("Р’РІРµРґРёС‚Рµ Р·РЅР°С‡РµРЅРёРµ X")
        layout.addWidget(self.x_input_tab2)

        self.y_input_tab2 = QLineEdit(self)
        self.y_input_tab2.setPlaceholderText("Р’РІРµРґРёС‚Рµ Р·РЅР°С‡РµРЅРёРµ Y")
        layout.addWidget(self.y_input_tab2)

        self.f_combo_tab2 = QComboBox(self)
        self.f_combo_tab2.addItems(['cos', 'exp', 'sin'])
        layout.addWidget(self.f_combo_tab2)

        self.c_button = QPushButton('Р’С‹С‡РёСЃР»РёС‚СЊ c', self)
        self.c_button.clicked.connect(self.on_calculate_c)
        layout.addWidget(self.c_button)

        self.result_label_tab2 = QLabel('Р—РґРµСЃСЊ Р±СѓРґРµС‚ РІС‹РІРѕРґРёС‚СЊСЃСЏ СЂРµР·СѓР»СЊС‚Р°С‚', self)
        layout.addWidget(self.result_label_tab2)

        self.tab2.setLayout(layout)

    def get_inputs(self, tab=1):
        try:
            if tab == 1:
                x = float(self.x_input.text())
                y = float(self.y_input.text())
                z = float(self.z_input.text())
                f = 0
            else:
                x = float(self.x_input_tab2.text())
                y = float(self.y_input_tab2.text())
                z = 0  # Р’РєР»Р°РґРєР° 2 РЅРµ РёСЃРїРѕР»СЊР·СѓРµС‚ z
                f = self.f_combo_tab2.currentText()
            return x, y, z, f
        except ValueError:
            QMessageBox.warning(self, 'РћС€РёР±РєР°', 'Р’РІРµРґРёС‚Рµ РєРѕСЂСЂРµРєС‚РЅС‹Рµ С‡РёСЃР»РѕРІС‹Рµ Р·РЅР°С‡РµРЅРёСЏ!')
            return None, None, None, None

    def on_calculate_v(self):
        x, y, z, f = self.get_inputs(tab=1)
        if x is not None and y is not None and z is not None:
            result = calculate_v(x, y, z, f)
            self.result_label_tab1.setText(result)

    def on_calculate_c(self):
        x, y, _, f = self.get_inputs(tab=2)
        if x is not None and y is not None:
            result = calculate_c(x, y, f)
            self.result_label_tab2.setText(result)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = FormulaApp()
    ex.show()
    sys.exit(app.exec_())
