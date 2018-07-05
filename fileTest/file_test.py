#!/usr/bin/python
# -*- coding: UTF-8 -*-
 
# 打开一个文件
fo = open("foo.txt", "w")
fo.write("Hello world!")
print "文件名: ", fo.name
print "是否已关闭 : ", fo.closed
print "访问模式 : ", fo.mode
print "末尾是否强制加空格 : ", fo.softspace

fo.close()

fo = open("foo.txt", "r+")
str = fo.read(13)
print "reading strings is:", str
fo.close()
