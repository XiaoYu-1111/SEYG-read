# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'modern_1.ui'
##
## Created by: Qt User Interface Compiler version 6.4.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QAbstractSpinBox, QApplication, QFrame, QGraphicsView,
    QGridLayout, QHBoxLayout, QHeaderView, QLabel,
    QLineEdit, QMainWindow, QPlainTextEdit, QPushButton,
    QSizePolicy, QSpacerItem, QSpinBox, QStackedWidget,
    QTableView, QVBoxLayout, QWidget)
import pic_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(600, 400)
        font = QFont()
        font.setFamilies([u"Arial Narrow"])
        font.setPointSize(15)
        MainWindow.setFont(font)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setMinimumSize(QSize(600, 400))
        self.centralwidget.setStyleSheet(u"")
        self.drap_shadow_layout = QVBoxLayout(self.centralwidget)
        self.drap_shadow_layout.setSpacing(0)
        self.drap_shadow_layout.setObjectName(u"drap_shadow_layout")
        self.drap_shadow_layout.setContentsMargins(10, 10, 10, 10)
        self.drap_shadow_frame = QFrame(self.centralwidget)
        self.drap_shadow_frame.setObjectName(u"drap_shadow_frame")
        self.drap_shadow_frame.setMinimumSize(QSize(0, 0))
        self.drap_shadow_frame.setStyleSheet(u"background-color: rgb(103, 104, 99);\n"
"border-radius:8px;")
        self.drap_shadow_frame.setFrameShape(QFrame.NoFrame)
        self.drap_shadow_frame.setFrameShadow(QFrame.Raised)
        self.drap_shadow_frame.setLineWidth(0)
        self.verticalLayout = QVBoxLayout(self.drap_shadow_frame)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.title_bar = QFrame(self.drap_shadow_frame)
        self.title_bar.setObjectName(u"title_bar")
        self.title_bar.setMaximumSize(QSize(16777215, 50))
        self.title_bar.setAutoFillBackground(False)
        self.title_bar.setStyleSheet(u"")
        self.title_bar.setFrameShape(QFrame.NoFrame)
        self.title_bar.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.title_bar)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 10, 0)
        self.frame_title = QFrame(self.title_bar)
        self.frame_title.setObjectName(u"frame_title")
        font1 = QFont()
        font1.setFamilies([u"Agency FB"])
        font1.setPointSize(17)
        self.frame_title.setFont(font1)
        self.frame_title.setStyleSheet(u"")
        self.frame_title.setFrameShape(QFrame.StyledPanel)
        self.frame_title.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_title)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(20, 0, 0, 0)
        self.label_title = QLabel(self.frame_title)
        self.label_title.setObjectName(u"label_title")
        font2 = QFont()
        font2.setFamilies([u"Arial"])
        font2.setPointSize(10)
        font2.setBold(False)
        self.label_title.setFont(font2)
        self.label_title.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"")
        self.label_title.setFrameShape(QFrame.Box)
        self.label_title.setLineWidth(0)

        self.verticalLayout_2.addWidget(self.label_title)


        self.horizontalLayout.addWidget(self.frame_title)

        self.frame_btns = QFrame(self.title_bar)
        self.frame_btns.setObjectName(u"frame_btns")
        self.frame_btns.setMaximumSize(QSize(100, 16777215))
        self.frame_btns.setStyleSheet(u"")
        self.frame_btns.setFrameShape(QFrame.NoFrame)
        self.frame_btns.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_btns)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.btn_maximize = QPushButton(self.frame_btns)
        self.btn_maximize.setObjectName(u"btn_maximize")
        self.btn_maximize.setMinimumSize(QSize(16, 16))
        self.btn_maximize.setMaximumSize(QSize(17, 17))
        self.btn_maximize.setStyleSheet(u"#btn_maximize{border-radius:8px;background-color: rgb(0, 255, 0);}\n"
"#btn_maximize:hover{background-color: rgba(0, 255, 0, 150);\n"
"}")

        self.horizontalLayout_2.addWidget(self.btn_maximize)

        self.btn_minimize = QPushButton(self.frame_btns)
        self.btn_minimize.setObjectName(u"btn_minimize")
        self.btn_minimize.setMinimumSize(QSize(16, 16))
        self.btn_minimize.setMaximumSize(QSize(17, 17))
        self.btn_minimize.setStyleSheet(u"#btn_minimize{border-radius:8px;background-color: rgb(255, 170, 0);\n"
"}\n"
"#btn_minimize:hover{background-color: rgba(255, 170, 0, 150);\n"
"}")

        self.horizontalLayout_2.addWidget(self.btn_minimize)

        self.btn_close = QPushButton(self.frame_btns)
        self.btn_close.setObjectName(u"btn_close")
        self.btn_close.setMinimumSize(QSize(16, 16))
        self.btn_close.setMaximumSize(QSize(17, 17))
        self.btn_close.setStyleSheet(u"#btn_close{border-radius:8px;background-color: rgb(255, 0, 0);\n"
"}\n"
"#btn_close:hover{background-color: rgba(255, 0, 0, 150);\n"
"}")

        self.horizontalLayout_2.addWidget(self.btn_close)


        self.horizontalLayout.addWidget(self.frame_btns)


        self.verticalLayout.addWidget(self.title_bar)

        self.content_bar = QFrame(self.drap_shadow_frame)
        self.content_bar.setObjectName(u"content_bar")
        font3 = QFont()
        font3.setPointSize(11)
        font3.setBold(True)
        self.content_bar.setFont(font3)
        self.content_bar.setStyleSheet(u"")
        self.content_bar.setFrameShape(QFrame.NoFrame)
        self.content_bar.setFrameShadow(QFrame.Raised)
        self.content_bar.setLineWidth(0)
        self.verticalLayout_4 = QVBoxLayout(self.content_bar)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.widget = QWidget(self.content_bar)
        self.widget.setObjectName(u"widget")
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget.sizePolicy().hasHeightForWidth())
        self.widget.setSizePolicy(sizePolicy)
        self.widget.setMinimumSize(QSize(100, 0))
        self.widget.setMaximumSize(QSize(200, 16777215))
        self.widget.setStyleSheet(u"")
        self.verticalLayout_7 = QVBoxLayout(self.widget)
        self.verticalLayout_7.setSpacing(0)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(-1, 0, -1, -1)
        self.Page1_button = QPushButton(self.widget)
        self.Page1_button.setObjectName(u"Page1_button")
        self.Page1_button.setMinimumSize(QSize(0, 40))
        self.Page1_button.setMaximumSize(QSize(100, 16777215))
        self.Page1_button.setStyleSheet(u"#Page1_button{color: rgb(153, 113, 113);background-color: rgb(237, 236, 208);}\n"
"#Page1_button:hover{background-color: rgb(220, 227, 235);}\n"
"#Page1_button:pressed{padding-top:5px;padding-left:5px;}")

        self.verticalLayout_7.addWidget(self.Page1_button)

        self.Page2_button = QPushButton(self.widget)
        self.Page2_button.setObjectName(u"Page2_button")
        self.Page2_button.setMinimumSize(QSize(0, 40))
        self.Page2_button.setMaximumSize(QSize(100, 16777215))
        self.Page2_button.setStyleSheet(u"#Page2_button{color: rgb(153, 113, 113);background-color: rgb(237, 236, 208);}\n"
"#Page2_button:hover{background-color: rgb(220, 227, 235);}\n"
"#Page2_button:pressed{padding-top:5px;padding-left:5px;}\n"
"\n"
"\n"
"\n"
"")

        self.verticalLayout_7.addWidget(self.Page2_button)

        self.Page3_button = QPushButton(self.widget)
        self.Page3_button.setObjectName(u"Page3_button")
        self.Page3_button.setMinimumSize(QSize(0, 40))
        self.Page3_button.setMaximumSize(QSize(100, 16777215))
        self.Page3_button.setStyleSheet(u"#Page3_button{color: rgb(153, 113, 113);background-color: rgb(237, 236, 208);}\n"
"#Page3_button:hover{background-color: rgb(220, 227, 235);}\n"
"#Page3_button:pressed{padding-top:5px;padding-left:5px;}\n"
"\n"
"\n"
"\n"
"")

        self.verticalLayout_7.addWidget(self.Page3_button)


        self.horizontalLayout_4.addWidget(self.widget)

        self.widget_2 = QWidget(self.content_bar)
        self.widget_2.setObjectName(u"widget_2")
        self.verticalLayout_5 = QVBoxLayout(self.widget_2)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.stackedWidget = QStackedWidget(self.widget_2)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.page_1 = QWidget()
        self.page_1.setObjectName(u"page_1")
        self.verticalLayout_6 = QVBoxLayout(self.page_1)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.widget_3 = QWidget(self.page_1)
        self.widget_3.setObjectName(u"widget_3")
        self.widget_3.setStyleSheet(u"background-color: rgb(237, 236, 208);")
        self.verticalLayout_9 = QVBoxLayout(self.widget_3)
        self.verticalLayout_9.setSpacing(0)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_8 = QVBoxLayout()
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.widget_5 = QWidget(self.widget_3)
        self.widget_5.setObjectName(u"widget_5")
        self.widget_5.setMinimumSize(QSize(0, 200))
        self.verticalLayout_10 = QVBoxLayout(self.widget_5)
        self.verticalLayout_10.setSpacing(3)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalLayout_10.setContentsMargins(3, 3, 3, 3)
        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setSpacing(0)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.widget_6 = QWidget(self.widget_5)
        self.widget_6.setObjectName(u"widget_6")
        self.widget_6.setLayoutDirection(Qt.LeftToRight)
        self.horizontalLayout_8 = QHBoxLayout(self.widget_6)
        self.horizontalLayout_8.setSpacing(0)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.widget_8 = QWidget(self.widget_6)
        self.widget_8.setObjectName(u"widget_8")
        self.widget_8.setMaximumSize(QSize(200, 16777215))
        self.widget_8.setStyleSheet(u"background-color: rgb(186, 190, 158);")
        self.verticalLayout_13 = QVBoxLayout(self.widget_8)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.verticalLayout_13.setContentsMargins(9, -1, -1, -1)
        self.verticalLayout_11 = QVBoxLayout()
        self.verticalLayout_11.setSpacing(5)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_11.setContentsMargins(5, 5, 5, 6)
        self.Page1_openfile = QPushButton(self.widget_8)
        self.Page1_openfile.setObjectName(u"Page1_openfile")
        self.Page1_openfile.setMinimumSize(QSize(0, 40))
        self.Page1_openfile.setMaximumSize(QSize(100, 16777215))
        self.Page1_openfile.setStyleSheet(u"#Page1_openfile{color: rgb(237, 236, 208);background-color: rgb(103, 104, 99);border-radius:10px;}\n"
"#Page1_openfile:hover{background-color: rgb(103, 104, 99);}\n"
"#Page1_openfile:pressed{padding-top:5px;padding-left:5px;}\n"
"")

        self.verticalLayout_11.addWidget(self.Page1_openfile)

        self.Page1_savefile = QPushButton(self.widget_8)
        self.Page1_savefile.setObjectName(u"Page1_savefile")
        self.Page1_savefile.setMinimumSize(QSize(0, 40))
        self.Page1_savefile.setMaximumSize(QSize(100, 16777215))
        self.Page1_savefile.setStyleSheet(u"#Page1_savefile{color: rgb(237, 236, 208);background-color: rgb(103, 104, 99);border-radius:10px;}\n"
"#Page1_savefile:hover{background-color: rgb(103, 104, 99);}\n"
"#Page1_savefile:pressed{padding-top:5px;padding-left:5px;}")

        self.verticalLayout_11.addWidget(self.Page1_savefile)

        self.line_path = QLineEdit(self.widget_8)
        self.line_path.setObjectName(u"line_path")
        self.line_path.setMinimumSize(QSize(0, 30))
        self.line_path.setMaximumSize(QSize(200, 16777215))
        self.line_path.setStyleSheet(u"background-color: rgb(103, 104, 99);")

        self.verticalLayout_11.addWidget(self.line_path)

        self.line_path2 = QLineEdit(self.widget_8)
        self.line_path2.setObjectName(u"line_path2")
        self.line_path2.setMinimumSize(QSize(0, 30))
        self.line_path2.setMaximumSize(QSize(200, 16777215))
        self.line_path2.setStyleSheet(u"background-color: rgb(103, 104, 99);")

        self.verticalLayout_11.addWidget(self.line_path2)


        self.verticalLayout_13.addLayout(self.verticalLayout_11)

        self.widget_12 = QWidget(self.widget_8)
        self.widget_12.setObjectName(u"widget_12")
        self.horizontalLayout_9 = QHBoxLayout(self.widget_12)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")

        self.verticalLayout_13.addWidget(self.widget_12)


        self.horizontalLayout_8.addWidget(self.widget_8)

        self.widget_9 = QWidget(self.widget_6)
        self.widget_9.setObjectName(u"widget_9")
        self.widget_9.setStyleSheet(u"background-color: rgb(237, 236, 208);")
        self.verticalLayout_12 = QVBoxLayout(self.widget_9)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.plainTextEdit = QPlainTextEdit(self.widget_9)
        self.plainTextEdit.setObjectName(u"plainTextEdit")
        self.plainTextEdit.setStyleSheet(u"background-color: rgb(178, 182, 151);")

        self.verticalLayout_12.addWidget(self.plainTextEdit)

        self.plainTextEdit_2 = QPlainTextEdit(self.widget_9)
        self.plainTextEdit_2.setObjectName(u"plainTextEdit_2")
        self.plainTextEdit_2.setStyleSheet(u"background-color: rgb(186, 190, 158);")

        self.verticalLayout_12.addWidget(self.plainTextEdit_2)


        self.horizontalLayout_8.addWidget(self.widget_9)


        self.horizontalLayout_7.addWidget(self.widget_6)


        self.verticalLayout_10.addLayout(self.horizontalLayout_7)


        self.verticalLayout_8.addWidget(self.widget_5)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setSpacing(3)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(-1, 3, 3, 3)
        self.Search_con = QLineEdit(self.widget_3)
        self.Search_con.setObjectName(u"Search_con")
        self.Search_con.setMinimumSize(QSize(0, 40))
        self.Search_con.setMaximumSize(QSize(16777215, 16777215))
        font4 = QFont()
        font4.setFamilies([u"Yu Gothic UI Semilight"])
        font4.setPointSize(12)
        font4.setBold(True)
        font4.setUnderline(False)
        self.Search_con.setFont(font4)
        self.Search_con.setStyleSheet(u"background-color: rgb(103, 104, 99);\n"
"border-radius:20px;\n"
"color: rgb(237, 237, 239);")
        self.Search_con.setCursorPosition(5)
        self.Search_con.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.Search_con.setDragEnabled(False)

        self.horizontalLayout_6.addWidget(self.Search_con)

        self.Search_but = QPushButton(self.widget_3)
        self.Search_but.setObjectName(u"Search_but")
        self.Search_but.setMinimumSize(QSize(100, 40))
        self.Search_but.setStyleSheet(u"#Search_but{color: rgb(237, 237, 239);background-color: rgb(103, 104, 99);}\n"
"#Search_but:hover{color: rgb(103, 104, 99);background-color: rgb(214, 182, 171);}\n"
"\n"
"\n"
"#Search_but:pressed{padding-top:5px;padding-left:5px;}")

        self.horizontalLayout_6.addWidget(self.Search_but)


        self.verticalLayout_8.addLayout(self.horizontalLayout_6)


        self.verticalLayout_9.addLayout(self.verticalLayout_8)


        self.verticalLayout_6.addWidget(self.widget_3)

        self.widget_4 = QWidget(self.page_1)
        self.widget_4.setObjectName(u"widget_4")
        self.widget_4.setMinimumSize(QSize(0, 0))
        self.widget_4.setMaximumSize(QSize(16777215, 60))
        self.widget_4.setStyleSheet(u"")
        self.horizontalLayout_5 = QHBoxLayout(self.widget_4)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(20, -1, 20, -1)
        self.Page1_but1 = QPushButton(self.widget_4)
        self.Page1_but1.setObjectName(u"Page1_but1")
        self.Page1_but1.setMinimumSize(QSize(0, 30))
        self.Page1_but1.setMaximumSize(QSize(300, 50))
        self.Page1_but1.setStyleSheet(u"#Page1_but1{color: rgb(153, 113, 113);background-color: rgb(237, 236, 208);}\n"
"#Page1_but1:hover{background-color: rgb(220, 227, 235);}\n"
"#Page1_but1:pressed{padding-top:5px;padding-left:5px;}\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"")

        self.horizontalLayout_5.addWidget(self.Page1_but1)

        self.Page1_but2 = QPushButton(self.widget_4)
        self.Page1_but2.setObjectName(u"Page1_but2")
        self.Page1_but2.setMinimumSize(QSize(0, 30))
        self.Page1_but2.setMaximumSize(QSize(300, 50))
        self.Page1_but2.setStyleSheet(u"#Page1_but2{color: rgb(153, 113, 113);background-color: rgb(237, 236, 208);}\n"
"#Page1_but2:hover{background-color: rgb(220, 227, 235);}\n"
"#Page1_but2:pressed{padding-top:5px;padding-left:5px;}\n"
"\n"
"\n"
"\n"
"\n"
"")

        self.horizontalLayout_5.addWidget(self.Page1_but2)

        self.Page1_but3 = QPushButton(self.widget_4)
        self.Page1_but3.setObjectName(u"Page1_but3")
        self.Page1_but3.setMinimumSize(QSize(0, 30))
        self.Page1_but3.setMaximumSize(QSize(300, 50))
        self.Page1_but3.setStyleSheet(u"#Page1_but3{color: rgb(153, 113, 113);background-color: rgb(237, 236, 208);}\n"
"#Page1_but3:hover{background-color: rgb(220, 227, 235);}\n"
"#Page1_but3:pressed{padding-top:5px;padding-left:5px;}\n"
"")

        self.horizontalLayout_5.addWidget(self.Page1_but3)


        self.verticalLayout_6.addWidget(self.widget_4)

        self.stackedWidget.addWidget(self.page_1)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.verticalLayout_15 = QVBoxLayout(self.page_2)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.verticalLayout_14 = QVBoxLayout()
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.label = QLabel(self.page_2)
        self.label.setObjectName(u"label")
        self.label.setMinimumSize(QSize(0, 50))
        self.label.setMaximumSize(QSize(16777215, 50))
        font5 = QFont()
        font5.setPointSize(13)
        self.label.setFont(font5)
        self.label.setStyleSheet(u"color: rgb(153, 113, 113);background-color: rgb(237, 236, 208);")
        self.label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_14.addWidget(self.label)

        self.widget_7 = QWidget(self.page_2)
        self.widget_7.setObjectName(u"widget_7")
        self.horizontalLayout_10 = QHBoxLayout(self.widget_7)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.tableView = QTableView(self.widget_7)
        self.tableView.setObjectName(u"tableView")
        self.tableView.setStyleSheet(u"background-color: rgb(237, 236, 208);")

        self.horizontalLayout_10.addWidget(self.tableView)

        self.graphicsView_3 = QGraphicsView(self.widget_7)
        self.graphicsView_3.setObjectName(u"graphicsView_3")
        self.graphicsView_3.setStyleSheet(u"background-color: rgb(237, 236, 208);")

        self.horizontalLayout_10.addWidget(self.graphicsView_3)


        self.verticalLayout_14.addWidget(self.widget_7)


        self.verticalLayout_15.addLayout(self.verticalLayout_14)

        self.widget_13 = QWidget(self.page_2)
        self.widget_13.setObjectName(u"widget_13")
        self.horizontalLayout_13 = QHBoxLayout(self.widget_13)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.page2_but1 = QPushButton(self.widget_13)
        self.page2_but1.setObjectName(u"page2_but1")
        self.page2_but1.setMinimumSize(QSize(0, 40))
        self.page2_but1.setMaximumSize(QSize(200, 16777215))
        self.page2_but1.setStyleSheet(u"#page2_but1{color: rgb(153, 113, 113);background-color: rgb(237, 236, 208);}\n"
"#page2_but1:hover{background-color: rgb(220, 227, 235);}\n"
"#page2_but1:pressed{padding-top:5px;padding-left:5px;}")

        self.horizontalLayout_13.addWidget(self.page2_but1)

        self.page2_but2 = QPushButton(self.widget_13)
        self.page2_but2.setObjectName(u"page2_but2")
        self.page2_but2.setMinimumSize(QSize(0, 40))
        self.page2_but2.setMaximumSize(QSize(200, 16777215))
        self.page2_but2.setStyleSheet(u"#page2_but2{color: rgb(153, 113, 113);background-color: rgb(237, 236, 208);}\n"
"#page2_but2:hover{background-color: rgb(220, 227, 235);}\n"
"#page2_but2:pressed{padding-top:5px;padding-left:5px;}")

        self.horizontalLayout_13.addWidget(self.page2_but2)


        self.verticalLayout_15.addWidget(self.widget_13)

        self.stackedWidget.addWidget(self.page_2)
        self.page_3 = QWidget()
        self.page_3.setObjectName(u"page_3")
        self.verticalLayout_17 = QVBoxLayout(self.page_3)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.verticalLayout_16 = QVBoxLayout()
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.label_2 = QLabel(self.page_3)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMinimumSize(QSize(0, 50))
        self.label_2.setMaximumSize(QSize(16777215, 50))
        self.label_2.setFont(font5)
        self.label_2.setStyleSheet(u"color: rgb(153, 113, 113);background-color: rgb(237, 236, 208);")
        self.label_2.setAlignment(Qt.AlignCenter)

        self.verticalLayout_16.addWidget(self.label_2)


        self.verticalLayout_17.addLayout(self.verticalLayout_16)

        self.widget_10 = QWidget(self.page_3)
        self.widget_10.setObjectName(u"widget_10")
        self.verticalLayout_18 = QVBoxLayout(self.widget_10)
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.horizontalLayout_11 = QHBoxLayout()
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.widget_14 = QWidget(self.widget_10)
        self.widget_14.setObjectName(u"widget_14")
        self.widget_14.setMinimumSize(QSize(200, 0))
        self.verticalLayout_20 = QVBoxLayout(self.widget_14)
        self.verticalLayout_20.setSpacing(0)
        self.verticalLayout_20.setObjectName(u"verticalLayout_20")
        self.verticalLayout_20.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_19 = QVBoxLayout()
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.widget_15 = QWidget(self.widget_14)
        self.widget_15.setObjectName(u"widget_15")
        self.widget_15.setMinimumSize(QSize(200, 150))
        self.widget_15.setMaximumSize(QSize(16777215, 150))
        self.widget_15.setStyleSheet(u"background-color: rgb(237, 236, 208);")
        self.verticalLayout_22 = QVBoxLayout(self.widget_15)
        self.verticalLayout_22.setObjectName(u"verticalLayout_22")
        self.widget_17 = QWidget(self.widget_15)
        self.widget_17.setObjectName(u"widget_17")
        self.widget_17.setMaximumSize(QSize(16777215, 20))
        self.verticalLayout_23 = QVBoxLayout(self.widget_17)
        self.verticalLayout_23.setSpacing(0)
        self.verticalLayout_23.setObjectName(u"verticalLayout_23")
        self.verticalLayout_23.setContentsMargins(0, 0, 0, 0)
        self.label_5 = QLabel(self.widget_17)
        self.label_5.setObjectName(u"label_5")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.label_5.sizePolicy().hasHeightForWidth())
        self.label_5.setSizePolicy(sizePolicy1)
        self.label_5.setMinimumSize(QSize(0, 20))
        self.label_5.setMaximumSize(QSize(16777215, 40))

        self.verticalLayout_23.addWidget(self.label_5)


        self.verticalLayout_22.addWidget(self.widget_17)

        self.verticalLayout_21 = QVBoxLayout()
        self.verticalLayout_21.setObjectName(u"verticalLayout_21")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setHorizontalSpacing(0)
        self.gridLayout.setVerticalSpacing(10)
        self.spinBox_columns_end = QSpinBox(self.widget_15)
        self.spinBox_columns_end.setObjectName(u"spinBox_columns_end")
        self.spinBox_columns_end.setMaximum(10000)

        self.gridLayout.addWidget(self.spinBox_columns_end, 1, 2, 1, 1)

        self.label_4 = QLabel(self.widget_15)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout.addWidget(self.label_4, 1, 0, 1, 1)

        self.label_3 = QLabel(self.widget_15)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout.addWidget(self.label_3, 0, 0, 1, 1)

        self.spinBox_row_start = QSpinBox(self.widget_15)
        self.spinBox_row_start.setObjectName(u"spinBox_row_start")
        self.spinBox_row_start.setMaximum(10000)

        self.gridLayout.addWidget(self.spinBox_row_start, 0, 1, 1, 1)

        self.spinBox_columns_start = QSpinBox(self.widget_15)
        self.spinBox_columns_start.setObjectName(u"spinBox_columns_start")
        self.spinBox_columns_start.setMaximum(10000)

        self.gridLayout.addWidget(self.spinBox_columns_start, 1, 1, 1, 1)

        self.spinBox_row_end = QSpinBox(self.widget_15)
        self.spinBox_row_end.setObjectName(u"spinBox_row_end")
        self.spinBox_row_end.setMaximum(10000)
        self.spinBox_row_end.setStepType(QAbstractSpinBox.DefaultStepType)

        self.gridLayout.addWidget(self.spinBox_row_end, 0, 2, 1, 1)


        self.verticalLayout_21.addLayout(self.gridLayout)


        self.verticalLayout_22.addLayout(self.verticalLayout_21)

        self.widget_18 = QWidget(self.widget_15)
        self.widget_18.setObjectName(u"widget_18")
        self.horizontalLayout_14 = QHBoxLayout(self.widget_18)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.horizontalLayout_14.setContentsMargins(0, 0, 0, 0)
        self.Rows_max = QPushButton(self.widget_18)
        self.Rows_max.setObjectName(u"Rows_max")
        self.Rows_max.setMinimumSize(QSize(0, 20))
        self.Rows_max.setStyleSheet(u"#Rows_max{color: rgb(237, 236, 208);background-color: rgb(103, 104, 99);}\n"
"#Rows_max:pressed{padding-top:5px;padding-left:5px;}\n"
"\n"
"")

        self.horizontalLayout_14.addWidget(self.Rows_max)

        self.Clumns_max = QPushButton(self.widget_18)
        self.Clumns_max.setObjectName(u"Clumns_max")
        self.Clumns_max.setMinimumSize(QSize(0, 20))
        self.Clumns_max.setStyleSheet(u"#Clumns_max{color: rgb(237, 236, 208);background-color: rgb(103, 104, 99);}\n"
"#Clumns_max:pressed{padding-top:5px;padding-left:5px;}\n"
"\n"
"")

        self.horizontalLayout_14.addWidget(self.Clumns_max)


        self.verticalLayout_22.addWidget(self.widget_18)


        self.verticalLayout_19.addWidget(self.widget_15)

        self.widget_16 = QWidget(self.widget_14)
        self.widget_16.setObjectName(u"widget_16")
        self.widget_16.setMinimumSize(QSize(300, 0))

        self.verticalLayout_19.addWidget(self.widget_16)


        self.verticalLayout_20.addLayout(self.verticalLayout_19)


        self.horizontalLayout_11.addWidget(self.widget_14)

        self.graphicsView_2 = QGraphicsView(self.widget_10)
        self.graphicsView_2.setObjectName(u"graphicsView_2")
        self.graphicsView_2.setStyleSheet(u"background-color: rgb(237, 236, 208);")

        self.horizontalLayout_11.addWidget(self.graphicsView_2)


        self.verticalLayout_18.addLayout(self.horizontalLayout_11)


        self.verticalLayout_17.addWidget(self.widget_10)

        self.widget_11 = QWidget(self.page_3)
        self.widget_11.setObjectName(u"widget_11")
        self.horizontalLayout_12 = QHBoxLayout(self.widget_11)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.page3_but1 = QPushButton(self.widget_11)
        self.page3_but1.setObjectName(u"page3_but1")
        self.page3_but1.setMinimumSize(QSize(0, 40))
        self.page3_but1.setMaximumSize(QSize(200, 16777215))
        self.page3_but1.setStyleSheet(u"#page3_but1{color: rgb(153, 113, 113);background-color: rgb(237, 236, 208);}\n"
"#page3_but1:hover{background-color: rgb(220, 227, 235);}\n"
"#page3_but1:pressed{padding-top:5px;padding-left:5px;}")

        self.horizontalLayout_12.addWidget(self.page3_but1)

        self.page3_but2 = QPushButton(self.widget_11)
        self.page3_but2.setObjectName(u"page3_but2")
        self.page3_but2.setMinimumSize(QSize(0, 40))
        self.page3_but2.setMaximumSize(QSize(200, 16777215))
        self.page3_but2.setStyleSheet(u"#page3_but2{color: rgb(153, 113, 113);background-color: rgb(237, 236, 208);}\n"
"#page3_but2:hover{background-color: rgb(220, 227, 235);}\n"
"#page3_but2:pressed{padding-top:5px;padding-left:5px;}")

        self.horizontalLayout_12.addWidget(self.page3_but2)


        self.verticalLayout_17.addWidget(self.widget_11)

        self.stackedWidget.addWidget(self.page_3)

        self.verticalLayout_5.addWidget(self.stackedWidget)


        self.horizontalLayout_4.addWidget(self.widget_2)


        self.verticalLayout_4.addLayout(self.horizontalLayout_4)


        self.verticalLayout.addWidget(self.content_bar)

        self.credits_bar = QFrame(self.drap_shadow_frame)
        self.credits_bar.setObjectName(u"credits_bar")
        self.credits_bar.setMinimumSize(QSize(0, 30))
        self.credits_bar.setMaximumSize(QSize(16777215, 30))
        self.credits_bar.setStyleSheet(u"")
        self.credits_bar.setFrameShape(QFrame.StyledPanel)
        self.credits_bar.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.credits_bar)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.frame_label_credits = QFrame(self.credits_bar)
        self.frame_label_credits.setObjectName(u"frame_label_credits")
        self.frame_label_credits.setMaximumSize(QSize(16777215, 50))
        self.frame_label_credits.setStyleSheet(u"")
        self.frame_label_credits.setFrameShape(QFrame.StyledPanel)
        self.frame_label_credits.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_15 = QHBoxLayout(self.frame_label_credits)
        self.horizontalLayout_15.setSpacing(0)
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.horizontalLayout_15.setContentsMargins(20, 0, 0, 0)
        self.label_credits = QLabel(self.frame_label_credits)
        self.label_credits.setObjectName(u"label_credits")
        self.label_credits.setFont(font2)
        self.label_credits.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.horizontalLayout_15.addWidget(self.label_credits)

        self.label_6 = QLabel(self.frame_label_credits)
        self.label_6.setObjectName(u"label_6")
        font6 = QFont()
        font6.setFamilies([u"Bahnschrift Light"])
        font6.setPointSize(11)
        self.label_6.setFont(font6)
        self.label_6.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.horizontalLayout_15.addWidget(self.label_6, 0, Qt.AlignRight)

        self.horizontalSpacer = QSpacerItem(30, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_15.addItem(self.horizontalSpacer)


        self.horizontalLayout_3.addWidget(self.frame_label_credits)

        self.frame_grip = QFrame(self.credits_bar)
        self.frame_grip.setObjectName(u"frame_grip")
        self.frame_grip.setMinimumSize(QSize(30, 30))
        self.frame_grip.setMaximumSize(QSize(60, 30))
        self.frame_grip.setStyleSheet(u"background-color: rgb(103, 104, 99);\n"
"image: url(:/icon/picture/size.png);\n"
"")
        self.frame_grip.setFrameShape(QFrame.StyledPanel)
        self.frame_grip.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_3.addWidget(self.frame_grip)


        self.verticalLayout.addWidget(self.credits_bar)


        self.drap_shadow_layout.addWidget(self.drap_shadow_frame)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.btn_close.clicked.connect(MainWindow.close)
        self.btn_minimize.clicked.connect(MainWindow.showMinimized)

        self.stackedWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label_title.setText(QCoreApplication.translate("MainWindow", u"Python-SEGY-Read !", None))
#if QT_CONFIG(tooltip)
        self.btn_maximize.setToolTip(QCoreApplication.translate("MainWindow", u"Maximize", None))
#endif // QT_CONFIG(tooltip)
        self.btn_maximize.setText("")
        self.btn_minimize.setText("")
        self.btn_close.setText("")
        self.Page1_button.setText(QCoreApplication.translate("MainWindow", u"Page1", None))
        self.Page2_button.setText(QCoreApplication.translate("MainWindow", u"Page2", None))
        self.Page3_button.setText(QCoreApplication.translate("MainWindow", u"Page3", None))
        self.Page1_openfile.setText(QCoreApplication.translate("MainWindow", u"Open_file", None))
        self.Page1_savefile.setText(QCoreApplication.translate("MainWindow", u"Save_file", None))
        self.Search_con.setInputMask("")
        self.Search_con.setText(QCoreApplication.translate("MainWindow", u"SEG-Y", None))
        self.Search_but.setText(QCoreApplication.translate("MainWindow", u"Search", None))
        self.Page1_but1.setText(QCoreApplication.translate("MainWindow", u"Display Data", None))
        self.Page1_but2.setText(QCoreApplication.translate("MainWindow", u"Two", None))
        self.Page1_but3.setText(QCoreApplication.translate("MainWindow", u"Three", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Page2", None))
        self.page2_but1.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.page2_but2.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Page3", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Choice data range ", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Clumns\uff08\u91c7\u6837\u70b9\uff09", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Rows(\u9053\uff09", None))
        self.Rows_max.setText(QCoreApplication.translate("MainWindow", u"Rows_max", None))
        self.Clumns_max.setText(QCoreApplication.translate("MainWindow", u"Clumns_max", None))
        self.page3_but1.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.page3_but2.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.label_credits.setText(QCoreApplication.translate("MainWindow", u"Designed by Python !", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
    # retranslateUi

