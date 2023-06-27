import subprocess
import pandas as pd
import numpy as np
BaseFolder = input('indexファイルと複数のcsvファイルが入っているフォルダを入力　>> ')
IndexFileName = input('indexファイルの名前を入力 〇.csv　>> ')
OutputFileName = input('出力ファイルの名前を入力 〇.csv　>> ')
KeyName=input('csvファイルの共通文字を入力 例：ラン　>> ')
IndexFile=BaseFolder+'\\\\'+IndexFileName'+'.csv'
OutputFile=BaseFolder+'\\\\'+OutputFileName+'.csv''
df_index=pd.read_csv(IndexFile, delimiter=',', index_col=None, header=0, skiprows=0, encoding='utf-8', engine='python')
IDs=df_index['ID'].to_list()
df_list=pd.DataFrame(index=range(0), columns=[])
for ID in IDs:
    CsvFile=BaseFolder+'\\\\'+str(ID)+str(KeyName)+'.csv'
    df = pd.read_csv(CsvFile, delimiter=',', index_col=None, header=None, skiprows=0, encoding='utf-8', engine='python')
    # df=pd.read_csv(CsvFile, sep='\s+', index_col=None, header=None, skiprows=0, encoding='utf-8', engine='python')
    df_list=pd.concat([df_list, df], axis=0)
    print('df_list', df)
df_list.to_csv(OutputFile, encoding='utf-8-sig')
subprocess.Popen(["start", "", OutputFile], shell=True)