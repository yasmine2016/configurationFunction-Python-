"""
============================
author:YAN GAO
student ID:1995106
============================
"""
import re
import os

class Config:
    def __init__(self,fileName):
        self.fpath = fileName
        self.fname = os.path.basename(self.fpath)
        self.path_dst = self.fpath[:self.fpath.find(self.fname) - 1]
        self.dic_all = dict()

    def addFile(self,contain):
        try:
            with open(self.fname,'a') as f:
                f.writelines(contain)
        except Exception as e:
            print(e)

    def writeFile(self,contain):
        try:
            with open(self.fname,'w') as f:
                f.writelines(contain)
        except Exception as e:
            print(e)

    def changeToDict(self,str_all):
        values = []
        all_dic = {}
        key_temp = ''
        for i in str_all:
            if i.find('[') == 0 and i.find('=') == -1:
                if key_temp != '':
                    all_dic.update({key_temp: values})
                    key_temp = i
                    values = []
                else:
                    key_temp = i
            else:
                if key_temp != '' and i.find('=') != -1:
                    values.append(i)
                if i == str_all[len(str_all) - 1]:
                    all_dic.update({key_temp: values})
        return all_dic

    def chkSection(self, section_name):
        rtn = False
        str_section = '[' + section_name + ']'
        dic_values = self.dic_all.get(str_section)
        if dic_values != None:
            rtn = True
        return rtn

    def addAttribute(self,section_name,attributte_name, attribute_value):
        str_section = '[' + section_name + ']'
        if self.chkSection(section_name):
            dic_values = self.dic_all.get(str_section)
            for i in dic_values:
                index_attr = i.replace(' ', '').find(attributte_name + '=')
                if index_attr != -1:
                    dic_values.remove(i)
                    dic_values.append(attributte_name + " = " + str(attribute_value))
                    self.dic_all[str_section] = dic_values
                    print("Add attribute '{}:{}={}' success!".format(section_name,attributte_name,attribute_value))
                    return
            dic_values.append(attributte_name + " = " + str(attribute_value))
            self.dic_all[str_section] = dic_values
        else:
            self.dic_all[str_section] =[attributte_name + " = " + str(attribute_value)]
        print("Add attribute '{}:{}={}' success!".format(section_name,attributte_name,attribute_value))

    def removeAttribute(self,section_name,attributte_name):
        str_section = '[' + section_name + ']'
        if self.chkSection(section_name):
            dic_values = self.dic_all.get(str_section)
            for i in dic_values:
                index_attr = i.replace(' ','').find(attributte_name+'=')
                if index_attr != -1:
                    dic_values.remove(i)
                    self.dic_all[str_section] = dic_values
                    print("Remvoe attribute '{}:{}' success!".format(section_name,attributte_name))
                    return
            print("removeAttribute: This attributte '{}' is not exist".format(attributte_name))
        else:
            print("removeAttribute: This section '{}' is not exist".format(section_name))

    def getIntValue(self,section_name,attributte_name):
        rtn = None
        str_section = '[' + section_name + ']'
        if self.chkSection(section_name):
            dic_values = self.dic_all.get(str_section)
            for i in dic_values:
                index_attr = i.find(attributte_name)
                if index_attr != -1:
                    index_equ = i.find('=')
                    str_value = i[index_equ+1:].strip()
                    try:
                        int_value = int(str_value)
                        rtn = int_value
                    except:
                        break
        else:
            print("getIntValue: This section '{}' is not exist".format(section_name))

        return rtn

    def getStringValue(self,section_name,attributte_name):
        rtn = None
        str_section = '[' + section_name + ']'
        if self.chkSection(section_name):
            dic_values = self.dic_all.get(str_section)
            for i in dic_values:
                index_attr = i.find(attributte_name)
                if index_attr != -1:
                    index_equ = i.find('=')
                    fina_value = i[index_equ + 1:].strip()
                    try:
                        str_value = str(fina_value)
                        rtn = str_value
                    except:
                        break
        else:
            print("getStringValue: This section '{}' is not exist".format(section_name))
        return rtn

    def getFloatValue(self,section_name,attributte_name):
        rtn = None
        str_section = '[' + section_name + ']'
        if self.chkSection(section_name):
            dic_values = self.dic_all.get(str_section)
            for i in dic_values:
                index_attr = i.find(attributte_name)
                if index_attr != -1:
                    index_equ = i.find('=')
                    str_value = i[index_equ + 1:].strip()
                    try:
                        float_value = float(str_value)
                        rtn = float_value
                    except:
                        break
        else:
            print("getFloatValue: This section '{}' is not exist".format(section_name))
        return rtn

    def getListValue(self,section_name,attributte_name):
        rtn = None
        str_section = '[' + section_name + ']'
        if self.chkSection(section_name):
            dic_values = self.dic_all.get(str_section)
            for i in dic_values:
                index_attr = i.find(attributte_name)
                if index_attr != -1:
                    index_equ = i.find('=')
                    str_value = i[index_equ + 1:].strip()
                    if str_value.find('[') == 0 and str_value.find(']') == len(str_value)-1:
                        rtn = str_value
        else:
            print("getListValue: This section '{}' is not exist".format(section_name))
        return rtn

    def load(self):
        rtn = False
        try:
            with open(self.fpath, 'r') as f:
                str_all = re.split(r'[\n]+',f.read().strip())
                self.dic_all = self.changeToDict(str_all)
                rtn = True
        except Exception as e:
            print(e)

        return rtn

    def save(self):
        try:
            with open(self.fpath,'w') as f:
                for key in self.dic_all:
                    f.write(key+'\n')
                    for j in self.dic_all[key]:
                        f.write(j+'\n')
        except Exception as e:
            print(e)
