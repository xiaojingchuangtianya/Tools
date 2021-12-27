import shutil
import time
import keyboard
import os
import easyocr
from urllib.parse import unquote
import requests
baseDir="C:\\Users\\Administrator\\AppData\\Local\\Temp"

class captureTran():
    def __init__(self,baseDir=None) -> None:
        self.baseDir=baseDir
        self.tranApiUrl="http://fanyi.youdao.com/translate"#翻译接口
        self.korea=""
        self.imgUrl=""
        self.img=""

    #根据路径获取路径下最新的图片
    def getNowPicture(self):
        allFile=os.listdir(baseDir)
        #可以考虑获取最新的文件，此处使用按文件前缀以及时间戳最大的来判断
        #企业微信截图_16401374484339.png
        maxpath=0
        for i in allFile:
            if i.endswith("png"):
                if not os.path.isdir(i):
                    if "企业微信截图_"+str(time.time())[:5] in i:
                        if int(unquote(i,"utf-8")[7:-4])>maxpath:
                            maxpath=int(i[7:-4])
        self.imgUrl=os.path.join(baseDir,"企业微信截图_"+str(maxpath)+".png")
        shutil.copyfile(self.imgUrl,"translate.png")
    #将内容图片翻译识别后，然后将韩文进行输出
    def getBeforeTran(self):
        print("开始检测的文件是：",u"{}".format(self.imgUrl))
        reader=easyocr.Reader(["ko"])
        result=reader.readtext("translate.png")
        for i in result:
            self.korea+=i[1]
        print(self.korea)

    #将内容进行翻译

    def afterTranslate(self):
        data={
            "i":self.korea,
            "from":"ko",
            "to":"zh-CHS",
            "smartresult": "dict",
            "client": "fanyideskweb",
            "salt": "16081210430989",
            "doctype": "json",
            "version": "2.1",
            "keyfrom": "fanyi.web",
            "action": "FY_BY_CLICKBUTTION"
        }
        res=requests.post(self.tranApiUrl,data=data).json()
        print(res['translateResult'][0][0]['tgt'])
        self.korea=""

c=captureTran(baseDir)
def getTran(c):
    c.getNowPicture()
    c.getBeforeTran()
    c.afterTranslate()

keyboard.add_hotkey("f9",getTran,args=(c,))
keyboard.wait()
