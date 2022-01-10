import tkinter as tk
from tkinter import filedialog
import sys
from antlr4 import *
from antlr.timeLexer import timeLexer
from antlr.timeParser import timeParser
from antlr.timeVisitor import timeVisitor
from antlr.test_time_visitor import *
from z3 import *
import pandas as pd

def filepath_analysis(Filepath):
    dir_stop = 0
    filename_stop = 0
    for i in range(len(Filepath)-1,-1,-1):
        if Filepath[i]==".":
            filename_stop = i
        if Filepath[i]=="/":
            dir_stop = i
            break
    Filedir = Filepath[:dir_stop]
    Filename = Filepath[dir_stop+1:filename_stop]
    return Filedir, Filename


def choose_file():
    root = tk.Tk()
    root.withdraw()
    Filepath = filedialog.askopenfilename()
    return Filepath

def analyze_make_res_file(Filepath):
    df = pd.read_excel(Filepath,sheet_name="考勤记录")
    data_res = pd.DataFrame(columns=['人员名称', '上班时间','上班时长','所属部门', '所属考勤组', '日期', '考勤时间1', '打卡时间1', '打卡状态1', '处理情况1', '打卡方式1',
       '打卡地点1', '坐标1', 'WIFI网络1', '备注1', '打卡入口1', '打卡设备信息1','考勤时间2', '打卡时间2', '打卡状态2', '处理情况2', '打卡方式2',
       '打卡地点2', '坐标2', 'WIFI网络2', '备注2', '打卡入口2', '打卡设备信息2'])
    res_col_name=['人员名称', '上班时间','上班时长','所属部门', '所属考勤组', '日期', '考勤时间1', '打卡时间1', '打卡状态1', '处理情况1', '打卡方式1',
       '打卡地点1', '坐标1', 'WIFI网络1', '备注1', '打卡入口1', '打卡设备信息1','考勤时间2', '打卡时间2', '打卡状态2', '处理情况2', '打卡方式2',
       '打卡地点2', '坐标2', 'WIFI网络2', '备注2', '打卡入口2', '打卡设备信息2']

    for i in range(0,len(df),2):
        arr=[]   
        data1 = df.iloc[i].values
        data2 = df.iloc[i+1].values
        arr = [data1[0]]
        arr.append(str(data1[5])+"-"+str(data2[5]))

        if type(data1[5])==str and type(data2[5])==str:
            t11, t12 = analyze_time(data1[5])
            t21, t22 = analyze_time(data2[5])
            minutes = int(t21)*60+int(t22)-int(t11)*60-int(t12)
            arr.append(str(minutes//60)+"hours "+str(minutes%60)+"minutes")
        else:
            arr.append("XXXXX")
        arr.extend(data1[1:4])
        arr.extend(data1[4:])
        arr.extend(data2[4:])
    
        d = dict(zip(res_col_name,arr))

        data_res.loc[len(data_res)] = arr

    data_res.to_excel(Filedir+"/"+Filename+"_result.xls")


        
    Respath = Filedir+"/"+Filename+"_result.xls"
    return Respath

