#韩语转换脚本使用

>前置条件1
>>
```python
#安装keydorad,easyocr,requests包
pip install keyboard  -i http://pypi.douban.com/simple/
pip install easyocr  -i http://pypi.douban.com/simple/
pip install requests  -i http://pypi.douban.com/simple/
```
>前置条件2

>>korean.pth文件过大，无法上传到github,[传送门](https://github.com/JaidedAI/EasyOCR/releases/download/v1.3/korean_g2.zip)
>>解压后将korean.pth放置到路径下 C:\Users\Administrator\\.EasyOCR\model(这个路径视本地环境修改)
>>还有代码里的basedir是你的temp文件放置的路径，按本地实际路径修改

>使用
>>运行脚本`python  interFace.py`
>>使用微信截图/qq截图/企业微信截图，选中尽可能小的区域
>>粘贴到任意一个企业微信的聊天窗口，按下f9即可，翻译前的韩文以及中文都会展示出来