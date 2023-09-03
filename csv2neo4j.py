import csv # 导入csv文件
import py2neo # 导入py2neo库
from py2neo import Graph,Node,Relationship,NodeMatcher

g = Graph('neo4j://localhost:7687', user='neo4j', password='1') # 连接neo4j，将'xxx'分别改为你的用户名和密码
g.delete_all() # 清除neo4j中原有的结点等所有信息

with open('C:/Users/FanHaidi/AppData/Local/Programs/data.csv','r',encoding='gbk') as f:
    reader=csv.reader(f)
    for item in reader:
        #if reader.line_num==1:
        #    continue
        print("当前行数：",reader.line_num,"当前内容：",item)
        start_node=Node(item[0],name=item[1])
        end_node=Node(item[3],name=item[4])
        relation=Relationship(start_node,item[2],end_node)
        

        g.merge(start_node,item[0],"name")
        g.merge(end_node,item[3],"name")   
        g.merge(relation,"关系","属性")
# 注意缩进 