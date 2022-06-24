#主要功能
import time
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from baseUi import Ui_MainWindow
import win32gui
import win32con
from functools import partial
# 根据传进来的一个句柄id来解决问题
ondealList=[]

class windowHandle:
    # 窗口类,处理窗口的句柄以及选中问题
    def __init__(self,onDeal) -> None:
        self.winList=[]#所有句柄id
        self.winTitle={}
        self.onDealId=onDeal#正在处理的进程,用于关闭和其他操作.

    # 获取全部的窗口句柄,记录在winList里
    def getAllHandles(self):
        win32gui.EnumWindows(self.windowCallback,self.winList)
        # print(self.winList)

    # 根据句柄去获取到对应的标题
    def getTitleForHandle(self):
        for i in self.winList:
            titleName=win32gui.GetWindowText(i)
            if "微信" in titleName or "Chrome" in titleName:
                self.winTitle[i] = titleName
            continue
        print(self.winTitle)
    
    #置顶操作   
    def toTop(self):
        print(self.winTitle[self.onDealId])
        win32gui.ShowWindow(self.onDealId,win32con.SW_MAXIMIZE)#SW_MAXIMIZE ,SW_NORMAL,SW_SHOWDEFAULT

    def closeProcess(self):
        win32gui.CloseWindow(self.onDealId)#这里只是关闭窗口
        #关闭进程的话就使用os执行对应命令行

    # 回调函数
    def windowCallback(self,hWnd, param):
        param.append(hWnd)

#测试用的简单模块
def change(ui):
    ui.label.setText("test")

def comboBoxChange(dealId):
    h.onDealId=dealId#修改当前正在处理的进程
    print("当前被选中的进程是:%s"%h.onDealId)

h=windowHandle(33333)
h.getAllHandles()
h.getTitleForHandle()
# h.toTop()
# h.closeProcess()

if __name__=="__main__":
    app = QApplication(sys.argv)
    MainWindow = QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    dictList=h.winTitle.items()#将字典转换为列表
    startFlag=0#用于作第一个时候进行一个默认选择
    for i in dictList:
        if not startFlag:
            comboBoxChange(i[0])
            startFlag=1
            print("1")
        print(i[1],i[0])
        ui.comboBox.addItem(i[1][:10])#传入字符串和进程id

    #添加对应的触发事件
    # ui.comboBox.Ac.connect(partial(comboBoxChange,ui.comboBox.currentData()))#下拉框勾选的触发事件
    ui.comboBox.activated.connect(partial(comboBoxChange,ui.comboBox.currentData))
    ui.pushButton.clicked.connect(partial(change,ui))#按钮触发事件


    sys.exit(app.exec_())
