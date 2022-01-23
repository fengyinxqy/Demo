import tkinter as tk
import tkinter.messagebox as ms
import matplotlib.pyplot as plt
import jieba
from wordcloud import WordCloud
class AnalysisMaxPage(tk.Frame):
    def __init__(self,master=None,data=[]):
        tk.Frame.__init__(self, master)
        self.root=master
        self.data=data
        self.Text=tk.Text(self,height=41)
        self.createPage()
        
    def ShowInText(self,data_dict1,data_dict2):
        title=['省份\t\t','最高分\t\t','最低分\t']
        for t in title:
            self.Text.insert(tk.INSERT,t)
        self.Text.insert(tk.INSERT, "\n-------------------------------------------\n")
        pro=list(data_dict1)
        max_score=list(data_dict1.values())
        min_score = list(data_dict2.values())
        for i in range(len(data_dict1)):
            self.Text.insert(tk.INSERT,pro[i])
            self.Text.insert(tk.INSERT, "\t\t")
            self.Text.insert(tk.INSERT,max_score[i])
            self.Text.insert(tk.INSERT, "\t\t")
            self.Text.insert(tk.INSERT,min_score[i])
        self.Text.insert(tk.INSERT, "\n-------------------------------------------\n")
        
    def GetDictMax(self,data_dict):
        for key in data_dict:
            max_score=data_dict[key]
            for line in self.data:
                if line[5].strip(" ")==key:
                    max_score=max(max_score,int(line[8]))
            data_dict[key]=max_score
        return data_dict
    
    def GetDictMin(self,data_dict):
        for key in data_dict:
            min_score=data_dict[key]
            for line in self.data:
                if line[5].strip(" ")==key:
                    min_score=min(min_score,int(line[8]))
            data_dict[key]=min_score
        return data_dict
            
    def GetDict(self):
        if len(self.data)==0:
            ms.showinfo(title="出错",message="没有学生数据")
            return 0
        else:
            data_dict={}
            for line in self.data:
                data_dict[line[5]]=int(line[8])
        return data_dict
    
    def ShowInfo(self):
        self.Text.delete(1.0,tk.END)
        self.ShowInText(self.GetDictMax(self.GetDict()),self.GetDictMin(self.GetDict()))
        
    def ShowInLine(self):
        max_score_dict=self.GetDictMax(self.GetDict())
        max_value=list(max_score_dict.values())
        key=list(max_score_dict.keys())
        min_score_dict=self.GetDictMin(self.GetDict())
        min_value=list(min_score_dict.values())
        plt.rcParams['font.sans-serif']=['SimHei','Times New Roman']
        plt.rcParams['axes.unicode_minus']=False
        fig1=plt.figure()
        fig1.set_facecolor('blueviolet')
        plt.subplot[211]
        plt.title('各省分数统计',fontproperties='STKAITI',fontsize=20)
        plt.ylabel('最高分',fontproperties='simhei',fontsize=12)
        plt.plot(key,min_value,marker="*",mec='k',mfc='w',color='c',linestyle=":",linewidth=2)
        plt.show()
    
    def createPage(self):
        tk.Button(self.root, text="文本方式",width=10,command=self.ShowInfo).grid(row=0, columnspan=2,sticky=tk.W,padx=180,pady=10)
        tk.Button(self.root, text="图形方式",width=10,command=self.ShowInLine).grid(row=0, columnspan=2,sticky=tk.E,padx=180,pady=10)
        self.Text.grid(row=1, columnspan=2, sticky=tk.E)
        
class AnalysisPeoplePage(tk.Frame):
    def __init__(self, master=None,data=[]):
        tk.Frame.__init__(self, master)
        self.root=master
        self.Text=tk.Text(self,height=41)
        self.data=data
        self.createPage()
    
    def ShowInText(self,data_dict):
        title=['民族\t','人数\t']
        for t in title:
            self.Text.insert(tk.INSERT,t)
        self.Text.insert(tk.INSERT,'\n')
        for key,value in data_dict.items():
            self.Text.insert(tk.INSERT, key)
            self.Text.insert(tk.INSERT, "\t")
            self.Text.insert(tk.INSERT, value)
            self.Text.insert(tk.INSERT, "\n")
    def GetDict(self):
        if len(self.data)==0:
            ms.showinfo(title="出错",message="没有学生数据")
            return 0
        else:
            data_dict = {}
            for line in self.data:
                data_dict[line[4]]=data_dict.get(line[4],0)+1
        return data_dict
    def ShowInData(self):
        self.ShowInText(self.GetDict())
    def ShowInPic(self):
        Peo_dict=self.GetDict()
        value=list(Peo_dict.values())
        key=list(Peo_dict.keys())
        x=list(range(len(key)))
        plt.rcParams['font.sans-serif']=['SimHei','Times New Roman']
        plt.rcParams['axes.unicode_minus']=False
        plt.bar(x,value,width=0.2,tick_label=key)
        plt.title('各民族人数统计',fontproperties='STKAITI',fontsize=20)
        plt.xlabel('民族',fontproperties='STKAITI',fontsize=18)
        plt.ylabel('人数',fontproperties='simhei',fontsize=18)
        plt.show()
    def createPage(self):
        tk.Button(self.root, text="文本方式",width=10,command=self.ShowInData).grid(row=0, columnspan=2,sticky=tk.W,padx=180,pady=10)
        tk.Button(self.root, text="图形方式",width=10,command=self.ShowInPic).grid(row=0, columnspan=2,sticky=tk.E,padx=200,pady=10)
        self.Text.grid(row=1, columnspan=2, sticky=tk.E)

class AnalysisHobbyPage(tk.Frame):
    def __init__(self, master=None,data=[]):
        tk.Frame.__init__(self, master)
        self.root=master
        self.data=data
        self.Text=tk.Text(self,height=41)
        self.createPage()
    
    def ShowInText(self,data_dict):
        title=['词语\t','出现次数\t']
        for t in title:
            self.Text.insert(tk.INSERT,t)
        self.Text.insert(tk.INSERT,'\n')
        for key,value in data_dict.items():
            self.Text.insert(tk.INSERT, key)
            self.Text.insert(tk.INSERT, "\t")
            self.Text.insert(tk.INSERT, value)
            self.Text.insert(tk.INSERT, "\n")
    def GetWordStr(self):
        wordstr=''
        for line in self.data:
            wordstr = wordstr+line[7]
        wordstr=wordstr.replace('、', '').strip('\n')
        return  wordstr
    def ShowWords(self):
        if len(self.data) == 0:
            ms.showinfo(title="出错",message="没有学生数据")
            return 0
        else:
            word_dict = { }
            words=jieba.lcut(self.GetWordStr())
            for word in words:
                word_dict[word]=word_dict.get(word,0)+1
                self.ShowInText(word_dict)
    def createPage(self):
        tk.Button(self.root, text="词频统计",width=10,command=self.ShowInText).grid(row=0, columnspan=2,sticky=tk.W,padx=180,pady=10)
        tk.Button(self.root, text="词云图",width=10,command=self.ShowWords).grid(row=0, columnspan=2,sticky=tk.E,padx=200,pady=10)
        self.Text.grid(row=1, columnspan=2, sticky=tk.E)