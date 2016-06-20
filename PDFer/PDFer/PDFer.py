import pdf2txt

#import time
import csv
from PySide import QtGui
import os
import os.path

# prove prove

my_dir = QtGui.QFileDialog.getExistingDirectory(None,'Scegli una cartella','\\srveuro\Ufficio_Tecnico\VALIDAZIONE\S10')
file_list = []
 
for dirpath, dirnames, filenames in os.walk(my_dir):
    for filename in [f for f in filenames if f.endswith(".pdf")]:
        file_list.append(os.path.join(dirpath, filename))

nome_file = raw_input('Nome del file CSV:')

#nome=[]
#nome.append('Ore')
#
#my_dir = QtGui.QFileDialog.getExistingDirectory(None,'Scegli una cartella','D:\Documenti\Lavoro\Eurocoating\Logs')
#
#
## Get folder path containing text files
#file_list = glob.glob(my_dir + '/*.csv')
#
#

#lunghezza = 5 #len(file_list)
lunghezza = len(file_list)
    
excel = [[0 for x in range(7)] for y in range(lunghezza)] 

for f in range(0,lunghezza):
#for f in range(0,len(file_list)):
    print f
    reportpdf = file_list[f]
    
    reporttxt = my_dir + '\\temp.txt'
    
    pdf2txt.main(['', '-o', reporttxt, reportpdf]) 
    
    data_raw = []
    
    
    testo = open(reporttxt, 'r')
    
    with testo as myfile:
        for line in myfile:
            data_raw.append(line)
            
    #for i in range(0,len(data_raw)):
    #    print i, data_raw[i]
        
    testo.close()
    

    
    
    
    ############## Data ##############
    
    excel[f][0] = data_raw[2][:-1]
    
    
    ############## Nome #############
    
    index = data_raw.index('[mm]\n')
    

        
    excel[f][1] = data_raw[index+2][:-1]
    
    ############## Norma #############
    
    index = data_raw.index('GAUSS\n')
    
    if int(data_raw[index-3][:-1]) == 10:
        excel[f][2] = 'EC'
        
    if int(data_raw[index-3][:-1]) == 5:
        excel[f][2] = 'NORMA'   
    
    
    
    ############## Ra #############
    
    index = data_raw.index('Ra\n')
    
    excel[f][3] = float(data_raw[index+10][:-3])
    
    ############## Rz #############
    
    excel[f][4] = float(data_raw[index+11][:-3])
    
    ############## Rt #############
    
    excel[f][5] = float(data_raw[index+12][:-3])
    
    ############## Nome file #############
    
    excel[f][6] = reportpdf
    
    
nome_csv = my_dir + "\\" +  nome_file +".csv"
    
with open(nome_csv, "wb") as c:
    writer = csv.writer(c, delimiter=";")
    writer.writerows(excel)
    
print "Finito!"