from os import name
from flask import Flask, render_template, url_for, request
import os
import tkinter as tk
from tkinter import filedialog
import pandas as pd
app = Flask(__name__)

FrontResult=""
@app.route('/')
def main(): 
    title = "考勤系统" 
    return render_template('main.html',title=title)


@app.route('/show_obj_address')
def show_obj_address():
    title = "Ready to work"
    
    root = tk.Tk()
    print('1')
    root.withdraw()
    print('2')
    Filepath = filedialog.askopenfilename()
    print('3')
    if Filepath=="":
        pass

    return render_template('show_obj_address.html',title=title,Filepath = Filepath)
    
@app.route('/show_res_address',methods=['GET','POST'])
def show_res_address():
    print(request.json)
    Filepath = request.json['filepath']
    title = "Finished"
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

    df = pd.read_excel(Filepath,sheet_name="考勤记录")
    print(df.columns)
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
            t11,t12 = data1[5].split(":")
            t21,t22= data2[5].split(":")
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
    # return render_template('show_res_address.html',title=title,Filepath = Filepath,Respath = Respath)
    return Respath

if __name__ == "__main__":
    app.run(debug=True)