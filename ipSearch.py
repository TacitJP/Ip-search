# -*- coding: utf-8 -*-

from PyQt5 import QtCore, QtGui, QtWidgets
import  requests

class Ui_Form(object):
    def __init__(self):
        super(Ui_Form, self).__init__()
        self.setupUi(widget)
        self.lineEdit.returnPressed.connect(self.keyPressEvent)


    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.setFixedSize(394, 310)
        self.plainTextEdit = QtWidgets.QPlainTextEdit(Form)
        self.plainTextEdit.setGeometry(QtCore.QRect(60, 90, 291, 171))
        self.plainTextEdit.setObjectName("plainTextEdit")
        self.horizontalLayoutWidget = QtWidgets.QWidget(Form)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(60, 10, 291, 101))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.lineEdit = QtWidgets.QLineEdit(self.horizontalLayoutWidget)
        self.lineEdit.setObjectName("lineEdit")
        self.horizontalLayout.addWidget(self.lineEdit)
        self.pushButton = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout.addWidget(self.pushButton)

        self.retranslateUi(Form)
        self.pushButton.clicked.connect(self.reMessage)

    def keyPressEvent(self):
        self.reMessage()


    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "IP查询"))
        self.lineEdit.setPlaceholderText(_translate("Form", "请输入IP地址"))
        self.pushButton.setText(_translate("Form", "查询"))

    def reMessage(self):
        _translate = QtCore.QCoreApplication.translate
        gotoURL = 'http://ip.taobao.com/service/getIpInfo.php?ip='
        ipInput = self.lineEdit.text()
        if ipInput=="":
            self.plainTextEdit.setPlainText(_translate("Form", "请输入IP地址进行查询"))
            return 0
        tempURL = gotoURL + ipInput
        #print(tempURL)
        reIP = requests.get(tempURL)
        if reIP.status_code ==200:
            a = reIP.text
            dircTransfor=eval(a[17:-2])
            self.plainTextEdit.setPlainText(_translate("Form","ip:"+dircTransfor['ip']+"\n"
                                                        "国家: " + dircTransfor['country'] +"\n"
                                                        "地区: " + dircTransfor['area'] + "\n"
                                                        "省份: " + dircTransfor['region'] + "\n"
                                                        "城市: " + dircTransfor['city'] + "\n"
                                                        "县: " + dircTransfor['county'] + "\n"
                                                        "运营商: " +dircTransfor['isp'] + "\n"
                                                       ))
        else:
            self.plainTextEdit.setPlainText(_translate("Form", "服务器连接不稳定请重试"))







if __name__ == "__main__":
    import sys,os
    app= QtWidgets.QApplication(sys.argv)
    widget = QtWidgets.QWidget()
    ui = Ui_Form()
    widget.show()
    sys.exit(app.exec_())

