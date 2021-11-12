# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'UI_Kiosco.ui'
##
## Created by: Qt User Interface Compiler version 5.15.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(960, 700)
        MainWindow.setStyleSheet(u"")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.window_layout = QVBoxLayout(self.centralwidget)
        self.window_layout.setSpacing(0)
        self.window_layout.setObjectName(u"window_layout")
        self.window_layout.setContentsMargins(10, 10, 10, 10)
        self.window = QFrame(self.centralwidget)
        self.window.setObjectName(u"window")
        self.window.setEnabled(True)
        self.window.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:1, y1:1, x2:0, y2:0, stop:0 rgba(15, 12, 41, 255), stop:1 rgba(48, 43, 99, 255));\n"
"border-radius:10px;")
        self.window.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.window)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.title_bar = QFrame(self.window)
        self.title_bar.setObjectName(u"title_bar")
        self.title_bar.setEnabled(True)
        self.title_bar.setMinimumSize(QSize(0, 40))
        self.title_bar.setMaximumSize(QSize(16777215, 50))
        self.title_bar.setStyleSheet(u"background-color: none;")
        self.title_bar.setFrameShape(QFrame.StyledPanel)
        self.title_bar.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.title_bar)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 5, 0, 0)
        self.frame_title = QFrame(self.title_bar)
        self.frame_title.setObjectName(u"frame_title")
        font = QFont()
        font.setFamily(u"JasmineUPC")
        font.setPointSize(17)
        self.frame_title.setFont(font)
        self.frame_title.setFrameShape(QFrame.StyledPanel)
        self.frame_title.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame_title)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_title = QLabel(self.frame_title)
        self.label_title.setObjectName(u"label_title")
        font1 = QFont()
        font1.setFamily(u"Levenim MT")
        font1.setPointSize(14)
        self.label_title.setFont(font1)
        self.label_title.setStyleSheet(u"color: rgb(0, 212, 212)")

        self.horizontalLayout_4.addWidget(self.label_title)

        self.label_backup = QLabel(self.frame_title)
        self.label_backup.setObjectName(u"label_backup")
        self.label_backup.setFont(font1)
        self.label_backup.setStyleSheet(u"color: rgb(0, 170, 255);")

        self.horizontalLayout_4.addWidget(self.label_backup)


        self.horizontalLayout.addWidget(self.frame_title)

        self.frame_btns = QFrame(self.title_bar)
        self.frame_btns.setObjectName(u"frame_btns")
        self.frame_btns.setMaximumSize(QSize(100, 16777215))
        self.frame_btns.setFrameShape(QFrame.StyledPanel)
        self.frame_btns.setFrameShadow(QFrame.Raised)
        self.btn_close = QPushButton(self.frame_btns)
        self.btn_close.setObjectName(u"btn_close")
        self.btn_close.setGeometry(QRect(70, 10, 16, 16))
        self.btn_close.setMinimumSize(QSize(16, 16))
        self.btn_close.setMaximumSize(QSize(17, 17))
        self.btn_close.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_close.setStyleSheet(u"QPushButton {\n"
"	border: none;\n"
"	border-radius: 8px;\n"
"	background-color: rgb(255, 0, 0);\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgba(255, 0, 0, 150);\n"
"}")
        self.btn_minimize = QPushButton(self.frame_btns)
        self.btn_minimize.setObjectName(u"btn_minimize")
        self.btn_minimize.setGeometry(QRect(40, 10, 16, 16))
        self.btn_minimize.setMinimumSize(QSize(16, 16))
        self.btn_minimize.setMaximumSize(QSize(17, 17))
        self.btn_minimize.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_minimize.setStyleSheet(u"QPushButton {\n"
"	border: none;\n"
"	border-radius: 8px;\n"
"	background-color: rgb(85, 255, 127);\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgba(58, 255, 127, 150);\n"
"}")

        self.horizontalLayout.addWidget(self.frame_btns)


        self.verticalLayout.addWidget(self.title_bar)

        self.content_bar = QFrame(self.window)
        self.content_bar.setObjectName(u"content_bar")
        self.content_bar.setStyleSheet(u"background-color: none;")
        self.content_bar.setFrameShape(QFrame.StyledPanel)
        self.content_bar.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.content_bar)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(15, 0, 15, 0)
        self.frame_menus = QFrame(self.content_bar)
        self.frame_menus.setObjectName(u"frame_menus")
        self.frame_menus.setMinimumSize(QSize(150, 0))
        self.frame_menus.setMaximumSize(QSize(150, 16777215))
        self.frame_menus.setFrameShape(QFrame.StyledPanel)
        self.frame_menus.setFrameShadow(QFrame.Raised)
        self.btn_ventas = QPushButton(self.frame_menus)
        self.btn_ventas.setObjectName(u"btn_ventas")
        self.btn_ventas.setGeometry(QRect(20, 60, 111, 41))
        font2 = QFont()
        font2.setFamily(u"Latha")
        font2.setPointSize(15)
        font2.setBold(False)
        font2.setItalic(False)
        font2.setWeight(50)
        self.btn_ventas.setFont(font2)
        self.btn_ventas.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_ventas.setStyleSheet(u"QPushButton {\n"
"	background-color: qlineargradient(spread:pad, x1:0.517, y1:1, x2:0.511, 				y2:0, stop:0 rgba(0, 69, 104, 255), stop:1 rgba(0, 170, 255, 255));\n"
"	color: rgb(0, 0, 0);\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: qlineargradient(spread:pad, x1:0.517, y1:1, x2:0.511, 				y2:0, stop:0 rgba(0, 69, 104, 150), stop:1 rgba(0, 170, 255, 150));\n"
"	color: rgb(255, 255, 255);\n"
"}")
        self.btn_cuentas = QPushButton(self.frame_menus)
        self.btn_cuentas.setObjectName(u"btn_cuentas")
        self.btn_cuentas.setGeometry(QRect(20, 120, 111, 41))
        self.btn_cuentas.setFont(font2)
        self.btn_cuentas.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_cuentas.setStyleSheet(u"QPushButton {\n"
"	background-color: qlineargradient(spread:pad, x1:0.517, y1:1, x2:0.511, 				y2:0, stop:0 rgba(0, 69, 104, 255), stop:1 rgba(0, 170, 255, 255));\n"
"	color: rgb(0, 0, 0);\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: qlineargradient(spread:pad, x1:0.517, y1:1, x2:0.511, 				y2:0, stop:0 rgba(0, 69, 104, 150), stop:1 rgba(0, 170, 255, 150));\n"
"	color: rgb(255, 255, 255);\n"
"}")
        self.btn_historial = QPushButton(self.frame_menus)
        self.btn_historial.setObjectName(u"btn_historial")
        self.btn_historial.setGeometry(QRect(20, 180, 111, 41))
        self.btn_historial.setFont(font2)
        self.btn_historial.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_historial.setStyleSheet(u"QPushButton {\n"
"	background-color: qlineargradient(spread:pad, x1:0.517, y1:1, x2:0.511, 				y2:0, stop:0 rgba(0, 69, 104, 255), stop:1 rgba(0, 170, 255, 255));\n"
"	color: rgb(0, 0, 0);\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: qlineargradient(spread:pad, x1:0.517, y1:1, x2:0.511, 				y2:0, stop:0 rgba(0, 69, 104, 150), stop:1 rgba(0, 170, 255, 150));\n"
"	color: rgb(255, 255, 255);\n"
"}")
        self.btn_configuracion = QPushButton(self.frame_menus)
        self.btn_configuracion.setObjectName(u"btn_configuracion")
        self.btn_configuracion.setGeometry(QRect(20, 450, 111, 41))
        self.btn_configuracion.setFont(font2)
        self.btn_configuracion.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_configuracion.setStyleSheet(u"QPushButton {\n"
"	background-color: qlineargradient(spread:pad, x1:0.517, y1:1, x2:0.511, 				y2:0, stop:0 rgba(0, 69, 104, 255), stop:1 rgba(0, 170, 255, 255));\n"
"	color: rgb(0, 0, 0);\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: qlineargradient(spread:pad, x1:0.517, y1:1, x2:0.511, 				y2:0, stop:0 rgba(0, 69, 104, 150), stop:1 rgba(0, 170, 255, 150));\n"
"	color: rgb(255, 255, 255);\n"
"}")

        self.horizontalLayout_3.addWidget(self.frame_menus)

        self.frame_pages = QFrame(self.content_bar)
        self.frame_pages.setObjectName(u"frame_pages")
        self.frame_pages.setFrameShape(QFrame.StyledPanel)
        self.frame_pages.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_pages)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 10, 0, 0)
        self.pages_widget = QStackedWidget(self.frame_pages)
        self.pages_widget.setObjectName(u"pages_widget")
        font3 = QFont()
        font3.setFamily(u"Latha")
        font3.setPointSize(14)
        self.pages_widget.setFont(font3)
        self.pages_widget.setStyleSheet(u"")
        self.page_ventas = QWidget()
        self.page_ventas.setObjectName(u"page_ventas")
        self.listaVentas = QTableWidget(self.page_ventas)
        self.listaVentas.setObjectName(u"listaVentas")
        self.listaVentas.setGeometry(QRect(30, 70, 301, 501))
        font4 = QFont()
        font4.setFamily(u"Levenim MT")
        font4.setPointSize(12)
        self.listaVentas.setFont(font4)
        self.listaVentas.setFocusPolicy(Qt.StrongFocus)
        self.listaVentas.setStyleSheet(u"QTableWidget {	\n"
"	background-color: qlineargradient(spread:pad, x1:0.522682, y1:1, x2:0.516682, y2:0.011, stop:0 rgba(0, 111, 166, 255), stop:1 rgba(0, 170, 255, 255));\n"
"	border-radius: 5px;\n"
"	gridline-color: rgb(44, 49, 60);\n"
"	border-bottom: 1px solid rgb(44, 49, 60);\n"
"}\n"
"QTableWidget::item{\n"
"	border-color: rgb(44, 49, 60);\n"
"	padding-left: 5px;\n"
"	padding-right: 5px;\n"
"	gridline-color: rgb(44, 49, 60);\n"
"}\n"
"QTableWidget::item:selected{\n"
"	background-color: rgb(27, 55, 83);\n"
"}\n"
"QScrollBar:horizontal {\n"
"    border: none;\n"
"    background: rgb(52, 59, 72);\n"
"    height: 14px;\n"
"    margin: 0px 21px 0 21px;\n"
"	border-radius: 0px;\n"
"}\n"
" QScrollBar:vertical {\n"
"	border: none;\n"
"    background: rgb(52, 59, 72);\n"
"    width: 14px;\n"
"    margin: 21px 0 21px 0;\n"
"	border-radius: 0px;\n"
" }\n"
"QHeaderView::section{\n"
"	Background-color: qlineargradient(spread:pad, x1:0.522682, y1:1, x2:0.516682, y2:0.011, stop:0 rgba(0, 111, 166, 255), stop:1 rgba(0, "
                        "170, 255, 255));\n"
"	max-width: 30px;\n"
"	border: 1px solid rgb(44, 49, 60);\n"
"	border-style: none;\n"
"    border-bottom: 1px solid rgb(44, 49, 60);\n"
"    border-right: 1px solid rgb(44, 49, 60);\n"
"}\n"
"QTableWidget::horizontalHeader {	\n"
"	background-color:  qlineargradient(spread:pad, x1:0.522682, y1:1, x2:0.516682, y2:0.011, stop:0 rgba(0, 111, 166, 255), stop:1 rgba(0, 170, 255, 255));\n"
"}\n"
"QHeaderView::section:horizontal\n"
"{\n"
"    border: 1px solid rgb(32, 34, 42);\n"
"	background-color: qlineargradient(spread:pad, x1:0.522682, y1:1, x2:0.516682, y2:0.011, stop:0 rgba(0, 111, 166, 255), stop:1 rgba(0, 170, 255, 255));\n"
"	padding: 3px;\n"
"}\n"
"QHeaderView::section:vertical\n"
"{\n"
"    border: 1px solid rgb(44, 49, 60);\n"
"}")
        self.listaVentas.setFrameShape(QFrame.VLine)
        self.listaVentas.setFrameShadow(QFrame.Sunken)
        self.listaVentas.setLineWidth(2)
        self.listaVentas.setSizeAdjustPolicy(QAbstractScrollArea.AdjustIgnored)
        self.listaVentas.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.listaVentas.setSelectionMode(QAbstractItemView.SingleSelection)
        self.listaVentas.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.listaVentas.horizontalHeader().setDefaultSectionSize(77)
        self.listaVentas.horizontalHeader().setHighlightSections(False)
        self.listaVentas.horizontalHeader().setStretchLastSection(True)
        self.listaVentas.verticalHeader().setVisible(False)
        self.listaVentas.verticalHeader().setHighlightSections(False)
        self.label_ventas = QLabel(self.page_ventas)
        self.label_ventas.setObjectName(u"label_ventas")
        self.label_ventas.setGeometry(QRect(40, 30, 181, 31))
        font5 = QFont()
        font5.setFamily(u"Levenim MT")
        font5.setPointSize(14)
        font5.setBold(False)
        font5.setWeight(50)
        self.label_ventas.setFont(font5)
        self.label_ventas.setStyleSheet(u"color: rgb(0, 170, 255);")
        self.label_ingreso = QLabel(self.page_ventas)
        self.label_ingreso.setObjectName(u"label_ingreso")
        self.label_ingreso.setGeometry(QRect(370, 30, 171, 31))
        self.label_ingreso.setFont(font1)
        self.label_ingreso.setStyleSheet(u"color: rgb(0, 170, 255);")
        self.btn_agregar = QPushButton(self.page_ventas)
        self.btn_agregar.setObjectName(u"btn_agregar")
        self.btn_agregar.setGeometry(QRect(360, 260, 121, 41))
        self.btn_agregar.setFont(font3)
        self.btn_agregar.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_agregar.setStyleSheet(u"QPushButton {\n"
"	background-color: qlineargradient(spread:pad, x1:0.517, y1:1, x2:0.511, 				y2:0, stop:0 rgba(0, 69, 104, 255), stop:1 rgba(0, 170, 255, 255));\n"
"	color: rgb(0, 0, 0);\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: qlineargradient(spread:pad, x1:0.517, y1:1, x2:0.511, 				y2:0, stop:0 rgba(0, 69, 104, 150), stop:1 rgba(0, 170, 255, 150));\n"
"	color: rgb(255, 255, 255);\n"
"}")
        self.btn_borrar = QPushButton(self.page_ventas)
        self.btn_borrar.setObjectName(u"btn_borrar")
        self.btn_borrar.setGeometry(QRect(360, 340, 121, 41))
        self.btn_borrar.setFont(font3)
        self.btn_borrar.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_borrar.setStyleSheet(u"QPushButton {\n"
"	background-color: qlineargradient(spread:pad, x1:0.517, y1:1, x2:0.511, 				y2:0, stop:0 rgba(0, 69, 104, 255), stop:1 rgba(0, 170, 255, 255));\n"
"	color: rgb(0, 0, 0);\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: qlineargradient(spread:pad, x1:0.517, y1:1, x2:0.511, 				y2:0, stop:0 rgba(0, 69, 104, 150), stop:1 rgba(0, 170, 255, 150));\n"
"	color: rgb(255, 255, 255);\n"
"}")
        self.label_dia = QLabel(self.page_ventas)
        self.label_dia.setObjectName(u"label_dia")
        self.label_dia.setGeometry(QRect(370, 520, 271, 41))
        self.label_dia.setFont(font1)
        self.label_dia.setStyleSheet(u"color: rgb(0, 170, 255);")
        self.ingreso_entry = QLineEdit(self.page_ventas)
        self.ingreso_entry.setObjectName(u"ingreso_entry")
        self.ingreso_entry.setGeometry(QRect(360, 70, 261, 41))
        self.ingreso_entry.setFont(font1)
        self.ingreso_entry.setStyleSheet(u"QLineEdit {\n"
"	background-color: qlineargradient(spread:pad, x1:0.522682, y1:1, 						x2:0.516682, y2:0.011, stop:0 rgba(0, 111, 166, 255), stop:1 rgba(0, 170, 			255, 255));\n"
"}\n"
"\n"
"QLineEdit:hover {\n"
"	background-color: qlineargradient(spread:pad, x1:0.528, y1:1, x2:0.522, y2:0.596227, stop:0 rgba(0, 111, 166, 255), stop:1 rgba(0, 170, 255, 255));\n"
"}")
        self.adicional_entry = QLineEdit(self.page_ventas)
        self.adicional_entry.setObjectName(u"adicional_entry")
        self.adicional_entry.setGeometry(QRect(360, 160, 261, 41))
        self.adicional_entry.setFont(font1)
        self.adicional_entry.setStyleSheet(u"QLineEdit {\n"
"	background-color: qlineargradient(spread:pad, x1:0.522682, y1:1, 						x2:0.516682, y2:0.011, stop:0 rgba(0, 111, 166, 255), stop:1 rgba(0, 170, 			255, 255));\n"
"}\n"
"\n"
"QLineEdit:hover {\n"
"	background-color: qlineargradient(spread:pad, x1:0.528, y1:1, x2:0.522, y2:0.596227, stop:0 rgba(0, 111, 166, 255), stop:1 rgba(0, 170, 255, 255));\n"
"}")
        self.label_status = QLineEdit(self.page_ventas)
        self.label_status.setObjectName(u"label_status")
        self.label_status.setGeometry(QRect(370, 430, 261, 41))
        self.label_status.setFont(font1)
        self.label_status.setCursor(QCursor(Qt.ArrowCursor))
        self.label_status.setFocusPolicy(Qt.NoFocus)
        self.label_status.setAcceptDrops(False)
        self.label_status.setStyleSheet(u"background-color: rgba(0,0,0,0);\n"
"color: rgb(0, 170, 255);")
        self.pages_widget.addWidget(self.page_ventas)
        self.page_config = QWidget()
        self.page_config.setObjectName(u"page_config")
        self.email_label = QLabel(self.page_config)
        self.email_label.setObjectName(u"email_label")
        self.email_label.setGeometry(QRect(140, 180, 71, 41))
        self.email_label.setFont(font1)
        self.email_label.setStyleSheet(u"color: rgb(0, 170, 255);")
        self.email_entry = QLineEdit(self.page_config)
        self.email_entry.setObjectName(u"email_entry")
        self.email_entry.setGeometry(QRect(230, 180, 301, 41))
        self.email_entry.setFont(font1)
        self.email_entry.setStyleSheet(u"QLineEdit {\n"
"	background-color: qlineargradient(spread:pad, x1:0.522682, y1:1, 						x2:0.516682, y2:0.011, stop:0 rgba(0, 111, 166, 255), stop:1 rgba(0, 170, 			255, 255));\n"
"}\n"
"\n"
"QLineEdit:hover {\n"
"	background-color: qlineargradient(spread:pad, x1:0.528, y1:1, x2:0.522, y2:0.596227, stop:0 rgba(0, 111, 166, 255), stop:1 rgba(0, 170, 255, 255));\n"
"}")
        self.plainTextEdit = QPlainTextEdit(self.page_config)
        self.plainTextEdit.setObjectName(u"plainTextEdit")
        self.plainTextEdit.setGeometry(QRect(40, 30, 681, 121))
        self.plainTextEdit.setFont(font1)
        self.plainTextEdit.setStyleSheet(u"color: rgb(0, 170, 255);\n"
"background-color: rgba(0, 0, 0, 0);")
        self.btn_email = QPushButton(self.page_config)
        self.btn_email.setObjectName(u"btn_email")
        self.btn_email.setGeometry(QRect(550, 180, 101, 41))
        self.btn_email.setFont(font3)
        self.btn_email.setStyleSheet(u"QPushButton {\n"
"	background-color: qlineargradient(spread:pad, x1:0.517, y1:1, x2:0.511, 				y2:0, stop:0 rgba(0, 69, 104, 255), stop:1 rgba(0, 170, 255, 255));\n"
"	color: rgb(0, 0, 0);\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: qlineargradient(spread:pad, x1:0.517, y1:1, x2:0.511, 				y2:0, stop:0 rgba(0, 69, 104, 150), stop:1 rgba(0, 170, 255, 150));\n"
"	color: rgb(255, 255, 255);\n"
"}")
        self.email_status = QLabel(self.page_config)
        self.email_status.setObjectName(u"email_status")
        self.email_status.setGeometry(QRect(100, 300, 591, 41))
        self.email_status.setFont(font1)
        self.email_status.setStyleSheet(u"color: rgb(0, 170, 255);\n"
"background-color: rgba(0, 0, 0, 0);")
        self.plainTextEdit_2 = QPlainTextEdit(self.page_config)
        self.plainTextEdit_2.setObjectName(u"plainTextEdit_2")
        self.plainTextEdit_2.setGeometry(QRect(50, 370, 681, 121))
        self.plainTextEdit_2.setFont(font1)
        self.plainTextEdit_2.setStyleSheet(u"color: rgb(0, 170, 255);\n"
"background-color: rgba(0, 0, 0, 0);")
        self.label_pass = QLabel(self.page_config)
        self.label_pass.setObjectName(u"label_pass")
        self.label_pass.setGeometry(QRect(140, 240, 71, 41))
        self.label_pass.setFont(font1)
        self.label_pass.setStyleSheet(u"color: rgb(0, 170, 255);")
        self.pass_entry = QLineEdit(self.page_config)
        self.pass_entry.setObjectName(u"pass_entry")
        self.pass_entry.setGeometry(QRect(230, 240, 301, 41))
        self.pass_entry.setFont(font1)
        self.pass_entry.setStyleSheet(u"QLineEdit {\n"
"	background-color: qlineargradient(spread:pad, x1:0.522682, y1:1, 						x2:0.516682, y2:0.011, stop:0 rgba(0, 111, 166, 255), stop:1 rgba(0, 170, 			255, 255));\n"
"}\n"
"\n"
"QLineEdit:hover {\n"
"	background-color: qlineargradient(spread:pad, x1:0.528, y1:1, x2:0.522, y2:0.596227, stop:0 rgba(0, 111, 166, 255), stop:1 rgba(0, 170, 255, 255));\n"
"}")
        self.pages_widget.addWidget(self.page_config)
        self.page_historial = QWidget()
        self.page_historial.setObjectName(u"page_historial")
        self.historial_ventas = QTableWidget(self.page_historial)
        self.historial_ventas.setObjectName(u"historial_ventas")
        self.historial_ventas.setGeometry(QRect(500, 360, 241, 211))
        self.historial_ventas.viewport().setProperty("cursor", QCursor(Qt.ArrowCursor))
        self.historial_ventas.setStyleSheet(u"QTableWidget {	\n"
"	background-color: qlineargradient(spread:pad, x1:0.522682, y1:1, x2:0.516682, y2:0.011, stop:0 rgba(0, 111, 166, 255), stop:1 rgba(0, 170, 255, 255));\n"
"	border-radius: 5px;\n"
"	gridline-color: rgb(44, 49, 60);\n"
"	border-bottom: 1px solid rgb(44, 49, 60);\n"
"}\n"
"QTableWidget::item{\n"
"	border-color: rgb(44, 49, 60);\n"
"	padding-left: 5px;\n"
"	padding-right: 5px;\n"
"	gridline-color: rgb(44, 49, 60);\n"
"}\n"
"QTableWidget::item:selected{\n"
"	background-color: rgb(27, 55, 83);\n"
"}\n"
"QScrollBar:horizontal {\n"
"    border: none;\n"
"    background: rgb(52, 59, 72);\n"
"    height: 14px;\n"
"    margin: 0px 21px 0 21px;\n"
"	border-radius: 0px;\n"
"}\n"
" QScrollBar:vertical {\n"
"	border: none;\n"
"    background: rgb(52, 59, 72);\n"
"    width: 14px;\n"
"    margin: 21px 0 21px 0;\n"
"	border-radius: 0px;\n"
" }\n"
"QHeaderView::section{\n"
"	Background-color: qlineargradient(spread:pad, x1:0.522682, y1:1, x2:0.516682, y2:0.011, stop:0 rgba(0, 111, 166, 255), stop:1 rgba(0, "
                        "170, 255, 255));\n"
"	max-width: 30px;\n"
"	border: 1px solid rgb(44, 49, 60);\n"
"	border-style: none;\n"
"    border-bottom: 1px solid rgb(44, 49, 60);\n"
"    border-right: 1px solid rgb(44, 49, 60);\n"
"}\n"
"QTableWidget::horizontalHeader {	\n"
"	background-color:  qlineargradient(spread:pad, x1:0.522682, y1:1, x2:0.516682, y2:0.011, stop:0 rgba(0, 111, 166, 255), stop:1 rgba(0, 170, 255, 255));\n"
"}\n"
"QHeaderView::section:horizontal\n"
"{\n"
"    border: 1px solid rgb(32, 34, 42);\n"
"	background-color: qlineargradient(spread:pad, x1:0.522682, y1:1, x2:0.516682, y2:0.011, stop:0 rgba(0, 111, 166, 255), stop:1 rgba(0, 170, 255, 255));\n"
"	padding: 3px;\n"
"}\n"
"QHeaderView::section:vertical\n"
"{\n"
"    border: 1px solid rgb(44, 49, 60);\n"
"}")
        self.historial_ventas.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.historial_ventas.setDragDropOverwriteMode(False)
        self.historial_ventas.setSelectionMode(QAbstractItemView.SingleSelection)
        self.historial_ventas.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.historial_ventas.horizontalHeader().setDefaultSectionSize(60)
        self.historial_ventas.horizontalHeader().setStretchLastSection(True)
        self.historial_ventas.verticalHeader().setVisible(False)
        self.historial_ventas.verticalHeader().setHighlightSections(False)
        self.calendar = QCalendarWidget(self.page_historial)
        self.calendar.setObjectName(u"calendar")
        self.calendar.setGeometry(QRect(30, 80, 321, 211))
        self.calendar.setFont(font4)
        self.calendar.setStyleSheet(u"QToolButton#qt_calendar_prevmonth,QToolButton#qt_calendar_nextmonth,QToolButton#qt_calendar_monthbutton,QToolButton#qt_calendar_yearbutton{\n"
"border:0px solid #000000;\n"
"border-radius:3px;\n"
"margin:3px 3px 3px 3px;\n"
"padding:3px;\n"
"background-color:rgba(0,0,0,0);\n"
"color: rgb(0, 250, 250);\n"
"}\n"
"\n"
"QToolButton#qt_calendar_prevmonth:hover,QToolButton#qt_calendar_nextmonth:hover,QToolButton#qt_calendar_monthbutton:hover,QToolButton#qt_calendar_yearbutton:hover,QToolButton#qt_calendar_prevmonth:pressed,QToolButton#qt_calendar_nextmonth:pressed,QToolButton#qt_calendar_monthbutton:pressed,QToolButton#qt_calendar_yearbutton:pressed{\n"
"border:1px solid #D8D8D8;\n"
"color: rgb(0, 250, 250);\n"
"}\n"
"\n"
"QCalendarWidget QSpinBox#qt_calendar_yearedit{\n"
"margin:3px 3px 3px 3px;\n"
"padding:0px -7px 0px 0px;\n"
"}\n"
"\n"
"QDateEdit QCalendarWidget QSpinBox#qt_calendar_yearedit,QDateTimeEdit QCalendarWidget QSpinBox#qt_calendar_yearedit{\n"
"padding:0px -2px 0px 0px;\n"
"}\n"
"\n"
"QCalendarWidget "
                        "QToolButton::menu-indicator{\n"
"image:None;\n"
"}\n"
"\n"
"QCalendarWidget QTableView{\n"
"border-width:0px;\n"
"color: rgb(0, 170, 255);\n"
"background-color: rgb(33, 29, 73);\n"
"selection-background-color: rgb(85, 0, 255);\n"
"selection-color: rgb(85, 255, 255);\n"
"}\n"
"\n"
"QCalendarWidget QWidget#qt_calendar_navigationbar{\n"
"border:1px solid #575757;\n"
"border-width:1px 1px 0px 1px;\n"
"background: qlineargradient(spread:pad, x1:1, y1:1, x2:0, y2:0, stop:0 rgba(15, 12, 41, 255), stop:1 rgba(48, 43, 99, 255));\n"
"}")
        self.calendar.setInputMethodHints(Qt.ImhNone)
        self.calendar.setMinimumDate(QDate(2015, 9, 14))
        self.calendar.setMaximumDate(QDate(2115, 12, 31))
        self.calendar.setGridVisible(False)
        self.calendar.setHorizontalHeaderFormat(QCalendarWidget.ShortDayNames)
        self.calendar.setVerticalHeaderFormat(QCalendarWidget.NoVerticalHeader)
        self.calendar.setNavigationBarVisible(True)
        self.calendar.setDateEditEnabled(False)
        self.label = QLabel(self.page_historial)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(510, 320, 151, 31))
        self.label.setFont(font1)
        self.label.setStyleSheet(u"color: rgb(0, 170, 255);")
        self.label_2 = QLabel(self.page_historial)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(30, 320, 151, 31))
        self.label_2.setFont(font1)
        self.label_2.setStyleSheet(u"color: rgb(0, 170, 255);")
        self.historial_deudas = QTableWidget(self.page_historial)
        self.historial_deudas.setObjectName(u"historial_deudas")
        self.historial_deudas.setGeometry(QRect(20, 360, 451, 211))
        self.historial_deudas.setStyleSheet(u"QTableWidget {	\n"
"	background-color: qlineargradient(spread:pad, x1:0.522682, y1:1, x2:0.516682, y2:0.011, stop:0 rgba(0, 111, 166, 255), stop:1 rgba(0, 170, 255, 255));\n"
"	border-radius: 5px;\n"
"	gridline-color: rgb(44, 49, 60);\n"
"	border-bottom: 1px solid rgb(44, 49, 60);\n"
"}\n"
"QTableWidget::item{\n"
"	border-color: rgb(44, 49, 60);\n"
"	padding-left: 5px;\n"
"	padding-right: 5px;\n"
"	gridline-color: rgb(44, 49, 60);\n"
"}\n"
"QTableWidget::item:selected{\n"
"	background-color: rgb(27, 55, 83);\n"
"}\n"
"QScrollBar:horizontal {\n"
"    border: none;\n"
"    background: rgb(52, 59, 72);\n"
"    height: 14px;\n"
"    margin: 0px 21px 0 21px;\n"
"	border-radius: 0px;\n"
"}\n"
" QScrollBar:vertical {\n"
"	border: none;\n"
"    background: rgb(52, 59, 72);\n"
"    width: 14px;\n"
"    margin: 21px 0 21px 0;\n"
"	border-radius: 0px;\n"
" }\n"
"QHeaderView::section{\n"
"	Background-color: qlineargradient(spread:pad, x1:0.522682, y1:1, x2:0.516682, y2:0.011, stop:0 rgba(0, 111, 166, 255), stop:1 rgba(0, "
                        "170, 255, 255));\n"
"	max-width: 30px;\n"
"	border: 1px solid rgb(44, 49, 60);\n"
"	border-style: none;\n"
"    border-bottom: 1px solid rgb(44, 49, 60);\n"
"    border-right: 1px solid rgb(44, 49, 60);\n"
"}\n"
"QTableWidget::horizontalHeader {	\n"
"	background-color:  qlineargradient(spread:pad, x1:0.522682, y1:1, x2:0.516682, y2:0.011, stop:0 rgba(0, 111, 166, 255), stop:1 rgba(0, 170, 255, 255));\n"
"}\n"
"QHeaderView::section:horizontal\n"
"{\n"
"    border: 1px solid rgb(32, 34, 42);\n"
"	background-color: qlineargradient(spread:pad, x1:0.522682, y1:1, x2:0.516682, y2:0.011, stop:0 rgba(0, 111, 166, 255), stop:1 rgba(0, 170, 255, 255));\n"
"	padding: 3px;\n"
"}\n"
"QHeaderView::section:vertical\n"
"{\n"
"    border: 1px solid rgb(44, 49, 60);\n"
"}")
        self.historial_deudas.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.historial_deudas.setDragDropOverwriteMode(True)
        self.historial_deudas.setSelectionMode(QAbstractItemView.SingleSelection)
        self.historial_deudas.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.historial_deudas.horizontalHeader().setDefaultSectionSize(85)
        self.historial_deudas.horizontalHeader().setHighlightSections(False)
        self.historial_deudas.horizontalHeader().setStretchLastSection(True)
        self.historial_deudas.verticalHeader().setVisible(False)
        self.historial_deudas.verticalHeader().setHighlightSections(False)
        self.FechaHoy = QLabel(self.page_historial)
        self.FechaHoy.setObjectName(u"FechaHoy")
        self.FechaHoy.setGeometry(QRect(40, 20, 251, 41))
        font6 = QFont()
        font6.setFamily(u"Leelawadee")
        font6.setPointSize(14)
        self.FechaHoy.setFont(font6)
        self.FechaHoy.setStyleSheet(u"color: rgb(0, 170, 255);")
        self.pruebacalendar = QLabel(self.page_historial)
        self.pruebacalendar.setObjectName(u"pruebacalendar")
        self.pruebacalendar.setGeometry(QRect(390, 20, 341, 41))
        self.pruebacalendar.setFont(font1)
        self.pruebacalendar.setStyleSheet(u"color: rgb(0, 170, 255);")
        self.pages_widget.addWidget(self.page_historial)
        self.page_cuentas = QWidget()
        self.page_cuentas.setObjectName(u"page_cuentas")
        font7 = QFont()
        font7.setPointSize(8)
        self.page_cuentas.setFont(font7)
        self.listaCuentas = QTableWidget(self.page_cuentas)
        self.listaCuentas.setObjectName(u"listaCuentas")
        self.listaCuentas.setGeometry(QRect(30, 130, 231, 191))
        self.listaCuentas.setStyleSheet(u"QTableWidget {	\n"
"	background-color: qlineargradient(spread:pad, x1:0.522682, y1:1, x2:0.516682, y2:0.011, stop:0 rgba(0, 111, 166, 255), stop:1 rgba(0, 170, 255, 255));\n"
"	border-radius: 5px;\n"
"	gridline-color: rgb(44, 49, 60);\n"
"	border-bottom: 1px solid rgb(44, 49, 60);\n"
"}\n"
"QTableWidget::item{\n"
"	border-color: rgb(44, 49, 60);\n"
"	padding-left: 5px;\n"
"	padding-right: 5px;\n"
"	gridline-color: rgb(44, 49, 60);\n"
"}\n"
"QTableWidget::item:selected{\n"
"	background-color: rgb(27, 55, 83);\n"
"}\n"
"QScrollBar:horizontal {\n"
"    border: none;\n"
"    background: rgb(52, 59, 72);\n"
"    height: 14px;\n"
"    margin: 0px 21px 0 21px;\n"
"	border-radius: 0px;\n"
"}\n"
" QScrollBar:vertical {\n"
"	border: none;\n"
"    background: rgb(52, 59, 72);\n"
"    width: 14px;\n"
"    margin: 21px 0 21px 0;\n"
"	border-radius: 0px;\n"
" }\n"
"QHeaderView::section{\n"
"	Background-color: qlineargradient(spread:pad, x1:0.522682, y1:1, x2:0.516682, y2:0.011, stop:0 rgba(0, 111, 166, 255), stop:1 rgba(0, "
                        "170, 255, 255));\n"
"	max-width: 30px;\n"
"	border: 1px solid rgb(44, 49, 60);\n"
"	border-style: none;\n"
"    border-bottom: 1px solid rgb(44, 49, 60);\n"
"    border-right: 1px solid rgb(44, 49, 60);\n"
"}\n"
"QTableWidget::horizontalHeader {	\n"
"	background-color:  qlineargradient(spread:pad, x1:0.522682, y1:1, x2:0.516682, y2:0.011, stop:0 rgba(0, 111, 166, 255), stop:1 rgba(0, 170, 255, 255));\n"
"}\n"
"QHeaderView::section:horizontal\n"
"{\n"
"    border: 1px solid rgb(32, 34, 42);\n"
"	background-color: qlineargradient(spread:pad, x1:0.522682, y1:1, x2:0.516682, y2:0.011, stop:0 rgba(0, 111, 166, 255), stop:1 rgba(0, 170, 255, 255));\n"
"	padding: 3px;\n"
"}\n"
"QHeaderView::section:vertical\n"
"{\n"
"    border: 1px solid rgb(44, 49, 60);\n"
"}")
        self.listaCuentas.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.listaCuentas.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.listaCuentas.setDragDropOverwriteMode(False)
        self.listaCuentas.setSelectionMode(QAbstractItemView.SingleSelection)
        self.listaCuentas.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.listaCuentas.horizontalHeader().setMinimumSectionSize(31)
        self.listaCuentas.horizontalHeader().setDefaultSectionSize(115)
        self.listaCuentas.horizontalHeader().setStretchLastSection(True)
        self.listaCuentas.verticalHeader().setVisible(False)
        self.listaCuentas.verticalHeader().setDefaultSectionSize(35)
        self.listaCuentas.verticalHeader().setHighlightSections(False)
        self.listaDeudas = QTableWidget(self.page_cuentas)
        self.listaDeudas.setObjectName(u"listaDeudas")
        self.listaDeudas.setGeometry(QRect(290, 130, 441, 191))
        self.listaDeudas.setStyleSheet(u"QTableWidget {	\n"
"	background-color: qlineargradient(spread:pad, x1:0.522682, y1:1, x2:0.516682, y2:0.011, stop:0 rgba(0, 111, 166, 255), stop:1 rgba(0, 170, 255, 255));\n"
"	border-radius: 5px;\n"
"	gridline-color: rgb(44, 49, 60);\n"
"	border-bottom: 1px solid rgb(44, 49, 60);\n"
"}\n"
"QTableWidget::item{\n"
"	border-color: rgb(44, 49, 60);\n"
"	padding-left: 5px;\n"
"	padding-right: 5px;\n"
"	gridline-color: rgb(44, 49, 60);\n"
"}\n"
"QTableWidget::item:selected{\n"
"	background-color: rgb(27, 55, 83);\n"
"}\n"
"QScrollBar:horizontal {\n"
"    border: none;\n"
"    background: rgb(52, 59, 72);\n"
"    height: 14px;\n"
"    margin: 0px 21px 0 21px;\n"
"	border-radius: 0px;\n"
"}\n"
" QScrollBar:vertical {\n"
"	border: none;\n"
"    background: rgb(52, 59, 72);\n"
"    width: 14px;\n"
"    margin: 21px 0 21px 0;\n"
"	border-radius: 0px;\n"
" }\n"
"QHeaderView::section{\n"
"	Background-color: qlineargradient(spread:pad, x1:0.522682, y1:1, x2:0.516682, y2:0.011, stop:0 rgba(0, 111, 166, 255), stop:1 rgba(0, "
                        "170, 255, 255));\n"
"	max-width: 30px;\n"
"	border: 1px solid rgb(44, 49, 60);\n"
"	border-style: none;\n"
"    border-bottom: 1px solid rgb(44, 49, 60);\n"
"    border-right: 1px solid rgb(44, 49, 60);\n"
"}\n"
"QTableWidget::horizontalHeader {	\n"
"	background-color:  qlineargradient(spread:pad, x1:0.522682, y1:1, x2:0.516682, y2:0.011, stop:0 rgba(0, 111, 166, 255), stop:1 rgba(0, 170, 255, 255));\n"
"}\n"
"QHeaderView::section:horizontal\n"
"{\n"
"    border: 1px solid rgb(32, 34, 42);\n"
"	background-color: qlineargradient(spread:pad, x1:0.522682, y1:1, x2:0.516682, y2:0.011, stop:0 rgba(0, 111, 166, 255), stop:1 rgba(0, 170, 255, 255));\n"
"	padding: 3px;\n"
"}\n"
"QHeaderView::section:vertical\n"
"{\n"
"    border: 1px solid rgb(44, 49, 60);\n"
"}")
        self.listaDeudas.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.listaDeudas.setDragDropOverwriteMode(False)
        self.listaDeudas.setSelectionMode(QAbstractItemView.SingleSelection)
        self.listaDeudas.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.listaDeudas.horizontalHeader().setDefaultSectionSize(80)
        self.listaDeudas.horizontalHeader().setStretchLastSection(True)
        self.listaDeudas.verticalHeader().setVisible(False)
        self.listaDeudas.verticalHeader().setHighlightSections(False)
        self.label_nuevacuenta = QLabel(self.page_cuentas)
        self.label_nuevacuenta.setObjectName(u"label_nuevacuenta")
        self.label_nuevacuenta.setGeometry(QRect(40, 400, 151, 31))
        self.label_nuevacuenta.setFont(font1)
        self.label_nuevacuenta.setStyleSheet(u"color: rgb(0, 170, 255);")
        self.label_borrarcuenta = QLabel(self.page_cuentas)
        self.label_borrarcuenta.setObjectName(u"label_borrarcuenta")
        self.label_borrarcuenta.setGeometry(QRect(40, 30, 161, 31))
        self.label_borrarcuenta.setFont(font1)
        self.label_borrarcuenta.setStyleSheet(u"color: rgb(0, 170, 255);")
        self.btn_buscarcuenta = QPushButton(self.page_cuentas)
        self.btn_buscarcuenta.setObjectName(u"btn_buscarcuenta")
        self.btn_buscarcuenta.setGeometry(QRect(220, 70, 41, 41))
        self.btn_buscarcuenta.setFont(font3)
        self.btn_buscarcuenta.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_buscarcuenta.setStyleSheet(u"QPushButton {\n"
"	background-color: qlineargradient(spread:pad, x1:0.517, y1:1, x2:0.511, 				y2:0, stop:0 rgba(0, 69, 104, 255), stop:1 rgba(0, 170, 255, 255));\n"
"	color: rgb(0, 0, 0);\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: qlineargradient(spread:pad, x1:0.517, y1:1, x2:0.511, 				y2:0, stop:0 rgba(0, 69, 104, 150), stop:1 rgba(0, 170, 255, 150));\n"
"	color: rgb(255, 255, 255);\n"
"}")
        self.label_agregardeuda = QLabel(self.page_cuentas)
        self.label_agregardeuda.setObjectName(u"label_agregardeuda")
        self.label_agregardeuda.setGeometry(QRect(300, 30, 161, 31))
        self.label_agregardeuda.setFont(font1)
        self.label_agregardeuda.setStyleSheet(u"color: rgb(0, 170, 255);")
        self.btn_agregardeuda = QPushButton(self.page_cuentas)
        self.btn_agregardeuda.setObjectName(u"btn_agregardeuda")
        self.btn_agregardeuda.setGeometry(QRect(690, 70, 41, 41))
        self.btn_agregardeuda.setFont(font3)
        self.btn_agregardeuda.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_agregardeuda.setStyleSheet(u"QPushButton {\n"
"	background-color: qlineargradient(spread:pad, x1:0.517, y1:1, x2:0.511, 				y2:0, stop:0 rgba(0, 69, 104, 255), stop:1 rgba(0, 170, 255, 255));\n"
"	color: rgb(0, 0, 0);\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: qlineargradient(spread:pad, x1:0.517, y1:1, x2:0.511, 				y2:0, stop:0 rgba(0, 69, 104, 150), stop:1 rgba(0, 170, 255, 150));\n"
"	color: rgb(255, 255, 255);\n"
"}")
        self.label_pago = QLabel(self.page_cuentas)
        self.label_pago.setObjectName(u"label_pago")
        self.label_pago.setGeometry(QRect(310, 400, 141, 31))
        self.label_pago.setFont(font1)
        self.label_pago.setStyleSheet(u"color: rgb(0, 170, 255);")
        self.btn_nuevacuenta = QPushButton(self.page_cuentas)
        self.btn_nuevacuenta.setObjectName(u"btn_nuevacuenta")
        self.btn_nuevacuenta.setGeometry(QRect(220, 440, 41, 41))
        self.btn_nuevacuenta.setFont(font3)
        self.btn_nuevacuenta.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_nuevacuenta.setStyleSheet(u"QPushButton {\n"
"	background-color: qlineargradient(spread:pad, x1:0.517, y1:1, x2:0.511, 				y2:0, stop:0 rgba(0, 69, 104, 255), stop:1 rgba(0, 170, 255, 255));\n"
"	color: rgb(0, 0, 0);\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: qlineargradient(spread:pad, x1:0.517, y1:1, x2:0.511, 				y2:0, stop:0 rgba(0, 69, 104, 150), stop:1 rgba(0, 170, 255, 150));\n"
"	color: rgb(255, 255, 255);\n"
"}")
        self.btn_pagodeuda = QPushButton(self.page_cuentas)
        self.btn_pagodeuda.setObjectName(u"btn_pagodeuda")
        self.btn_pagodeuda.setGeometry(QRect(560, 440, 41, 41))
        self.btn_pagodeuda.setFont(font3)
        self.btn_pagodeuda.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_pagodeuda.setStyleSheet(u"QPushButton {\n"
"	background-color: qlineargradient(spread:pad, x1:0.517, y1:1, x2:0.511, 				y2:0, stop:0 rgba(0, 69, 104, 255), stop:1 rgba(0, 170, 255, 255));\n"
"	color: rgb(0, 0, 0);\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: qlineargradient(spread:pad, x1:0.517, y1:1, x2:0.511, 				y2:0, stop:0 rgba(0, 69, 104, 150), stop:1 rgba(0, 170, 255, 150));\n"
"	color: rgb(255, 255, 255);\n"
"}")
        self.btn_borrarcuenta = QPushButton(self.page_cuentas)
        self.btn_borrarcuenta.setObjectName(u"btn_borrarcuenta")
        self.btn_borrarcuenta.setGeometry(QRect(30, 520, 231, 41))
        self.btn_borrarcuenta.setFont(font3)
        self.btn_borrarcuenta.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_borrarcuenta.setStyleSheet(u"QPushButton {\n"
"	background-color: qlineargradient(spread:pad, x1:0.517, y1:1, x2:0.511, 				y2:0, stop:0 rgba(0, 69, 104, 255), stop:1 rgba(0, 170, 255, 255));\n"
"	color: rgb(0, 0, 0);\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: qlineargradient(spread:pad, x1:0.517, y1:1, x2:0.511, 				y2:0, stop:0 rgba(0, 69, 104, 150), stop:1 rgba(0, 170, 255, 150));\n"
"	color: rgb(255, 255, 255);\n"
"}")
        self.buscarcuenta_entry = QLineEdit(self.page_cuentas)
        self.buscarcuenta_entry.setObjectName(u"buscarcuenta_entry")
        self.buscarcuenta_entry.setGeometry(QRect(30, 70, 171, 41))
        self.buscarcuenta_entry.setFont(font1)
        self.buscarcuenta_entry.setStyleSheet(u"QLineEdit {\n"
"	background-color: qlineargradient(spread:pad, x1:0.522682, y1:1, 						x2:0.516682, y2:0.011, stop:0 rgba(0, 111, 166, 255), stop:1 rgba(0, 170, 			255, 255));\n"
"}\n"
"\n"
"QLineEdit:hover {\n"
"	background-color: qlineargradient(spread:pad, x1:0.528, y1:1, x2:0.522, y2:0.596227, stop:0 rgba(0, 111, 166, 255), stop:1 rgba(0, 170, 255, 255));\n"
"}")
        self.montodeuda_entry = QLineEdit(self.page_cuentas)
        self.montodeuda_entry.setObjectName(u"montodeuda_entry")
        self.montodeuda_entry.setGeometry(QRect(290, 70, 181, 41))
        self.montodeuda_entry.setFont(font1)
        self.montodeuda_entry.setStyleSheet(u"QLineEdit {\n"
"	background-color: qlineargradient(spread:pad, x1:0.522682, y1:1, 						x2:0.516682, y2:0.011, stop:0 rgba(0, 111, 166, 255), stop:1 rgba(0, 170, 			255, 255));\n"
"}\n"
"\n"
"QLineEdit:hover {\n"
"	background-color: qlineargradient(spread:pad, x1:0.528, y1:1, x2:0.522, y2:0.596227, stop:0 rgba(0, 111, 166, 255), stop:1 rgba(0, 170, 255, 255));\n"
"}")
        self.pagodeuda_entry = QLineEdit(self.page_cuentas)
        self.pagodeuda_entry.setObjectName(u"pagodeuda_entry")
        self.pagodeuda_entry.setGeometry(QRect(300, 440, 241, 41))
        self.pagodeuda_entry.setFont(font1)
        self.pagodeuda_entry.setStyleSheet(u"QLineEdit {\n"
"	background-color: qlineargradient(spread:pad, x1:0.522682, y1:1, 						x2:0.516682, y2:0.011, stop:0 rgba(0, 111, 166, 255), stop:1 rgba(0, 170, 			255, 255));\n"
"}\n"
"\n"
"QLineEdit:hover {\n"
"	background-color: qlineargradient(spread:pad, x1:0.528, y1:1, x2:0.522, y2:0.596227, stop:0 rgba(0, 111, 166, 255), stop:1 rgba(0, 170, 255, 255));\n"
"}")
        self.nuevacuenta_entry = QLineEdit(self.page_cuentas)
        self.nuevacuenta_entry.setObjectName(u"nuevacuenta_entry")
        self.nuevacuenta_entry.setGeometry(QRect(30, 440, 171, 41))
        self.nuevacuenta_entry.setFont(font1)
        self.nuevacuenta_entry.setStyleSheet(u"QLineEdit {\n"
"	background-color: qlineargradient(spread:pad, x1:0.522682, y1:1, 						x2:0.516682, y2:0.011, stop:0 rgba(0, 111, 166, 255), stop:1 rgba(0, 170, 			255, 255));\n"
"}\n"
"\n"
"QLineEdit:hover {\n"
"	background-color: qlineargradient(spread:pad, x1:0.528, y1:1, x2:0.522, y2:0.596227, stop:0 rgba(0, 111, 166, 255), stop:1 rgba(0, 170, 255, 255));\n"
"}")
        self.status_Cuenta = QLabel(self.page_cuentas)
        self.status_Cuenta.setObjectName(u"status_Cuenta")
        self.status_Cuenta.setGeometry(QRect(40, 340, 411, 41))
        self.status_Cuenta.setFont(font6)
        self.status_Cuenta.setStyleSheet(u"color: rgb(0, 170, 255);")
        self.productodeuda_entry = QLineEdit(self.page_cuentas)
        self.productodeuda_entry.setObjectName(u"productodeuda_entry")
        self.productodeuda_entry.setGeometry(QRect(490, 70, 181, 41))
        self.productodeuda_entry.setFont(font6)
        self.productodeuda_entry.setStyleSheet(u"QLineEdit {\n"
"	background-color: qlineargradient(spread:pad, x1:0.522682, y1:1, 						x2:0.516682, y2:0.011, stop:0 rgba(0, 111, 166, 255), stop:1 rgba(0, 170, 			255, 255));\n"
"}\n"
"\n"
"QLineEdit:hover {\n"
"	background-color: qlineargradient(spread:pad, x1:0.528, y1:1, x2:0.522, y2:0.596227, stop:0 rgba(0, 111, 166, 255), stop:1 rgba(0, 170, 255, 255));\n"
"}")
        self.total_deuda = QLabel(self.page_cuentas)
        self.total_deuda.setObjectName(u"total_deuda")
        self.total_deuda.setGeometry(QRect(470, 340, 261, 41))
        font8 = QFont()
        font8.setFamily(u"Levenim MT")
        font8.setPointSize(18)
        self.total_deuda.setFont(font8)
        self.total_deuda.setStyleSheet(u"color: rgb(0, 170, 255);")
        self.btn_borrardeuda = QPushButton(self.page_cuentas)
        self.btn_borrardeuda.setObjectName(u"btn_borrardeuda")
        self.btn_borrardeuda.setGeometry(QRect(300, 520, 301, 41))
        self.btn_borrardeuda.setFont(font3)
        self.btn_borrardeuda.setStyleSheet(u"QPushButton {\n"
"	background-color: qlineargradient(spread:pad, x1:0.517, y1:1, x2:0.511, 				y2:0, stop:0 rgba(0, 69, 104, 255), stop:1 rgba(0, 170, 255, 255));\n"
"	color: rgb(0, 0, 0);\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: qlineargradient(spread:pad, x1:0.517, y1:1, x2:0.511, 				y2:0, stop:0 rgba(0, 69, 104, 150), stop:1 rgba(0, 170, 255, 150));\n"
"	color: rgb(255, 255, 255);\n"
"}")
        self.pages_widget.addWidget(self.page_cuentas)

        self.verticalLayout_4.addWidget(self.pages_widget)


        self.horizontalLayout_3.addWidget(self.frame_pages)


        self.verticalLayout.addWidget(self.content_bar)

        self.credits_bar = QFrame(self.window)
        self.credits_bar.setObjectName(u"credits_bar")
        self.credits_bar.setMaximumSize(QSize(16777215, 30))
        self.credits_bar.setStyleSheet(u"background-color: none;")
        self.credits_bar.setFrameShape(QFrame.NoFrame)
        self.credits_bar.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.credits_bar)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.frame_label_credits = QFrame(self.credits_bar)
        self.frame_label_credits.setObjectName(u"frame_label_credits")
        self.frame_label_credits.setFrameShape(QFrame.StyledPanel)
        self.frame_label_credits.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_label_credits)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(15, 0, 0, 0)
        self.label_credits = QLabel(self.frame_label_credits)
        self.label_credits.setObjectName(u"label_credits")
        font9 = QFont()
        font9.setFamily(u"Levenim MT")
        self.label_credits.setFont(font9)
        self.label_credits.setStyleSheet(u"color: rgb(128, 102, 168);")

        self.verticalLayout_3.addWidget(self.label_credits)


        self.horizontalLayout_2.addWidget(self.frame_label_credits)

        self.frame_grip = QFrame(self.credits_bar)
        self.frame_grip.setObjectName(u"frame_grip")
        self.frame_grip.setMinimumSize(QSize(30, 30))
        self.frame_grip.setMaximumSize(QSize(30, 30))
        self.frame_grip.setStyleSheet(u"padding: 5px;")
        self.frame_grip.setFrameShape(QFrame.StyledPanel)
        self.frame_grip.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_2.addWidget(self.frame_grip)


        self.verticalLayout.addWidget(self.credits_bar)


        self.window_layout.addWidget(self.window)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.pages_widget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label_title.setText(QCoreApplication.translate("MainWindow", u"Kiosco", None))
        self.label_backup.setText("")
#if QT_CONFIG(tooltip)
        self.btn_close.setToolTip(QCoreApplication.translate("MainWindow", u"Close", None))
#endif // QT_CONFIG(tooltip)
        self.btn_close.setText("")
#if QT_CONFIG(tooltip)
        self.btn_minimize.setToolTip(QCoreApplication.translate("MainWindow", u"Minimize", None))
#endif // QT_CONFIG(tooltip)
        self.btn_minimize.setText("")
        self.btn_ventas.setText(QCoreApplication.translate("MainWindow", u"Ventas", None))
        self.btn_cuentas.setText(QCoreApplication.translate("MainWindow", u"Cuentas", None))
        self.btn_historial.setText(QCoreApplication.translate("MainWindow", u"Historial", None))
        self.btn_configuracion.setText(QCoreApplication.translate("MainWindow", u"Config", None))
        self.label_ventas.setText(QCoreApplication.translate("MainWindow", u"Ventas:", None))
        self.label_ingreso.setText(QCoreApplication.translate("MainWindow", u"Nuevo ingreso:", None))
        self.btn_agregar.setText(QCoreApplication.translate("MainWindow", u"Agregar", None))
        self.btn_borrar.setText(QCoreApplication.translate("MainWindow", u"Borrar", None))
        self.label_dia.setText(QCoreApplication.translate("MainWindow", u" Total del d\u00efa:", None))
        self.ingreso_entry.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Monto", None))
        self.adicional_entry.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Adicional", None))
        self.email_label.setText(QCoreApplication.translate("MainWindow", u" Gmail:", None))
        self.plainTextEdit.setPlainText(QCoreApplication.translate("MainWindow", u"La aplicaci\u00f3n Kiosco, generara un respaldo de modo online de la base de datos en cada inicio. Dicho respaldo se enviara al correo gmail registrado y precisa de una contrase\u00f1a de aplicacion de dispositivos.", None))
        self.btn_email.setText(QCoreApplication.translate("MainWindow", u"Ok", None))
        self.email_status.setText("")
        self.plainTextEdit_2.setPlainText(QCoreApplication.translate("MainWindow", u"Se recomienda crear una nueva direccion de gmail para el uso exclusivo de la app. De esa forma se tendra un registro mas ordendo", None))
        self.label_pass.setText(QCoreApplication.translate("MainWindow", u" Pass:", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"ventas:", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Creditos:", None))
        self.FechaHoy.setText("")
        self.pruebacalendar.setText("")
        self.label_nuevacuenta.setText(QCoreApplication.translate("MainWindow", u"Nueva cuenta:", None))
        self.label_borrarcuenta.setText(QCoreApplication.translate("MainWindow", u"Buscar cuenta:", None))
        self.btn_buscarcuenta.setText(QCoreApplication.translate("MainWindow", u"Ok", None))
        self.label_agregardeuda.setText(QCoreApplication.translate("MainWindow", u"Agregar deuda:", None))
        self.btn_agregardeuda.setText(QCoreApplication.translate("MainWindow", u"Ok", None))
        self.label_pago.setText(QCoreApplication.translate("MainWindow", u"Pago:", None))
        self.btn_nuevacuenta.setText(QCoreApplication.translate("MainWindow", u"Ok", None))
        self.btn_pagodeuda.setText(QCoreApplication.translate("MainWindow", u"Ok", None))
        self.btn_borrarcuenta.setText(QCoreApplication.translate("MainWindow", u"Borrar cuenta", None))
        self.buscarcuenta_entry.setPlaceholderText(QCoreApplication.translate("MainWindow", u" Nombre", None))
        self.montodeuda_entry.setPlaceholderText(QCoreApplication.translate("MainWindow", u" Monto", None))
        self.pagodeuda_entry.setPlaceholderText(QCoreApplication.translate("MainWindow", u" Ingreso", None))
        self.nuevacuenta_entry.setPlaceholderText(QCoreApplication.translate("MainWindow", u" Nombre", None))
        self.status_Cuenta.setText("")
        self.productodeuda_entry.setPlaceholderText(QCoreApplication.translate("MainWindow", u" Detallado", None))
        self.total_deuda.setText("")
        self.btn_borrardeuda.setText(QCoreApplication.translate("MainWindow", u"Borrar registro de deuda", None))
        self.label_credits.setText(QCoreApplication.translate("MainWindow", u"App desarrollada por Nahuel Calcara. \u00a9", None))
    # retranslateUi

