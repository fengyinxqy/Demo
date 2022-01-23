import tkinter as tk
import tkinter.messagebox as ms
import MainPage as mp
class LoginPage(object):
    def __init__(self,master=None):
        self.root=master
        self.root.geometry('%dx%d'%(500,300))
        self.username=tk.StringVar()
        self.password = tk.StringVar()
        self.E1=tk.Entry(self.root)
        self.createPage()
    
    def loginCheck(self):
        name=self.username.get()
        password = self.password.get()
        if self.isLegalUser(name,password):
            self.page.destroy()
            mp.MainPage(self.root,name)
        else:
            ms.showinfo(title='错误',message='账号或密码错误!')
            self.username.set("")
            self.password.set("")
    def isLegalUser(self, name, password):
        with open('python basis\Part9\账号密码.txt',"r",encoding="utf-8")as f:
            for line in f.readlines():
                info=line[:-1].split(",")
                if len(info)<2:
                    break
                if info[0].strip()==name and info[1].strip() ==password:
                    f.close()
                    return True
        return False
    
    def createPage(self):
        self.page=tk.Frame(self.root)
        self.page.pack()
        tk.Label(self.page, text="  ").grid(row=0,sticky=tk.W,pady=10)
        tk.Label(self.page, text="高考信息管理系统",font=('Helvetica 20 bold'),background="white").grid(row=1, columnspan=2,sticky=tk.E+tk.W)
        tk.Label(self.page, text="  ").grid(row=1,sticky=tk.W,pady=10)
        tk.Label(self.page, text="账号: ").grid(row=3, sticky=tk.E, pady=10)
        tk.Entry(self.page, textvariable=self.username).grid(row=3,column=1,sticky=tk.W)
        tk.Label(self.page, text="密码: ").grid(row=4, sticky=tk.E, pady=10)
        tk.Entry(self.page, textvariable=self.password,show="*").grid(row=4,column=1,sticky=tk.W)
        tk.Button(self.page, text="登录",width=5,command=self.loginCheck).grid(row=5, columnspan=2, sticky=tk.W,padx=50,pady=10)
        tk.Button(self.page, text="退出",width=5,command=self.page.quit).grid(row=5, columnspan=2, sticky=tk.E,padx=50,pady=10)