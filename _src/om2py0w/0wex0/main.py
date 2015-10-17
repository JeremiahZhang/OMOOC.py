# -*- coding: utf-8 -*-
import sys

print """Congratulations: You have invoked the script main.py

-- I love coding in Python!
-- Do you love it?

Have fun in Python Star Trek!""" # 

keywords = sys.argv[1:] # The list of command line arguments passed to a Python script
# 命令行中 除脚本名 以外的所有参数都保存在 keywords 中

print keywords # 查看keyword 它是list
