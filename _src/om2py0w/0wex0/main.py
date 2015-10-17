# -*- coding: utf-8 -*-
import sys

print """Congratulations: You have invoked the script main.py

-- I love coding in Python!
-- Do you love it?

Have fun in Python Star Trek!""" # 

keywords = sys.argv[1:] # The list of command line arguments passed to a Python script
# 命令行中 除脚本名 以外的所有参数都保存在 keywords 中

print keywords 
print type(keywords) # 查看keyword 它是list 输入英文 print 英文

# 在 cmd line 中输入中文 如 我爱python
# 问题： 中文 我爱 这部分 输出的是 一种编码形式 解决之 
# 分析： 传递参数（中文字符）后 再次输出 可能没有解码还原为中文字符
# 方案： google search 原来 在最初运用了 utf-8 编码 输出的时候 没有 unicoding 
