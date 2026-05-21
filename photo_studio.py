from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(632, 650)
        self.comboBox_tables = QtWidgets.QComboBox(Dialog)
        self.comboBox_tables.setGeometry(QtCore.QRect(180, 100, 241, 31))
        self.comboBox_tables.setObjectName("comboBox_tables")
        self.tableWidget_data = QtWidgets.QTableWidget(Dialog)
        self.tableWidget_data.setGeometry(QtCore.QRect(40, 230, 551, 281))
        self.tableWidget_data.setObjectName("tableWidget_data")
        self.tableWidget_data.setColumnCount(0)
        self.tableWidget_data.setRowCount(0)
        self.pushButton_load = QtWidgets.QPushButton(Dialog)
        self.pushButton_load.setGeometry(QtCore.QRect(450, 100, 131, 31))
        self.pushButton_load.setObjectName("pushButton_load")
        self.pushButton_add = QtWidgets.QPushButton(Dialog)
        self.pushButton_add.setGeometry(QtCore.QRect(40, 560, 131, 31))
        self.pushButton_add.setObjectName("pushButton_add")
        self.pushButton_edit = QtWidgets.QPushButton(Dialog)
        self.pushButton_edit.setGeometry(QtCore.QRect(180, 560, 131, 31))
        self.pushButton_edit.setObjectName("pushButton_edit")
        self.pushButton_delete = QtWidgets.QPushButton(Dialog)
        self.pushButton_delete.setGeometry(QtCore.QRect(320, 560, 131, 31))
        self.pushButton_delete.setObjectName("pushButton_delete")
        self.pushButton_refresh = QtWidgets.QPushButton(Dialog)
        self.pushButton_refresh.setGeometry(QtCore.QRect(460, 560, 131, 31))
        self.pushButton_refresh.setObjectName("pushButton_refresh")
        self.pushButton_search = QtWidgets.QPushButton(Dialog)
        self.pushButton_search.setGeometry(QtCore.QRect(450, 170, 131, 31))
        self.pushButton_search.setObjectName("pushButton_search")
        self.lineEdit_search = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_search.setGeometry(QtCore.QRect(180, 170, 241, 31))
        self.lineEdit_search.setObjectName("lineEdit_search")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.pushButton_load.setText(_translate("Dialog", "Загрузить таблицу"))
        self.pushButton_add.setText(_translate("Dialog", "Добавить запись"))
        self.pushButton_edit.setText(_translate("Dialog", "Редактировать запись"))
        self.pushButton_delete.setText(_translate("Dialog", "Удалить запись"))
        self.pushButton_refresh.setText(_translate("Dialog", "Обновить"))
        self.pushButton_search.setText(_translate("Dialog", "Найти"))


