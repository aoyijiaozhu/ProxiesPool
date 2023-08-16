# 作者：aoyijiaozhu
# 创建时间：2023/1/15 11:55
# 修改时间：2023/8/16
# 建立一个把 以字典元素储存的 txt格式文本 转换为 字典列表 的项目
from ast import literal_eval

def transform_lines(txt_file):  #txt有多行，把每行数据转换成字典元素
    file=txt_file
    lines=file.readlines()
    dict_lst=[]
    for line in lines:
        content=line.split('\n')[0]
        dict=literal_eval(content)
        dict_lst.append(dict)
    return dict_lst

def transform_line(txt_file):   #txt有单行，以逗号分隔
    file=txt_file
    obj=file.read()
    lst=obj.split(',')
    dict_lst = []
    for content in lst:
        dict = literal_eval(content)
        dict_lst.append(dict)
    return dict_lst

def transform_DIY(txt_file,split_value):   #自定义分割
    file=txt_file
    obj=file.read()
    lst=obj.split(split_value)
    dict_lst = []
    for content in lst:
        dict = literal_eval(content)
        dict_lst.append(dict)
    return dict_lst







