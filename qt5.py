import sys
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import os

from PyQt5 import QtCore, QtGui, QtWidgets
import requests

class MyTest(QWidget):

    def __init__(self, parent=None):
        super(MyTest, self).__init__(parent)

         #添加标题
        self.setWindowTitle("q0o0p-tools")
        #添加图标
        self.setWindowIcon(QIcon('w.png'))
        self.resize(700, 500)
        self.setObjectName("MainWindow")
        self.setWindowOpacity(0.85)
        # self.setStyleSheet("#MainWindow{border-image:url(w.png);}")
        # 设置窗口透明度
        self.setStyleSheet ("color:rgb(248,248,255);font-size:16px;background-color:rgb(54,54,54);border:0.5px groove gray;border-radius:8px;padding:2px 2px;");
        # self.setStyleSheet("#MainWindow{background-color:black}")
                

         # 设置窗口背景透明        
        # self.setAttribute(QtCore.Qt.WA_TranslucentBackground)

        self.label = QLabel(self)
        self.label.setText("q0o0p")
        self.label.setStyleSheet("color:rgb(108,166,205);border:0px;")
        self.lineEdit = QLineEdit()
        self.appPackage = QLineEdit() 
        #self.lineEdit.setText("http://www.baidu.com")
        self.btn_begin = QPushButton("开始")
        self.btn_q0o0p = QPushButton("q0o0p")
        self.btn_hex = QPushButton("dec to hex")
        self.btn_decimal = QPushButton("hex to dec") #十六进制转十进制
        self.btn_unicode= QPushButton("unicode")
        self.btn_startApp= QPushButton("start app")
        self.btn_readActivity= QPushButton("activity")
        self.btn_package= QPushButton("all package")
        self.btn_package.setStyleSheet("color:rgb(108,166,205)")
        self.text = QTextEdit()
        #信号于槽
        self.print = QTextEdit()
        self.print_activity = QTextEdit()
        self.print_activity.setStyleSheet("color:rgb(180,205,205)")

        self.print_cmd = QTextEdit()
        self.print_cmd.setStyleSheet("color:rgb(144,238,144)")

        self.btn_begin.clicked.connect(self.getstr)
        self.btn_q0o0p.clicked.connect(self.getstr)
        self.btn_unicode.clicked.connect(self.unicode)
        self.btn_hex.clicked.connect(self.hex)
        self.btn_decimal.clicked.connect(self.decimal)
        self.btn_readActivity.clicked.connect(self.read_activity)
        self.btn_package.clicked.connect(self.package)
        self.btn_startApp.clicked.connect(self.startApp)
        #布局嵌套
        wlayout = QVBoxLayout(self) #全局布局
        hlayout = QHBoxLayout() #行局部布局
        textView1 = QHBoxLayout() #行局部布局
        textView2 = QHBoxLayout() #行局部布局
        appLine = QHBoxLayout() #行局部布局
        btn1 = QHBoxLayout() #行局部布局
        # vlayout = QVBoxLayout() #列局部布局
        layout3 = QHBoxLayout()

        hlayout.addWidget(self.label)
        hlayout.addWidget(self.lineEdit)
        hlayout.addWidget(self.btn_begin)
        hlayout.addWidget(self.btn_q0o0p)

        layout3.addWidget(self.btn_unicode)
        layout3.addWidget(self.btn_hex)
        layout3.addWidget(self.btn_decimal)

        appLine.addWidget(self.appPackage)
        appLine.addWidget(self.btn_startApp)

        textView1.addWidget(self.text)
        textView1.addWidget(self.print)
        # textView1.addWidget(self.log)

        btn1.addWidget(self.btn_readActivity)
        btn1.addWidget(self.btn_package)

        textView2.addWidget(self.print_activity)
        textView2.addWidget(self.print_cmd)

        wlayout.addLayout(hlayout) #将局部布局加到全局布局中
        wlayout.addLayout(layout3) 
        wlayout.addLayout(textView1)
        wlayout.addLayout(btn1)
        wlayout.addLayout(appLine)
        wlayout.addLayout(textView2)


        self.show()


    def hex(self):
        try:
            code=self.lineEdit.text()
            dec_hex=hex(int(code))
            self.text.setPlainText(dec_hex)
        except Exception as e:
            print('please input hex unmber!')
    def startApp(self):
        try:
            app=self.appPackage.text()
            cmd = "adb shell am start -n" +app
            r = os.popen(cmd)  
            text = r.read(1024)  
            self.print.setPlainText(text)
            r.close()    
        except Exception as e:
            print(e)
            self.log.setText(e)

    def package(self):
        try:
            cmd = "adb shell  pm list packages" 
            r = os.popen(cmd)  
            text = r.read(1024)  
            self.print_cmd.setPlainText(text)
            r.close()    
        except Exception as e:
            print(e)
    def read_activity(self):
        try:
            cmd = "adb shell dumpsys activity top " 
            r = os.popen(cmd)  
            text = r.read(1024)  
            self.print_activity.setPlainText(text)
            r.close()    
        except Exception as e:
            print(e)

    def decimal(self):
        try:
            code=self.lineEdit.text()
            hex_dec=int(code,16)
            self.print.setPlainText(str(hex_dec))
        except Exception as e:
            print(e)        

    def unicode(self):
        try:
            code=self.lineEdit.text()
            # chinese_unicode=code.encode('unicode_escape')
            chinese_unicode=code.encode('unicode_escape')
            self.print.setPlainText(str(chinese_unicode))
            print(chinese_unicode)
        except Exception as e:
            print()
            raise e


    #槽函数
    def get(self):
        url = self.lineEdit.text()
        rep = requests.get(url)
        rep.encoding = 'utf-8'
        html = rep.text
        #将抓取的网页源码加入到textEdit中
        #setText()这个函数不能实现
        self.text.setPlainText(html)

        #槽函数
    def getstr(self):
        url = self.lineEdit.text()
        try:
            rep = requests.get(url)
            rep.encoding = 'utf-8'
            html = rep.text
            #将抓取的网页源码加入到textEdit中
            #setText()这个函数不能实现
            self.text.setPlainText(html)
        except Exception :
            print('http is null')
        



if __name__ =="__main__":
    app = QApplication(sys.argv)
    demo = MyTest()
    demo.show()
    sys.exit(app.exec())
