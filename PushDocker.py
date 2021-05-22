import sys,pykeyboard
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import os
from PyQt5 import QtCore, QtGui, QtWidgets
import requests


class Push(QWidget):

    def __init__(self, parent=None):
        super(Push, self).__init__(parent)

        # 添加标题
        self.setWindowTitle("docker opeartion files")
        # 添加图标
        self.setWindowIcon(QIcon('w.png'))
        self.resize(1400, 1000)
        self.setWindowOpacity(0.85)

        self.setStyleSheet(
            "color:rgb(248,248,255);font-size:36px;background-color:rgb(54,54,54);border:0.5px groove gray;padding:2px 2px;");
        self.label = QLabel(self)
        self.label.setText("q0o0p")
        self.label.setStyleSheet("color:rgb(108,166,205);border:0px;")

        self.lineEdit = QLineEdit()
        self.btn_push= QPushButton("上传")
        self.btn_pull= QPushButton("下载")
        self.btn_pull.setStyleSheet("color:rgb(108,166,205)")
        self.btn_q0o0p=QPushButton('q0o0p')
        self.btn_start_image=QPushButton('开启kali')
        self.btn_stop_image=QPushButton('停止kali')
        self.btn_see_image=QPushButton('查看所有Image')
        self.btn_del_log=QPushButton('清空日志')

        self.text = QTextEdit()
        # 信号于槽
        self.print = QTextEdit()
        self.print_log = QTextEdit()
        self.print_log.setStyleSheet("color:rgb(180,205,205)")

        self.print_cmd = QTextEdit()
        self.print_cmd.setStyleSheet("color:rgb(144,238,144)")

        self.btn_push.clicked.connect(self.PushFile)
        self.btn_pull.clicked.connect(self.PullFile)
        self.btn_q0o0p.clicked.connect(self.hex)
        self.btn_start_image.clicked.connect(self.StartImage)
        self.btn_stop_image.clicked.connect(self.StopImage)
        self.btn_see_image.clicked.connect(self.SeeImage)
        self.btn_del_log.clicked.connect(self.DelLog)

        # 布局嵌套
        wlayout = QVBoxLayout(self)  # 全局布局
        hlayout = QHBoxLayout()  # 行局部布局
        h1layout = QHBoxLayout()  # 行局部布局
        textView1 = QHBoxLayout()  # 行局部布局
        btnView1 = QVBoxLayout()
        h1layout.addLayout(textView1)
        h1layout.addLayout(btnView1)

        # vlayout = QVBoxLayout() #列局部布局

        hlayout.addWidget(self.label)
        hlayout.addWidget(self.lineEdit)
        hlayout.addWidget(self.btn_push)
        hlayout.addWidget(self.btn_pull)
        hlayout.addWidget(self.btn_q0o0p)


        btnView1.addWidget(self.btn_see_image)
        btnView1.addWidget(self.btn_start_image)
        btnView1.addWidget(self.btn_stop_image)
        btnView1.addWidget(self.btn_del_log)
        textView1.addWidget(self.print_log)
        textView1.addWidget(self.print)

        wlayout.addLayout(hlayout)  # 将局部布局加到全局布局中
        wlayout.addLayout(h1layout)
        self.show()

    def hex(self):
        try:
            code = self.lineEdit.text()
            dec_hex = hex(int(code))
            self.print_log.setPlainText(dec_hex)
        except Exception as e:
            print('please input hex unmber!')

    def SeeImage(self):
        cmd='docker ps -a'
        r=os.popen(cmd)
        text = r.read(1024)
        print(text)
        # self.print_log.setPlainText(text)
        # r.close()

    def StopImage(self):
        linux = '29334d0d66d2'
        stop='docker stop '+linux
        r = os.popen(stop)
        text = r.read(1024)
        print('stop '+text + ' success!')
        self.print_log.append('stop '+text + ' success!')
        r.close()

    def StartImage(self):
        linux = '29334d0d66d2'
        start='docker start '+linux
        r = os.popen(start)
        text = r.read(1024)
        print('start '+text+'success!')
        self.print_log.append('start '+text+' success!')
        r.close()

    def PushFile(self):
        try:
            self.StopImage()
            linux='29334d0d66d2'
            cmd = "docker cp "+self.lineEdit.text()+" "+linux+':/home'
            r = os.popen(cmd)
            text = r.read(1024)
            print(cmd)
            self.print_log.append(text)
            r.close()
            self.StartImage()
        except Exception as e:
            print(e)

    def PullFile(self):
        try:
            self.StopImage()
            linux = '29334d0d66d2'
            cmd = "docker cp "+ linux+ ':/home/'+self.lineEdit.text() +' D:\Android-tools\MagiskModule'
            r = os.popen(cmd)
            text = r.read(1024)
            print(cmd)
            self.print.setPlainText(text)
            r.close()
            self.StartImage()
        except Exception as e:
            print(e)
            self.print.append(text)

    def tet(self):
        url = self.lineEdit.text()
        try:
            rep = requests.get(url)
            rep.encoding = 'utf-8'
            html = rep.text
            # 将抓取的网页源码加入到textEdit中
            # setText()这个函数不能实现
            self.text.setPlainText(html)
        except Exception:
            print('http is null')

    def DelLog(self):
        self.print_log.clear()

    def OpenFilePath(self):
        k = pykeyboard()
        k.press_key(k.alt_key) # 按住alt键
        k.tap_key(k.tab_key) #点击tab键
        k.release_key(k.alt_key) # 松开alt键


if __name__ == "__main__":
    app = QApplication(sys.argv)
    docker_push = Push()
    docker_push.show()
    sys.exit(app.exec())
