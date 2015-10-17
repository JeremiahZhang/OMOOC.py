# -*- coding: utf-8 -*-
# 
import sys
# print sys.getdefaultencoding()
reload(sys) # 必须 reload
sys.setdefaultencoding('utf-8')

print """Congratulations: You have invoked the script main.py

-- I love coding in Python!
-- Do you love it?

Have fun in Python Star Trek!""" # 

done = False
textInput = ""

while (done == False):
    nextInput = raw_input("Please input ur words: ")
    if nextInput == "end":
        break
    else:
        textInput += nextInput

print ("Here is ur diary: " + textInput)

keywords = sys.argv[1:] # The list of command line arguments passed to a Python script
# 命令行中 除脚本名 以外的所有参数都保存在 keywords 中

print keywords 
print type(keywords) # 查看keyword 它是list 输入英文 print 英文

for words in keywords:
    # words = unicode(words, "ascii")
    # print words
    # print type(words)
    print words,

# ========== 中文输入
# 在 cmd line 中输入中文 如 我爱python
# 问题： 中文 我爱 这部分 输出的是 一种编码形式 解决之 
# 分析： 传递参数（中文字符）后 再次输出 可能没有解码还原为中文字符
# 方案： google search 原来 在最初运用了 utf-8 编码 输出的时候 没有 unicoding 
# keywords = unicode(keywords, "utf-8")
# 但是不能解码list error need string or buffer
# utf 解码错误
#     words = words.defcode("ascii").encode("utf-8")
# 在没有修改默认编码是 以上设置 也是错的
# 参考 http://www.kryptosx.info/archives/391.html
# ===========持续交互