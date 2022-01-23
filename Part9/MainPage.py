import tkinter as tk
import EditPage as ep
import QueryPage as qp
import SortPage as sp
import AnalysisPage as ap
import UserPage as up
import csv
class MainPage(object):
    def __init__(self, master=None,name=""):
        self.root = master
        self.root.geometry('%dx%d'%(600,600))
        self.data = []
        self.username=name
        self.createPage()
    def createPage(self):
        self.InsertPage=ep.InsertPage(self.root,self.data)
        self.DeletePage = ep.DeletePage(self.root, self.data)
        self.ChangePage = ep.ChangePage(self.root, self.data)
        self.QuerynumPage = qp.QueryNumPage(self.root, self.data)
        self.QuerynationPage=qp.QueryNationPage(self.root,self.data)
        self.QueryprovincePage=qp.QueryProvincePage(self.root,self.data)
        self.SortallPage=sp.SortAllPage(self.root, self.data)
        self.SortproPage=sp.SortProPage(self.root,self.data)
        self.SortkindPage=sp.SortKindPage(self.root,self.data)
        self.AnalysismaxPage=ap.AnalysisMaxPage(self.root,self.data)
        self.AnalysispeoplePage=ap.AnalysisPeoplePage(self.root,self.data)
        self.AnalysishobbyPage=ap.AnalysisHobbyPage(self.root,self.data)
        self.UserAddpage = up.UserAddPage(self.root, self.username)
        self.UserChangePage = up.UserChangePage(self.root, self.username)
        self.UserDeletePage = up.UserDeletePage(self.root, self.username)
        self.createMenu()
    def forgetAll(self):
        self.DeletePage.pack_forget()
        self.InsertPage.pack_forget()
        self.ChangePage.pack_forget()
        self.QuerynumPage.pack_forget()
        self.QuerynationPage.pack_forget()
        self.QueryprovincePage.pack_forget()
        self.SortallPage.pack_forget()
        self.SortproPage.pack_forget()
        self.SortkindPage.pack_forget()
        self.AnalysismaxPage.pack_forget()
        self.AnalysispeoplePage.pack_forget()
        self.AnalysishobbyPage.pack_forget()
        self.UserAddpage.pack_forget()
        self.UserChangePage.pack_forget()
        self.UserDeletePage.pack_forget()
        
    def inputData(self):
        self.forgetAll()
        self.InsertPage.pack()
    def deletData(self):
        self.forgetAll()
        self.DeletePage.pack()
    def changeData(self):
        self.forgetAll()
        self.ChangePage.pack()
    def queryNum(self):
        self.forgetAll()
        self.QuerynumPage.pack()
    def queryNation(self):
        self.forgetAll()
        self.QuerynationPage.pack()
    def queryProvince(self):
        self.forgetAll()
        self.QueryprovincePage.pack()
    def sortAll(self):
        self.forgetAll()
        self.SortallPage.pack()
    def sortPro(self):
        self.forgetAll()
        self.SortproPage.pack()
    def sortKind(self):
        self.forgetAll()
        self.SortkindPage.pack()
    def analysisMax(self):
        self.forgetAll()
        self.AnalysismaxPage.pack()
    def analysisPeople(self):
        self.forgetAll()
        self.AnalysispeoplePage.pack()
    def analysisHobby(self):
        self.forgetAll()
        self.AnalysishobbyPage.pack()
    def userAdd(self):
        self.forgetAll()
        self.UserAddpage.pack()
    def passwordChange(self):
        self.forgetAll()
        self.UserChangePage.pack()
    def userDelete(self):
        self.forgetAll()
        self.UserDeletePage.pack()
    def ImportData(self):
        with open("python basis\Part9\成绩单.csv","r",encoding="utf-8")as f:
            f.readline()
            for line in f:
                t = line.strip('\n').split(',')
                self.data.append(t)
    def SaveFile(self):
        with open("python basis\Part9\成绩单.csv","w",encoding="utf-8",newline='')as f:
            w=csv.writer(f)
            w.writerow(["编号","姓名","性别","年龄","民族","省份","科目","爱好","分数"])
            w.writerows(self.data)
    def createMenu(self):
        menu_main=tk.Menu(self.root)
        file_manage=tk.Menu(menu_main)
        data_change=tk.Menu(menu_main)
        data_search=tk.Menu(menu_main)
        data_sort=tk.Menu(menu_main)
        data_analysis=tk.Menu(menu_main)
        user_manage=tk.Menu(menu_main)
        
        file_manage.add_command(label="导入数据",command=self.inputData)
        file_manage.add_command(label="保存文件",command=self.SaveFile)
        file_manage.add_command(label="退出",command=self.root.quit())
        
        data_change.add_command(label="插入",command=self.inputData)
        data_change.add_command(label="删除",command=self.deletData)
        data_change.add_command(label="修改",command=self.changeData)
        
        data_search.add_command(label="按编号查询",command=self.queryNum)
        data_search.add_command(label="按民族查询",command=self.queryNation)
        data_search.add_command(label="按省份和科目查询",command=self.queryProvince)
        
        data_sort.add_command(label="所有分数排序",command=self.sortAll)
        data_sort.add_command(label="省份分数排序",command=self.sortPro)
        data_sort.add_command(label="文理分数排序",command=self.sortKind)
        
        data_analysis.add_command(label="各省份的最高分",command=self.analysisMax)
        data_analysis.add_command(label="各民族的总人数",command=self.analysisPeople)
        data_analysis.add_command(label="兴趣爱好词频",command=self.analysisHobby)
        
        user_manage.add_command(label="添加账户",command=self.userAdd)
        user_manage.add_command(label="修改密码",command=self.passwordChange)
        user_manage.add_command(label="删除账户",command=self.userDelete)
        
        menu_main.add_cascade(label="文件",menu=file_manage)
        menu_main.add_cascade(label="编辑",menu=data_change)
        menu_main.add_cascade(label="查找",menu=data_search)
        menu_main.add_cascade(label="排序",menu=data_sort)
        menu_main.add_cascade(label="统计",menu=data_analysis)
        menu_main.add_cascade(label="用户",menu=user_manage)
        self.root['menu']=menu_main
        
        
        