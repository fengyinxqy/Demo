import tkinter as tk
import tkinter.messagebox as ms
class InsertPage(tk.Frame):
    
    def __init__(self,master=None,data=[]):
        tk.Frame.__init__(self, master)
        self.root=master
        self.E1=tk.Entry(self)
        self.E2=tk.Entry(self)
        self.E3=tk.Entry(self)
        self.E4=tk.Entry(self)
        self.E8=tk.Entry(self)
        self.E9=tk.Entry(self)
        nation='''汉族、蒙古族、满族、朝鲜族、赫哲族、达斡尔族、鄂温克族、鄂伦春族、回族、东乡族、土族、撒拉族、保安族、裕固族、维吾尔族、哈萨克族、柯尔克孜族、锡伯族、塔吉克族、乌孜别克族、俄罗斯族、塔塔尔族、藏族、门巴族、珞巴族、羌族、彝族、白族、哈尼族、傣族、僳僳族、佤族、拉祜族、纳西族、景颇族、布朗族、阿昌族、普米族、怒族、德昂族、独龙族、基诺族、苗族、布依族、侗族、水族、仡佬族、壮族、瑶族、仫佬族、毛南族、京族、土家族、黎族、畲族、高山族'''.split('、')
        self.E5=tk.Spinbox(self,values=tuple(nation),width=19)
        province='''河北省、山西省、辽宁省、吉林省、黑龙江省、江苏省、浙江省、安徽省、福建省、江西省、山东省、河南省、湖北省、湖南省、广东省、海南省、四川省、贵州省、云南省 、陕西省 、甘肃省、青海省、台湾省、西藏自治区、广西壮族自治区、内蒙古自治区、宁夏回族自治区、新疆维吾尔自治区、北京市、上海市、天津市、重庆市、香港特别行政区、澳门特别行政区'''.split('、')
        self.var=tk.StringVar()
        self.var.set(province[0])
        kind=('理科','文科','艺体')
        self.E6=tk.OptionMenu(self,self.var,*province)
        self.E7=tk.Spinbox(self, values=kind,width=19)
        self.data=data
        self.createPage()
        
    def SetValue(self):
        info=[]
        if self.E1.get() and len(self.E1.get())==8:
            info.append(str(self.E1.get()))
            if len(self.E2.get()>1):
                info.append(self.E2.get())
                if self.E3.get().strip(' ')=='女' or self.E3.get().strip(' ')=='男':
                    info.append(self.E3.get())
                    if int(self.E4.get())>=10 and int(self.E4.get())<=100:
                        info.append(self.E4.get())
                        info.append(self.E5.get())
                        info.append(self.var.get())
                        info.append(self.E7.get())
                        if self.E8.get()!='':
                            info.append(self.E8.get())
                            if int(self.E9.get())>=0:
                                info.append(self.E9.get())
                            else:
                                ms.showinfo(title='出错',message='分数不能为负数')
                                self.E9.delete(0,'end')
                                self.E9.focus()
                        else:
                            info.append('无')
                    else:
                        ms.showinfo(title='出错',message='年龄非法')
                        self.E4.delete(0,'end')
                        self.E4.focus()
                else:
                    ms.showinfo(title='出错',message='性别只能是男或女')
                    self.E3.delete(0,'end')
                    self.E3.focus()
            else:
                ms.showinfo(title='出错',message='姓名输入有误')
                self.E2.delete(0,'end')
                self.E2.focus()
        else:
            ms.showinfo(title='出错',message='编号是8位的字符串!')
            self.E1.delete(0,'end')
            self.E1.focus()
        self.data.append(info)
    def createPage(self):
        tk.Label(self, text=' ').grid(row=0,sticky=tk.W,pady=10)
        self.E1.grid(row=1,column=1,sticky=tk.E)
        tk.Label(self, text='编号: ').grid(row=1,sticky=tk.W,pady=10)
        self.E2.grid(row=2,column=1,sticky=tk.E)
        tk.Label(self, text='姓名: ').grid(row=2,sticky=tk.W,pady=10)
        self.E3.grid(row=3,column=1,sticky=tk.E)
        tk.Label(self, text='性别: ').grid(row=3,sticky=tk.W,pady=10)
        self.E4.grid(row=4,column=1,sticky=tk.E)
        tk.Label(self, text='年龄: ').grid(row=4,sticky=tk.W,pady=10)
        self.E5.grid(row=5,column=1,sticky=tk.E)
        tk.Label(self, text='民族: ').grid(row=5,sticky=tk.W,pady=10)
        self.E6.grid(row=6,column=1,sticky=tk.E)
        tk.Label(self, text='省份: ').grid(row=6,sticky=tk.W,pady=10)
        self.E7.grid(row=7,column=1,sticky=tk.E)
        tk.Label(self, text='科目: ').grid(row=7,sticky=tk.W,pady=10)
        self.E8.grid(row=8,column=1,sticky=tk.E)
        tk.Label(self, text='爱好: ').grid(row=8,sticky=tk.W,pady=10)
        self.E9.grid(row=9,column=1,sticky=tk.E)
        tk.Label(self, text='分数: ').grid(row=9,sticky=tk.W,pady=10)
        tk.Label(self, text=' ').grid(row=10,sticky=tk.W,pady=10)
        tk.Button(self, text='插入',width=5,command=self.SetValue).grid(row=11,sticky=tk.W,pady=10)
        tk.Button(self, text='取消',width=5,command=self.quit()).grid(row=11,sticky=tk.E,pady=10)
        
class DeletePage(tk.Frame):
    def __init__(self, master=None,data=[]):
        tk.Frame.__init__(self, master)
        self.root=master
        self.E1=tk.Entry(self)
        self.data=data
        self.createPage()
        
    def DeleteInfo(self):
        if self.E1.get()=='':
            ms.showinfo(title='出错',message='输入的编号不能为空')
            return 0
        flag=0
        for item in self.E1.get():
            if item[0]==self.E1.get():
                self.data.remove(item)
                flag=1
                break
        if flag == 0:
            ms.showinfo(title='出错',message='输入的编号不存在')
    def createPage(self):
        tk.Label(self,text='  ').grid(row=0,stick=tk.W,pady=10)
        tk.Label(self, text='请输入要删除的学生编号: ').grid(row=1,columnspan=2,stick=tk.W,pady=10)
        self.E1.grid(row=2, columnspan=2, sticky=tk.E)
        tk.Label(self,text='  ').grid(row=3,stick=tk.W,pady=10)
        tk.Button(self, text='删除',width=5,command=self.DeleteInfo).grid(row=4,sticky=tk.W,pady=10)
        tk.Button(self, text='退出',width=5,command=self.quit()).grid(row=4,column=1,sticky=tk.E)

class ChangePage(tk.Frame):
    def __init__(self, master=None,data=[]):
        tk.Frame.__init__(self, master)
        self.root=master
        self.E1=tk.Entry(self)
        self.data=data
        self.Text=tk.Text(self,height=10)
        self.createPage()
        
    def ShowInText(self,item):
        title=['编号\t','姓名\t','性别\t','年龄\t','民族\t','省份\t','文理\t','爱好\t','分数']
        for t in title:
            self.Text.insert(tk.INSERT,t)
        self.Text.insert(tk.INSERT,'\n')
        for i in range(len(item)):
            self.Text.insert(tk.INSERT,item[i])
            self.Text.insert(tk.INSERT,'\t')
    
    def ShowInfo(self):
        if self.E1.get()=='':
            ms.showInfo(title='出错',message='输入的编号不能为空')
            return 0
        flag=0
        for item in self.data:
            if item[0] ==self.E1.get():
                self.ShowInText(item)
                flag = 1
                break
        if flag == 0:
            ms.showInfo(title='出错',message='输入的编号不存在')
            
    def ChangeInfo(self):
        text_content=(self.Text.get("2.0","end").replace(" ", " ")).split("\t")
        text_content.pop()
        self.data.append(text_content)
    
    def createPage(self):
        tk.Label(self,text='  ').grid(row=0,sticky=tk.W,pady=10)
        tk.Label(self, text='请输入要修改学生编号: ').grid(row=1,column=0,sticky=tk.W,pady=10)
        self.E1.grid(row=1, column=1, sticky=tk.E)
        tk.Label(self,text='  ').grid(row=3,sticky=tk.W,pady=10)
        tk.Button(self, text='显示',width=5,command=self.ShowInfo).grid(row=5,column=0,sticky=tk.W,pady=10)
        tk.Button(self, text='修改',width=5,command=self.ChangeInfo()).grid(row=5,column=1,sticky=tk.E,pady=10)
        tk.Button(self, text='取消',width=5,command=self.quit()).grid(row=5,column=2,sticky=tk.E)
        self.Text.grid(row=6,columnspan=3,sticky=tk.E)
        