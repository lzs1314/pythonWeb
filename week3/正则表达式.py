#@coding  :utf-8
#@FileName: 正则表达式.py
#@Author  :辰晨
#@Time    :2019/4/23 11:56


# s = 'hello world'
#
# print(s.find('llo'))
# ret = s.replace('ll','xx')
# print(ret)
# print(s.split('w'))

import re

# . 只能代替一个任意字符 \n 除外
# ^ 开始位置
# $ 结束位置
# * 重复匹配 [0,+oo]
# +  [1.+oo]
# ?  [0.1]

# ret = re.findall('w\w{2}l','hello world')
# ret = re.findall('w..l','hello world')
# ret = re.findall('lzs','lflzasgdslzsgojawqwjasdal')
# ret = re.findall('^h...o','hlflzasgdslzsgojawqwjasdahellol')
# ret = re.findall('^h...o$','hlflzasgdslzsgojawqwjasdahellol')
# ret = re.findall('lzs.*ll','hlflzasgdslzsgojawqwjasdahellol')
# ret = re.findall('ab+','hlflzasgdslzaaaaabsgojawqwjasdahellol')
# ret = re.findall('a+b','hlflzasgaaaaabdslzsgojawqwjasdahellol')
ret = re.findall('a{5}b','hlflzasaaaaabgdslzsgojawqwjasdahellol')

print(ret)


# * 等于{0,+oo}   +等价于{1，+oo}    ？等价于{0，1} 推荐前者

# ret = re.findall('a[c,d]x','acx')
# ret = re.findall('[a-z]x','adx')
# ret = re.findall('[w,*]x','adwx*')
ret = re.findall('[1-9,a-z,A-Z]x','12tyAS')
ret = re.findall('^iu','iu12tyAS')
ret = re.findall('[^t]','12tyAS')

# [] 字符集 取消元字符的特殊功能( \ ^ -)
# ^ 放[]里  取反
# 反斜杠后边跟元字符去除特殊功能,比如\.
# 反斜杠后边跟普通字符实现特殊功能,比如\d
#
# \d  匹配任何十进制数；它相当于类 [0-9]。
# \D 匹配任何非数字字符；它相当于类 [^0-9]。
# \s  匹配任何空白字符；它相当于类 [ \t\n\r\f\v]。
# \S 匹配任何非空白字符；它相当于类 [^ \t\n\r\f\v]。
# \w 匹配任何字母数字字符；它相当于类 [a-zA-Z0-9_]。
# \W 匹配任何非字母数字字符；它相当于类 [^a-zA-Z0-9_]
# \b  匹配一个特殊字符边界，比如空格 ，&，＃等


print(re.search('we', 'dgsdfweerdg').group())


# m = re.search('\bbk','bkdfk') #不加r拿不到
# m = re.search(r'\bbk','bkdfk')

er = re.search('(?P<id>\d{3})/(?P<name>\w{3})','wersa123/ooo')
print(er.group())


rt = re.match('asd','asdergsdg')

ret = re.split('[j,s]','sdjksal')

ret = re.sub('a..x','s..b','dkfljgalsx')

# re = re.findall('\.com','afsasfafs.comasf')
obj = re.compile('\.com')
obj.findall('agadgad.comgsdasd')





