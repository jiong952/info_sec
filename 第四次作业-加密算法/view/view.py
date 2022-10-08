import sys
from test import Ui_MainWindow
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5 import QtCore
from algorithm import Caesar
from algorithm import Hill
from algorithm import xor
from algorithm import Playfair
import numpy as np
from PyQt5 import QtCore, QtGui, QtWidgets
import util.fileutils as fileutils

# ckey = None
# pkey = None

class MyMainClass(QMainWindow, Ui_MainWindow):
    ckey = None
    pkey = None
    def __init__(self,parent=None):
        super(MyMainClass,self).__init__(parent)
        self.setupUi(self)
    def encrypt(self):
        # 获取加密方式
        algorithm = self.comboBox.currentText()
        fillChar = self.fillChar.text() # 填充字符或者密钥维度
        beforeText = self.beforeText.text()
        key = self.key_1.toPlainText()
        filePath = self.fillPath.text()
        afterText = self.afterText.text()
        ciphertext = ''
        if algorithm == 'Caesar':
            ciphertext = Caesar.encrypt(beforeText, int(key))
        elif algorithm == 'Hill':
            dim = int(fillChar)
            hill = Hill.Hill(m=dim)
            text = beforeText.upper()
            K = [int(n) for n in key.split(",")]
            K = np.array(K)
            K = K.reshape((dim, dim))
            hill.setKey(K)
            my_list_3, my_list_4 = ",", ","
            pkey = my_list_4.join([my_list_3.join([str(elem) for elem in sub]) for sub in hill.pkey])
            self.key_2.setText(pkey)
            nums = hill.translate(text, "num")
            result = hill.encrypt(nums)
            ciphertext = hill.translate(result, "text")
        elif algorithm == 'Playfair':
            if fillChar != '':
                ciphertext = Playfair.encrypt(beforeText, key, fillChar)
            else:
                ciphertext = Playfair.encrypt(beforeText, key)
        elif algorithm == 'xor':
            ciphertext = xor.encrypt(beforeText, int(key))
        self.afterText.setText(ciphertext)
    def decrypt(self):
        # 获取解密方式
        algorithm = self.comboBox.currentText()
        fillChar = self.fillChar.text()  # 填充字符或者密钥维度
        beforeText = self.beforeText.text()
        key = self.key_1.toPlainText()
        filePath = self.fillPath.text()
        afterText = self.afterText.text()
        plaintext = ''
        if algorithm == 'Caesar':
            plaintext = Caesar.decrypt(beforeText, int(key))
        elif algorithm == 'Hill':
            dim = int(fillChar)
            hill = Hill.Hill(m=dim)
            beforeText = beforeText.upper()
            ciphertext = hill.translate(beforeText, "num")
            # 解密密钥
            K = [int(n) for n in key.split(",")]
            K = np.array(K)
            K = K.reshape((dim, dim))
            hill.setPkey(K)
            nums = hill.decrypt(ciphertext)
            plaintext = hill.translate(nums, "text")
        elif algorithm == 'Playfair':
            if fillChar != '':
                plaintext = Playfair.decrypt(beforeText, key, fillChar)
            else:
                plaintext = Playfair.decrypt(beforeText, key)
        elif algorithm == 'xor':
            plaintext = xor.decrypt(beforeText, int(key))
        self.afterText.setText(plaintext)
    def generateKey(self):
        fillChar = self.fillChar.text() # 填充字符或者密钥维度
        if fillChar != '':
            dim = int(fillChar)
            hill = Hill.Hill(m=dim)
        else:
            hill = Hill.Hill()
        hill.setKey()
        # 加密密钥 解密密钥
        my_list_1, my_list_2 = ",", ","
        ckey = my_list_2.join([my_list_1.join([str(elem) for elem in sub]) for sub in hill.ckey])
        self.key_1.setText(ckey)
    def uploadFile(self):
        directory = QtWidgets.QFileDialog.getOpenFileName(self, "选取文件", "C:/", "All Files (*);;Text Files (*.txt)")
        self.fillPath.setText(directory[0])

    # 加密文件
    def encrypt_file(self):
        # 读文件
        algorithm = self.comboBox.currentText()
        path = self.fillPath.text()
        beforeText = fileutils.read_file(path)
        fillChar = self.fillChar.text()  # 填充字符或者密钥维度
        key = self.key_1.toPlainText()
        ciphertext = ''
        if algorithm == 'Caesar':
            ciphertext = Caesar.encrypt(beforeText, int(key))
        elif algorithm == 'Hill':
            dim = int(fillChar)
            hill = Hill.Hill(m=dim)
            text = beforeText.upper()
            K = [int(n) for n in key.split(",")]
            K = np.array(K)
            K = K.reshape((dim, dim))
            hill.setKey(K)
            my_list_3, my_list_4 = ",", ","
            pkey = my_list_4.join([my_list_3.join([str(elem) for elem in sub]) for sub in hill.pkey])
            self.key_2.setText(pkey)
            nums = hill.translate(text, "num")
            result = hill.encrypt(nums)
            ciphertext = hill.translate(result, "text")
        elif algorithm == 'Playfair':
            if fillChar != '':
                ciphertext = Playfair.encrypt(beforeText, key, fillChar)
            else:
                ciphertext = Playfair.encrypt(beforeText, key)
        elif algorithm == 'xor':
            ciphertext = xor.encrypt(beforeText, int(key))
        # 写文件
        fileutils.write_file(path,ciphertext)
    # 解密文件
    def decrypt_file(self):
        path = self.fillPath.text()
        algorithm = self.comboBox.currentText()
        fillChar = self.fillChar.text()  # 填充字符或者密钥维度
        key = self.key_1.toPlainText()
        beforeText = fileutils.read_file(path)
        plaintext = ''
        if algorithm == 'Caesar':
            plaintext = Caesar.decrypt(beforeText, int(key))
        elif algorithm == 'Hill':
            dim = int(fillChar)
            hill = Hill.Hill(m=dim)
            beforeText = beforeText.upper()
            ciphertext = hill.translate(beforeText, "num")
            # 解密密钥
            K = [int(n) for n in key.split(",")]
            K = np.array(K)
            K = K.reshape((dim, dim))
            hill.setPkey(K)
            nums = hill.decrypt(ciphertext)
            plaintext = hill.translate(nums, "text")
        elif algorithm == 'Playfair':
            if fillChar != '':
                plaintext = Playfair.decrypt(beforeText, key, fillChar)
            else:
                plaintext = Playfair.decrypt(beforeText, key)
        elif algorithm == 'xor':
            plaintext = xor.decrypt(beforeText, int(key))
        # 写文件
        fileutils.write_file(path, plaintext)


if __name__ == '__main__':
    QtCore.QCoreApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling)
    app = QApplication(sys.argv)
    ui = MyMainClass()
    ui.show()
    sys.exit(app.exec())