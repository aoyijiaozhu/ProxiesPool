# 作者：aoyijiaozhu
# 创建时间：2023/1/15 11:55
# 修改时间：2023/8/16
# 建立一个把 txt格式文本 转换为 列表 的项目

def transform_lines(txt_file):  #txt有多行，把每行数据转换成列表元素
    file=txt_file
    lines=file.readlines()
    lst=[]
    for line in lines:
        lst.append(line.split('\n')[0])
    return lst

def transform_line(txt_file):   #txt有单行，以逗号分隔
    file=txt_file
    obj=file.read()
    lst=obj.split(',')
    return lst

def transform_DIY(txt_file,split_value):   #自定义分割
    file=txt_file
    obj=file.read()
    lst=obj.split(split_value)
    return lst






