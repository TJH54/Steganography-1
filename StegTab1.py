#coding:utf-8
__author__ = 'g9752'

import wx
from TailAppend import *

class StegTab1(wx.Panel):
    """
    这里用来填充第一种隐写的功能:
    在文件的尾部直接追加，即“图种”的方式
    """
    def __init__(self,parent):
        wx.Panel.__init__(self,parent)

        self.wholeBox = wx.BoxSizer(wx.VERTICAL)
        srcPicBox = wx.BoxSizer(wx.HORIZONTAL)
        srcFileBox = wx.BoxSizer(wx.HORIZONTAL)
        dstBox = wx.BoxSizer(wx.HORIZONTAL)
        btnBox = wx.BoxSizer(wx.HORIZONTAL)

        """
        添加一行标题内容，用来显示这部分使用的算法
        """
        staticTitle = wx.StaticText(self,id=wx.ID_ANY,label=u"在文件的尾部直接追加信息，即“图种”的方式")
        font = wx.Font(20,wx.ROMAN,wx.SLANT,wx.BOLD)
        staticTitle.SetFont(font)
        staticTitle.SetForegroundColour(wx.RED)

        """
        设置源图片路径，，水平box
        """
        staticPicPath = wx.StaticText(self,id=wx.ID_ANY,label=u"源图片路径:   ")
        self.txtPicPath = wx.TextCtrl(self,id=wx.ID_ANY,value=u"这里记录源图片路径",size=(0,-1))
        btnPicPath = wx.Button(self,id=wx.ID_ANY,label=u"...",size=(40,25))

        srcPicBox.Add(staticPicPath,0,wx.ALL|wx.ALIGN_CENTER,5)
        srcPicBox.Add(self.txtPicPath,1,wx.ALL|wx.ALIGN_CENTER,5)
        srcPicBox.Add(btnPicPath,0,wx.ALL|wx.ALIGN_CENTER,5)

        """
        设置隐写文件路径，，水平box
        """
        staticFilePath = wx.StaticText(self,id=wx.ID_ANY,label=u"隐写文件路径:")
        self.txtFilePath = wx.TextCtrl(self,id=wx.ID_ANY,value=u"这里记录隐写文件路径",size=(0,-1))
        btnFilePath = wx.Button(self,id=wx.ID_ANY,label=u"...",size=(40,25))

        srcFileBox.Add(staticFilePath,0,wx.ALL|wx.ALIGN_CENTER,5)
        srcFileBox.Add(self.txtFilePath,1,wx.ALL|wx.ALIGN_CENTER,5)
        srcFileBox.Add(btnFilePath,0,wx.ALL|wx.ALIGN_CENTER,5)

        """
        设置目标文件路径，，水平box
        """
        staticDstPath = wx.StaticText(self,id=wx.ID_ANY,label=u"目的文件路径:")
        self.txtDstPath = wx.TextCtrl(self,id=wx.ID_ANY,value=u"这里记录目标文件路径",size=(0,-1))
        btnDstPath = wx.Button(self,id=wx.ID_ANY,label=u"...",size=(40,25))

        dstBox.Add(staticDstPath,0,wx.ALL|wx.ALIGN_CENTER,5)
        dstBox.Add(self.txtDstPath,1,wx.ALL|wx.ALIGN_CENTER,5)
        dstBox.Add(btnDstPath,0,wx.ALL|wx.ALIGN_CENTER,5)

        """
        创建 开始 和 清除 按钮
        """
        btnStart = wx.Button(self,id=wx.ID_ANY,label=u"开始")
        btnClear = wx.Button(self,id=wx.ID_ANY,label=u"清除")
        btnBox.Add(btnStart,0,wx.ALL,5)
        btnBox.Add(btnClear,0,wx.ALL,5)


        """
        将各个boxsizer分别放入 wholeBox,
        顺序是: 标题
                ------------------------------
                源图片路径设置box
                ------------------------------
                隐写文件路径设置box
                ------------------------------
                目标文件路径设置box
                ------------------------------
                                  开始    清除
                ------------------------------
        """
        self.wholeBox.Add(staticTitle,0,wx.ALL|wx.EXPAND)
        self.wholeBox.Add(wx.StaticLine(self,), 0, wx.ALL|wx.EXPAND, 5)

        self.wholeBox.Add(srcPicBox,0,wx.ALL|wx.EXPAND,5)
        self.wholeBox.Add(wx.StaticLine(self,), 0, wx.ALL|wx.EXPAND, 5)

        self.wholeBox.Add(srcFileBox,0,wx.ALL|wx.EXPAND,5)
        self.wholeBox.Add(wx.StaticLine(self,), 0, wx.ALL|wx.EXPAND, 5)

        self.wholeBox.Add(dstBox,0,wx.ALL|wx.EXPAND,5)
        self.wholeBox.Add(wx.StaticLine(self,), 0, wx.ALL|wx.EXPAND, 5)

        self.wholeBox.Add(btnBox,0,wx.ALIGN_RIGHT|wx.RIGHT,5)

        """
        绑定按钮事件
        """
        btnPicPath.Bind(wx.EVT_BUTTON,self.ChooseSrcPic)
        btnFilePath.Bind(wx.EVT_BUTTON,self.ChooseSrcFile)
        btnDstPath.Bind(wx.EVT_BUTTON,self.ChooseDstFile)
        btnStart.Bind(wx.EVT_BUTTON,self.OnStart)
        btnClear.Bind(wx.EVT_BUTTON,self.OnClear)
        self.SetSizer(self.wholeBox)

        """
        创建一个图片预览框
        """
        self.Image = wx.StaticBitmap(self,bitmap=wx.EmptyBitmap(400,300))
        self.wholeBox.Add(self.Image,0,wx.ALIGN_CENTER,5)

        """
        使用与背景色颜色相同的图片填充图片预览框
        """
        img = wx.Image(u"./example/background.jpg",wx.BITMAP_TYPE_ANY)
        img = img.Scale(400,300)

        self.Image.SetBitmap(wx.BitmapFromImage(img))
        self.Fit()
        pass

    def ChooseSrcPic(self,event):
        #wx.MessageDialog(self,u"选择图片路径",u"提示",wx.OK).ShowModal()
        wildcard = "All files (*.*)|*.*|" \
                   "BMP files (.bmp)|*.bmp|" \
                   "PNG files (*.png)|*.png|" \
                   "JPG files (*.jpg)|*.jpg"

        fileDialog = wx.FileDialog(self,u"选择源图片文件",os.getcwd(),"",wildcard,wx.FD_OPEN)
        if fileDialog.ShowModal() == wx.ID_OK:
            self.txtPicPath.SetValue(fileDialog.GetPath())

        pass

    def ChooseSrcFile(self,event):
        wildcard = "All files (*.*)|*.*"

        fileDialog = wx.FileDialog(self,u"选择隐写文件",os.getcwd(),"",wildcard,wx.FD_OPEN)
        if fileDialog.ShowModal() == wx.ID_OK:
            self.txtFilePath.SetValue(fileDialog.GetPath())

        pass

    def ChooseDstFile(self,event):
        wildcard = "All files (*.*)|*.*"

        fileDialog = wx.FileDialog(self,u"选择目标文件路径",os.getcwd(),"",wildcard,wx.FD_SAVE| wx.FD_OVERWRITE_PROMPT)
        if fileDialog.ShowModal() == wx.ID_OK:
            self.txtDstPath.SetValue(fileDialog.GetPath())
        pass

    def OnStart(self,event):

        src = self.txtPicPath.GetValue()
        dst = self.txtFilePath.GetValue()
        tofile = self.txtDstPath.GetValue()

        result = TailAppend(src,dst,tofile)

        if result[0] == True:
            wx.MessageBox(result[1],u"提示",wx.OK)

            """
            更改图片预览框的内容
            """
            img = wx.Image(tofile,wx.BITMAP_TYPE_ANY)
            img = img.Scale(400,300)

            self.Image.SetBitmap(wx.BitmapFromImage(img))

            #self.Refresh()         #有的时候会导致结果图片消失

        else:
            wx.MessageBox(result[1],u"提示",wx.OK)

        pass

    def OnClear(self,event):
        self.txtPicPath.SetValue(u"这里记录源图片路径")
        self.txtFilePath.SetValue(u"这里记录隐写文件路径")
        self.txtDstPath.SetValue(u"这里记录目标文件路径")
        img = wx.Image(u"./example/background.jpg",wx.BITMAP_TYPE_ANY)
        img = img.Scale(400,300)
        self.Image.SetBitmap(wx.BitmapFromImage(img))
        self.Refresh()
        pass