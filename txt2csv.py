import csv
 
csvFile = open("data1.csv",'w',newline='',encoding='GBK') # 固定格式
writer = csv.writer(csvFile) # 固定格式
csvRow = [] # 用来存储csv文件中一行的数据
 
# 对csvRow通过append()或其它命令添加数据
writer.writerow(csvRow) # 将csvRow中数据写入csv文件中

f = open("SPO_1.txt",'r',encoding='utf-8')
for line in f:
    csvRow = line.split()
    print(csvRow)
    writer.writerow(csvRow)
 
f.close()
csvFile.close()