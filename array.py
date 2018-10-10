import numpy as np
import pandas as pd
def change_file(filename):
    f=open(filename,'r',encoding='utf-8',errors='ignore')
    line=f.readline()
    res=[]
    while(line):
        if line=='\n':
            line=f.readline()
            continue
        line_str=line.split()
        if len(line_str)>0 and line_str[0]=='ROW':
            #print(line_str)
            resrow=[]
            line=f.readline()
            while(len(line.split())>0 and line.split()[0]!='ROW'):
                resrow+=line.split()
                line=f.readline()
            print(len(resrow),resrow)
            res.append(resrow)
            continue
        line=f.readline()
    return res

changed_array=change_file('刚度阵.txt')
changed_array=np.array(changed_array)
data1=pd.DataFrame(changed_array)
data1.to_csv('刚度阵.csv')

