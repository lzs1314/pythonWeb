#@coding  :utf-8
#@FileName: 配置文件模块.py
#@Author  :辰晨
#@Time    :2019/4/23 11:26

import configparser

config = configparser.ConfigParser()
# config["DEFAULT"] = {'ServerAliveInterval': '45',
#                      'Compression': 'yes',
#                      'CompressionLevel': '9'}
#
# config['bitbucket.org'] = {'User':'hg'}
# # config['bitbucket.org']['User'] = 'hg'
# config['topsecret.server.com'] = {}
# topsecret = config['topsecret.server.com']
# topsecret['Host Port'] = '50022'  # mutates the parser
# topsecret['ForwardX11'] = 'no'  # same here
# config['DEFAULT']['ForwardX11'] = 'yes'
#
#
#
# with open('example.ini', 'w') as configfile:
#     config.write(configfile)


# 读
config.read('example.ini')
# print(config.sections())
# print(config.defaults())
# print(config['bitbucket.org']['User'])


# for key in config['bitbucket.org']:
#     print(key)


# 删除
# config.remove_section('topsecret.server.com')
#


# 修改
config.set('bitbucket.org','user','lzs')



config.write(open('example.ini','w'))