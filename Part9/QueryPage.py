import tkinter as tk
import tkinter.messagebox as ms
class QueryNumPage(tk.Frame):
    def __init__(self,master=None,data=[]):
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
            if item[0] ==self.E1.get().strip(" "):
                self.ShowInText(item)
                flag = 1
                break
        if flag == 0:
            ms.showInfo(title='出错',message='输入的编号不存在')
            
    def close(self):
        self.Text.delete(1.0,tk.END)
        self.E1.delete(0,'end')
        self.E1.focus()
    
    def createPage(self):
        tk.Label(self,text='  ').grid(row=0,sticky=tk.W,pady=10)
        tk.Label(self, text='请输入学生编号: ').grid(row=1,columnspan=2,sticky=tk.W,padx=163,pady=10)
        self.E1.grid(row=1, columnspan=2, sticky=tk.E,padx=152,pady=10)
        tk.Label(self,text='  ').grid(row=3,sticky=tk.W,pady=10)
        tk.Button(self, text='显示',width=5,command=self.ShowInfo).grid(row=2,columnspan=2,sticky=tk.W,padx=200,pady=10)
        tk.Button(self, text='清空',width=5,command=self.close).grid(row=2,columnspan=2,sticky=tk.E,padx=200,pady=10)
        self.Text.grid(row=3,columnspan=2,sticky=tk.E)
class QueryNationPage(tk.Frame):
    def __init__(self,master=None,data=[]):
        tk.Frame.__init__(self, master)
        self.root=master
        self.E1=tk.Entry(self)
        self.data=data
        self.Text=tk.Text(self,height=38)
        self.createPage()
        
    def ShowInText(self,ls):
        title=['编号\t','姓名\t','性别\t','年龄\t','民族\t','省份\t','文理\t','爱好\t','分数']
        for t in title:
            self.Text.insert(tk.INSERT,t)
        self.Text.insert(tk.INSERT,'\n')
        for line in ls:
            for i in range(len(line)):
                self.Text.insert(tk.INSERT,line[i])
                self.Text.insert(tk.INSERT,'\t')
            self.Text.insert(tk.INSERT,'\n')
    
    def ShowInfo(self):
        self.Text.delete(1.0,tk.END)
        NationLs=[]
        if self.E1.get()=='':
            ms.showInfo(title='出错',message='输入的民族不能为空')
            return 0
        flag=0
        for item in self.data:
            if item[4] ==self.E1.get().strip(" "):
                NationLs.append(item)
                flag = 1
                break
        if flag == 0:
            ms.showInfo(title='出错',message='输入的民族不存在')
        else:
            self.ShowInText(NationLs)
    def close(self):
        self.Text.delete(1.0,tk.END)
        self.E1.delete(0,'end')
        self.E1.focus()
    def createPage(self):
        tk.Label(self, text='请输入学生民族: ').grid(row=0,columnspan=2,sticky=tk.W,padx=155,pady=10)
        self.E1.grid(row=0, columnspan=2, sticky=tk.E,padx=140,pady=10)
        tk.Button(self, text='显示',width=5,command=self.ShowInfo).grid(row=1,columnspan=2,sticky=tk.W,padx=200,pady=10)
        tk.Button(self, text='清空',width=5,command=self.close).grid(row=1,columnspan=2,sticky=tk.E,padx=200,pady=10)
        self.Text.grid(row=2,columnspan=2,sticky=tk.E)
    
class QueryProvincePage(tk.Frame):
    def __init__(self,master=None,data=[]):
        tk.Frame.__init__(self, master)
        self.root=master
        self.E1=tk.Entry(self)
        self.E2=tk.Entry(self)
        self.data=data
        self.Text=tk.Text(self,height=30)
        self.createPage()
        
    def ShowInText(self,ls):
        title=['编号\t','姓名\t','性别\t','年龄\t','民族\t','省份\t','文理\t','爱好\t','分数']
        for t in title:
            self.Text.insert(tk.INSERT,t)
        self.Text.insert(tk.INSERT,'\n')
        for line in ls:
            for i in range(len(line)):
                self.Text.insert(tk.INSERT,line[i])
                self.Text.insert(tk.INSERT,'\t')
            self.Text.insert(tk.INSERT,'\n')
    
    def ShowInfo(self):
        self.Text.delete(1.0,tk.END)
        ProLs=[]
        if self.E1.get()=='':
            ms.showInfo(title='出错',message='输入的民族不能为空')
            self.E1.focus()
            return 0
        else:
            if self.E2.get()=='':
                ms.showInfo(title='出错',message='输入的科目不能为空')
                self.E2.focus()
                return 0
        flag=0
        for item in self.data:
            if item[5] ==self.E1.get().strip(" ") and item[6]==self.E2.get().strip(" "):
                ProLs.append(item)
                flag = 1
                break
        if flag == 0:
            ms.showInfo(title='出错',message='不存在'+self.E1.get().strip(" ")+'的'+self.E2.get().strip(" ") + '学生')
        else:
            self.ShowInText(ProLs)
    def close(self):
        self.Text.delete(1.0,tk.END)
        self.E1.delete(0,'end')
        self.E2.delete(0,'end')
        self.E1.focus()
    def createPage(self):
        tk.Label(self, text='请输入学生省份: ').grid(row=0,columnspan=3,sticky=tk.W,padx=50,pady=10)
        self.E1.grid(row=0, columnspan=3, sticky=tk.E,padx=60,pady=10)
        tk.Label(self, text='请输入学生科目: ').grid(row=0,columnspan=3,sticky=tk.E,padx=60,pady=10)
        self.E2.grid(row=0, columnspan=3, sticky=tk.E,padx=50,pady=10)
        tk.Button(self, text='显示',width=5,command=self.ShowInfo).grid(row=1,columnspan=3,sticky=tk.W,padx=170,pady=10)
        tk.Button(self, text='清空',width=5,command=self.close).grid(row=1,columnspan=3,sticky=tk.E,padx=170,pady=10)
        self.Text.grid(row=2,columnspan=3,sticky=tk.E)
    