
import requests
# nuitka --standalone --onefile --output-dir=/path/to/output/dir --follow-imports --show-progress --enable-plugin=qt-plugins
from PyQt6.QtCore import QDir
from PyQt6 import QtCore, QtWidgets
import sys
import exifread
# 高德地图坐标转换
gaodeconvert_enable = 1
# 高德API的key
# gaodeapi_key = 这个api自己上高德的网站获取 https://console.amap.com/dev/key/app
# 高德api的网址
gaodeapi_sitehead = "https://restapi.amap.com/v3/assistant/coordinate/convert?locations="

class Ui_MainWindow(object):
    # 设置打开文件的方法
    def __init__(self):
        super().__init__()
    # 以下是设置UI的
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(470, 328)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(parent=self.centralwidget)
        self.label.setGeometry(QtCore.QRect(160, 20, 91, 21))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(40, 100, 54, 16))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(40, 60, 71, 16))
        self.label_3.setObjectName("label_3")

        self.pushButton = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(330, 100, 75, 24))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.select_file)  #选择文件的按钮



        self.label_4 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(340, 60, 54, 16))
        self.label_4.setObjectName("label_4")
        self.label_4.setText("<a href='https://console.amap.com/dev/key/app'>获取API</a>")
        self.label_4.setOpenExternalLinks(True)

        self.label_5 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(340, 7, 140, 50))
        self.label_5.setObjectName("label_5")
        self.label_5.setText("<a href='https://github.com/WinHex89/PictureToYaml'>查看教程👉</a>")
        self.label_5.setOpenExternalLinks(True)


        self.lineEdit = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(120, 60, 201, 20))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit.textChanged.connect(self.update_gaodeapi_key)
        self.gaodeapi_key = self.lineEdit.text() # 获取高德api的变量


        self.lineEdit_2 = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(120, 100, 201, 20))

        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_2.textChanged.connect(self.update_image_url)# 获取图片地址


        self.pushButton_3 = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(330, 140, 75, 81))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_3.clicked.connect(self.print_info)  #生成按钮


        self.textEdit = QtWidgets.QTextEdit(parent=self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(40, 140, 281, 200))
        self.textEdit.setObjectName("textEdit")  # 显示结果的框


        MainWindow.setCentralWidget(self.centralwidget)

        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 470, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def update_gaodeapi_key(self):
        self.gaodeapi_key = self.lineEdit.text()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "PictureToYaml生成照片元数据——©️自权的SPACE"))
        self.label.setText(_translate("MainWindow", "Picture To Yaml "))
        self.label_2.setText(_translate("MainWindow", "照片地址"))
        self.label_3.setText(_translate("MainWindow", "高德地图API"))
        self.pushButton.setText(_translate("MainWindow", "浏览"))
        self.pushButton_3.setText(_translate("MainWindow", "生成"))

    def select_file(self):
        from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QLineEdit, QFileDialog
        file_path, _ = QFileDialog.getOpenFileName(MainWindow, '请选择要转换的照片', '', '符合格式的照片 (*)')
        if file_path:
            self.lineEdit_2.setText(file_path)
            road=self.lineEdit_2.text()
            # image = os.path.basename(road)

            roadurl = road.replace("/", r"\\")
            return roadurl
            # imageob = road.replace("/", "\\")
            # 使用open函数以二进制读取模式打开文件



    def update_image_url(self, text):
        self.imageurl = QDir.toNativeSeparators(text)

    def getLatOrLng(self,refKey, tudeKey):

        road = self.lineEdit_2.text()
        roadurl = road.replace("/", r"\\")
        f = open(roadurl, 'rb')
        tags = exifread.process_file(f)
        if refKey not in tags:
            return None

        # ref = tags[refKey].printable
        LatOrLng = tags[tudeKey].printable[1:-1].replace(" ", "").replace("/", ",").split(",")

        LatOrLng = float(LatOrLng[0]) + float(LatOrLng[1]) / 60 + float(LatOrLng[2]) / float(LatOrLng[3]) / 3600

        if refKey == 'GPS GPSLatitudeRef' and tags[refKey].printable != "N":
            LatOrLng = LatOrLng * (-1)
        if refKey == 'GPS GPSLongitudeRef' and tags[refKey].printable != "E":
            LatOrLng = LatOrLng * (-1)
        return LatOrLng


    def print_info(self):

        import exifread
        road = self.lineEdit_2.text()
        print(road)
        roadurl = road.replace("/", r"\\")
        # 使用open函数以二进制读取模式打开文件
        with open(roadurl, 'rb') as f:
            tags = exifread.process_file(f)

        print(tags)


        self.textEdit.clear()  # 清空文本框内
        self.textEdit.append("---")
        # self.textEdit.append("mapmarker: default")

        self.textEdit.append("date: " + str(tags['EXIF DateTimeOriginal']))
        self.textEdit.append("device: " + str(tags['Image Make']) + " " + str(tags['Image Model']))
        self.textEdit.append("place: ")

        print(2)
        lat = self.getLatOrLng('GPS GPSLatitudeRef', 'GPS GPSLatitude')  # 纬度
        lng = self.getLatOrLng('GPS GPSLongitudeRef', 'GPS GPSLongitude')  # 经度
        print(3)
        gaodeconvert_enable = 1

        gaodeapi_key = self.lineEdit.text()
        # 高德api的网址

        import json
        import urllib.request
        gaodeapi_sitehead = "https://restapi.amap.com/v3/assistant/coordinate/convert?locations="
        gaodeapi_site = gaodeapi_sitehead + str(lng) + "," + str(lat) + "&coordsys=gps&output=json&key=" + gaodeapi_key
        response = requests.get(gaodeapi_site)
        locations = response.json()['locations']
        locations_list = locations.split(',')
        gn = locations_list[1] + ',' + locations_list[0]
        self.textEdit.append('gps: [{},{}]'.format(lat, lng))



        if lat is None or lng is None:
            self.textEdit.clear()  # 清空文本框内容
            self.textEdit.append("Error:No GPS")
            QtWidgets.QMessageBox.warning(self.centralwidget, "错误", "无法读取照片GPS信息")
            return

        if gaodeconvert_enable == 1:
            self.textEdit.append("location: [{}]".format(gn))
        else:
            self.textEdit.append("location: [{},{}]".format(lat, lng))

        self.textEdit.append("---")
        road = self.lineEdit_2.text()
        imageob = road.replace("/", "\\")
        self.textEdit.append('![]('+imageob+ ')')

        print("dz")




if __name__ == '__main__':
   app = QtWidgets.QApplication(sys.argv)
   MainWindow = QtWidgets.QMainWindow() # 创建窗体对象
   ui = Ui_MainWindow() # 创建PyQt设计的窗体对象，classobject变的话，这也要变
   ui.setupUi(MainWindow) # 调用PyQt窗体的方法对窗体对象进行初始化设置
   MainWindow.show() # 显示窗体
   sys.exit(app.exec()) # 程序关闭时退出进程

