
from PyQt5.QtWidgets import QPushButton,  QGroupBox, QDialog, QVBoxLayout, QLabel, QGridLayout, QComboBox, QCheckBox, \
    QTableWidget, QTableWidgetItem, QPlainTextEdit
from PyQt5.QtCore import pyqtSlot
from inspect import cleandoc


class App(QDialog):

    def __init__(self):
        super().__init__()
        self.title = 'PyQt5 layout - pythonspot.com'
        self.left = 200
        self.top = 200
        self.width = 600
        self.height = 800
        self.listaUe = ['at', 'be', 'bg', 'hr', 'cy', 'cz', 'dk', 'ee', 'fi', 'fr', 'gr', 'es', 'ie', 'lt', 'lu', 'lv',
                        'mt', 'nt', 'de', 'pl', 'pt', 'sk', 'si', 'se', 'hu', 'gb', 'it']
        self.listaUe = sorted(self.listaUe)
        self.lista1 = ('none', '1a', '1b', '1c', '1d')
        self.lista2 = ('none', '2a', '2b', '2c', '2d')
        self.lista3 = ('none', '3a', '3b', '3c', '3d')
        self.horizontalGroupBox = QGroupBox("Wprowadź dane")
        self.comboEu = self.createComboBox(self.listaUe)
        self.combo1 = self.createComboBox(self.lista1)
        self.combo2 = self.createComboBox(self.lista2)
        self.combo3 = self.createComboBox(self.lista3)
        self.checkB = QCheckBox()
        self.tab1 = []
        self.tab1 = self.createTable()
        self.initUI()
        self.wynik = []

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        self.createGridLayout()
        self.textbox = QPlainTextEdit(self)
        self.textbox.resize(280, 400)
        windowLayout = QVBoxLayout()
        windowLayout.addWidget(self.horizontalGroupBox)
        windowLayout.addWidget(self.tab1)
        windowLayout.addWidget(self.textbox)
        self.setLayout(windowLayout)
        self.show()

    def createGridLayout(self):
        layout = QGridLayout()
        dodaj = QPushButton('Dodaj')
        dodaj.clicked.connect(self.on_click_dodaj)
        raport = QPushButton('Generuj Raport')
        raport.clicked.connect(self.on_click_raport)
        layout.addWidget(QLabel('Wybierz państwo'), 0, 0)
        layout.addWidget(QLabel('Kryterium 1'), 0, 1)
        layout.addWidget(QLabel('Kryterium 2'), 0, 2)
        layout.addWidget(QLabel('Kryterium 3'), 0, 3)
        layout.addWidget(QLabel('Stała'), 0, 4)
        layout.addWidget(self.comboEu, 1, 0)
        layout.addWidget(self.combo1, 1, 1)
        layout.addWidget(self.combo2, 1, 2)
        layout.addWidget(self.combo3, 1, 3)
        layout.addWidget(self.tab1, 3, 0)
        layout.addWidget(self.checkB, 1, 4)
        layout.addWidget(dodaj, 2, 0)
        layout.addWidget(raport, 2, 3)
        self.horizontalGroupBox.setLayout(layout)

    def createComboBox(self, list):
        combo = QComboBox()
        combo.setMaximumWidth(150)
        for v in (list):
            combo.addItem(v)
        return combo

    def createTable(self):
        name = QTableWidget()
        name.setRowCount(0)
        name.setColumnCount(5)
        name.setEnabled(False)
        return name

    @pyqtSlot()
    def on_click_dodaj(self):
        rowPosition = self.tab1.rowCount()
        self.tab1.insertRow(rowPosition)
        self.tab1.setItem(rowPosition, 0, QTableWidgetItem(self.comboEu.currentText()))
        self.tab1.setItem(rowPosition, 1, QTableWidgetItem(self.combo1.currentText()))
        self.tab1.setItem(rowPosition, 2, QTableWidgetItem(self.combo2.currentText()))
        self.tab1.setItem(rowPosition, 3, QTableWidgetItem(self.combo3.currentText()))
        if self.checkB.checkState():
            self.tab1.setItem(rowPosition, 4, QTableWidgetItem('Tak'))
            self.wynik.append([self.comboEu.currentText(), self.combo1.currentText(), self.combo2.currentText(),
                               self.combo3.currentText(), 'Tak'])
        else:
            self.tab1.setItem(rowPosition, 4, QTableWidgetItem('Nie'))
            self.wynik.append([self.comboEu.currentText(), self.combo1.currentText(), self.combo2.currentText(),
                               self.combo3.currentText(), 'Nie'])

    @pyqtSlot()
    def on_click_raport(self):
         self.textbox.clear()
         panstwa = ''
         if self.tab1.rowCount() != 0:
            for i in range(self.tab1.rowCount()):
                panstwa += str(self.wynik[i][0]) + ','
            self.textbox.insertPlainText(cleandoc(f"""<selectioncryteria id="1"share="{panstwa}pl">
            <generation>Provided</generation>
            <selectionka id="2" share="{panstwa}pl">"""))
            for i in range(self.tab1.rowCount()):
                panstwo = str(self.wynik[i][0])
                for j in range(1, 4):
                    reason = str(self.wynik[i][j])
                    if reason != 'none':
                        self.textbox.insertPlainText(cleandoc(f"""\n<related>{panstwo}</related>
                        <reason>{reason}</reason>
                        </selectionka>"""))