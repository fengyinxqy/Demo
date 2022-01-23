import tkinter as tk
import tkinter.messagebox as ms
class SortAllPage(tk.Frame):
    def __init__(self,master=None,data=[]):
        tk.Frame.__init__(self, master)
        self.root=master
        self.data=data
        self.Text=tk.Text(self,height=41)
        self.createPage()
        
    def ShowInText(self,sortls):
        title=['编号\t','姓名\t','性别\t','年龄\t','民族\t','省份\t','文理\t','爱好\t','分数']
        for t in title:
            self.Text.insert(tk.INSERT,t)
        self.Text.insert(tk.INSERT,'\n')
        for line in sortls:
            for i in range(len(line)):
                self.Text.insert(tk.INSERT,line[i])
                self.Text.insert(tk.INSERT,'\t')
            self.Text.insert(tk.INSERT,'\n')
    
    def ShowInfoAsc(self):
        self.Text.delete(1.0,tk.END)
        if len(self.data)==0:
            ms.showinfo(title='出错',message='没有学生数据')
            return 0
        else:
            AfterSort=sorted(self.data,key=(lambda x:x[8]))
        self.ShowInText(AfterSort)
            
    def ShowInfoDes(self):
        self.Text.delete(1.0,tk.END)
        if len(self.data)==0:
            ms.showinfo(title='出错',message='没有学生数据')
            return 0
        else:
            AfterSort=sorted(self.data,key=(lambda x:x[8]),reverse=True)
        self.ShowInText(AfterSort) 
            
    def close(self):
        self.Text.delete(1.0,tk.END)
    
    def createPage(self):
        tk.Button(self,text='升序',width=5,command=self.ShowInfoAsc).grid(row=0,columnspan=2,sticky=tk.W,padx=100,pady=10)
        tk.Button(self,text='降序',width=5,command=self.ShowInfoDes).grid(row=0,columnspan=2,sticky=tk.W,padx=250,pady=10)
        tk.Button(self,text='清空',width=5,command=self.close).grid(row=0,columnspan=2,sticky=tk.E,padx=100,pady=10)
        self.Text.grid(row=1,columnspan=2,sticky=tk.E)
        
class SortProPage(tk.Frame):
    def __init__(self,master=None,data=[]):
        tk.Frame.__init__(self, master)
        self.root=master
        self.E1=tk.Entry(self)
        self.data=data
        self.Text=tk.Text(self,height=38)
        self.createPage()
        
    def ShowInText(self,sortls):
        title=['编号\t','姓名\t','性别\t','年龄\t','民族\t','省份\t','文理\t','爱好\t','分数']
        for t in title:
            self.Text.insert(tk.INSERT,t)
        self.Text.insert(tk.INSERT,'\n')
        for line in sortls:
            for i in range(len(line)):
                self.Text.insert(tk.INSERT,line[i])
                self.Text.insert(tk.INSERT,'\t')
            self.Text.insert(tk.INSERT,'\n')
            
    def ShowInfoAsc(self):
        self.Text.delete(1.0,tk.END)
        if len(self.data)==0:
            ms.showinfo(title='出错',message='没有学生数据')
            return 0
        else:
            flag=0
            ls_pro=[]
            for line in self.data:
                if line[5].strip(" ")==self.E1.get().strip(" "):
                    ls_pro.append(line)
                    flag=1
            if flag==0:
                ms.showinfo(title='出错',message='没有'+self.E1.get()+'的学生')
            else:
                AfterSort=sorted(ls_pro,key=(lambda x:x[8]))
                self.ShowInText(AfterSort)
    
    def ShowInfoDes(self):
        self.Text.delete(1.0,tk.END)
        if len(self.data)==0:
            ms.showinfo(title='出错',message='没有学生数据')
            return 0
        else:
            flag=0
            ls_pro=[]
            for line in self.data:
                if line[5].strip(" ")==self.E1.get().strip(" "):
                    ls_pro.append(line)
                    flag=1
            if flag==0:
                ms.showinfo(title='出错',message='没有'+self.E1.get()+'的学生')
            else:
                AfterSort=sorted(ls_pro,key=(lambda x:x[8]),reverse=True)
                self.ShowInText(AfterSort)
    
    def close(self):
        self.Text.delete(1.0,tk.END)
        self.E1.delete(0,'end')
        self.E1.focus()
        
    def createPage(self):
        tk.Label(self,text='请输入省份: ').grid(row=0,columnspan=2,sticky=tk.W,padx=175,pady=10)
        self.E1.grid(row=0,columnspan=2,sticky=tk.E,padx=165,pady=10)
        tk.Button(self,text='升序',width=5,command=self.ShowInfoAsc).grid(row=1,columnspan=2,sticky=tk.W,padx=100,pady=10)
        tk.Button(self,text='降序',width=5,command=self.ShowInfoDes).grid(row=1,columnspan=2,sticky=tk.W,padx=250,pady=10)
        tk.Button(self,text='清空',width=5,command=self.close).grid(row=2,columnspan=2,sticky=tk.E)
        self.Text.grid(row=1,columnspan=2,sticky=tk.E)

class SortKindPage(tk.Frame):
    def __init__(self,master=None,data=[]):
        tk.Frame.__init__(self, master)
        self.root=master
        self.data=data
        self.Text=tk.Text(self,height=41)
        self.createPage()
        
    def ShowInText(self,sortls):
        title=['编号\t','姓名\t','性别\t','年龄\t','民族\t','省份\t','文理\t','爱好\t','分数']
        for t in title:
            self.Text.insert(tk.INSERT,t)
        self.Text.insert(tk.INSERT,'\n')
        for line in sortls:
            for i in range(len(line)):
                self.Text.insert(tk.INSERT,line[i])
                self.Text.insert(tk.INSERT,'\t')
            self.Text.insert(tk.INSERT,'\n')
    
    def ShowInfoAsc(self):
        self.Text.delete(1.0,tk.END)
        if len(self.data)==0:
            ms.showinfo(title='出错',message='没有学生数据')
            return 0
        else:
            AfterSort=sorted(self.data,key=(lambda x:(x[6],x[8])))
        self.ShowInText(AfterSort)
            
    def ShowInfoDes(self):
        self.Text.delete(1.0,tk.END)
        if len(self.data)==0:
            ms.showinfo(title='出错',message='没有学生数据')
            return 0
        else:
            AfterSort=sorted(self.data,key=(lambda x:(x[6],x[8])),reverse=True)
        self.ShowInText(AfterSort) 
        
    def close(self):
        self.Text.delete(1.0,tk.END)
    
    def createPage(self):
        tk.Button(self,text='升序',width=5,command=self.ShowInfoAsc).grid(row=0,columnspan=2,sticky=tk.W,padx=100,pady=10)
        tk.Button(self,text='降序',width=5,command=self.ShowInfoDes).grid(row=0,columnspan=2,sticky=tk.W,padx=250,pady=10)
        tk.Button(self,text='清空',width=5,command=self.close).grid(row=0,columnspan=2,sticky=tk.E,padx=100,pady=10)
        self.Text.grid(row=1,columnspan=2,sticky=tk.E)