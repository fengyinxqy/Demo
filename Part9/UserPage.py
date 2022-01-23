from os import write
import tkinter as tk
import tkinter.messagebox as ms
import csv

from matplotlib.pyplot import flag
class UserAddPage(tk.Frame):
    def __init__(self, master=None,username=""):
        tk.Frame.__init__(self, master)
        self.root = master
        self.user_name=username
        self.E1=tk.Entry(self)
        self.E2=tk.Entry(self,show="*")
        self.createPage()
        
    def close(self):
        self.E1.delete(0,'end')
        self.E2.delete(0,'end')
        self.E1.focus()
    
    def SaveAccount(self):
        if self.user_name=="admin":
            flag=0
            with open("python basis\Part9\账号密码.txt","r",encoding="utf-8")as f:
                for line in f:
                    item = line.strip("\n").split(",")
                    if self.E1.get().strip(" ")==item[0]:
                        ms.showinfo(title="错误",message="该账号已存在!")
                        self.close()
                        flag = 1
                        break
            if flag == 0:
                with open("python basis\Part9\账号密码.txt","a",encoding="utf-8")as f:
                    f.write(self.E1.get().strip(" ")+","+self.E2.get().strip(""))
                    ms.showinfo(title="成功",message="已成功添加新用户!")
                    self.close()
        else:
            ms.showinfo(title="错误",message="当前账户没有权限")
            self.close()
                        
    def createPage(self):
        tk.Label(self, text='  ').grid(row=0,sticky=tk.W,pady=10)
        tk.Label(self, text='请输入新用户账号: ').grid(row=1, sticky=tk.W, pady=10)
        self.E1.grid(row=1,column=1,sticky=tk.E)
        tk.Label(self, text='  ').grid(row=2,sticky=tk.W,pady=10)
        tk.Label(self, text='请输入新用户密码: ').grid(row=3, sticky=tk.W, pady=10)
        self.E2.grid(row=3,column=1,sticky=tk.E)
        tk.Label(self, text='  ').grid(row=4,sticky=tk.W,pady=10)
        tk.Button(self, text='保存',width=5,command=self.SaveAccount).grid(row=5, sticky=tk.W,pady=10)
        tk.Button(self, text='取消',width=5,command=self.close).grid(row=5, column=1,sticky=tk.E)
        
class UserChangePage(tk.Frame):
    def __init__(self, master=None,username=""):
        tk.Frame.__init__(self, master)
        self.root = master
        self.user_name=username
        self.E1=tk.Entry(self)
        self.E2=tk.Entry(self,show="*")
        self.E3=tk.Entry(self,show="*")
        self.createPage()
    def close(self):
        self.E1.delete(0,'end')
        self.E2.delete(0,'end')
        self.E3.delete(0,'end')
        self.E1.focus()
        
    def SaveAccount(self):
        with open("python basis\Part9\账号密码.txt","r",encoding="utf-8")as f_r:
            lines = f_r.readlines()
            
        flag=0
        with open("python basis\Part9\账号密码.txt","w",encoding="utf-8")as f_w:
            for line in lines:
                item=line.strip("\n").split(",")
                if item[0]==self.E1.get().strip("  ")and item[1] == self.E2.get().strip(" "):
                    newline=item[0]+","+self.E3.get().strip(" ")
                    flag = 1
                    continue
                f_w.write(line)
            if flag == 0:
                ms.showinfo(title="错误",message="原账户或密码错误!")
                self.close()
            else:
                f_w.write("\n")
                f_w.write(newline)
                
    def createPage(self):
        tk.Label(self, text='  ').grid(row=0,sticky=tk.W,pady=10)
        tk.Label(self, text='请输入原账号: ').grid(row=1, sticky=tk.W, pady=10)
        self.E1.grid(row=1,column=1,sticky=tk.E)
        tk.Label(self, text='请输入原密码: ').grid(row=2, sticky=tk.W, pady=10)
        self.E2.grid(row=2,column=1,sticky=tk.E)
        tk.Label(self, text='请输入新密码: ').grid(row=3, sticky=tk.W, pady=10)
        self.E3.grid(row=3,column=1,sticky=tk.E)
        tk.Label(self, text='  ').grid(row=4,sticky=tk.W,pady=10)
        tk.Button(self, text='修改',width=5,command=self.SaveAccount).grid(row=6, sticky=tk.W,pady=10)
        tk.Button(self, text='取消',width=5,command=self.close).grid(row=6, column=1,sticky=tk.E)
        
class UserDeletePage(tk.Frame):
    def __init__(self, master=None,username=""):
        tk.Frame.__init__(self, master)
        self.root = master
        self.user_name=username
        self.E1=tk.Entry(self)
        self.createPage()
    def close(self):
        self.E1.delete(0,'end')
        self.E1.focus()
    def SaveAccount(self):
        if self.user_name=="admin":
            with open("python basis\Part9\账号密码.txt","r",encoding="utf-8")as f_r:
                lines = f_r.readlines()
            flag=0
            with open("python basis\Part9\账号密码.txt","w",encoding="utf-8")as f:
                for line in f:
                    item = line.strip("\n").split(",")
                    if item[0]==self.E1.get().strip(" "):
                        flag = 1
                        continue
                f_w=write(line)                      
            if flag == 0:
                ms.showinfo(title="错误",message="不存在该账号!")
                self.close()
            else:
                ms.showinfo(title="成功",message="成功删除账号为: "+self.E1.get().strip(" ")+"的用户")
                self.close()
        else:
            ms.showinfo(title="错误",message="当前账户没有权限!")
            self.close()
    def createPage(self):
        tk.Label(self, text='  ').grid(row=0,sticky=tk.W,pady=10)
        tk.Label(self, text='  ').grid(row=2,sticky=tk.W,pady=10)
        tk.Label(self, text='请输入要删除的账号: ').grid(row=2, sticky=tk.W, pady=10)
        self.E1.grid(row=2,column=1,sticky=tk.E)
        tk.Label(self, text='  ').grid(row=3,sticky=tk.W,pady=10)
        tk.Button(self, text='删除',width=5,command=self.SaveAccount).grid(row=4, sticky=tk.W,pady=10)
        tk.Button(self, text='取消',width=5,command=self.close).grid(row=4, column=1,sticky=tk.E)