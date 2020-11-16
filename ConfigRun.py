"""
============================
author:YAN GAO
student ID:1995106
============================
"""
from configurationProject.Config import Config

conf = Config(r'C:/temp/config.ini')

if conf.load() :
    conf.addAttribute('DB Configuration','MaxConnections',9)
    conf.addAttribute('DB Configuration','DBMS','Sybase')
    conf.addAttribute('DB Configuration','CharacterSet','UTF-8')
    conf.addAttribute('xx 11','aa',14.56)
    conf.addAttribute('yy 12','bb','1111111')
    conf.addAttribute('FileType','ColumnDelimiter',',')
    conf.addAttribute('FileType','ColumnNames',"['Name','Age','Score']")
    #
    conf.removeAttribute('FileType','ColumnDelimiter')
    #
    a = conf.getIntValue('DB Configuration','MaxConnections')
    print("a = ",a)
    a1 = conf.getIntValue('DB Configuration','DBMS')
    print("a1 = ",a1)
    #
    b = conf.getStringValue('DB Configuration','CharacterSet')
    print("b = ",b)
    #
    c = conf.getFloatValue('xx 11','aa')
    print("c = ",c)
    #
    d = conf.getListValue('FileType','ColumnNames')
    print("d = ",d)

    conf.save()
