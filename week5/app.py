#@coding  :utf-8
#@FileName: app.py
#@Author  :辰晨
#@Time    :2019/5/8 15:47

# from src import comm
#
# # comm.add()
# func = 'add'
# fun = getattr(comm,func)
# fun()

module = 'src.comm'
func = 'add'
# 字符串导入模块
import importlib

m=importlib.import_module(module)
fun = getattr(m,func)
fun()













