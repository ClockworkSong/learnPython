#!/usr/bin/python 
#! -*- coding: utf-8 -*-

import time
import datetime

ticks = time.time()

print "current time:", ticks

print "format current time:", time.strftime("%Y-%m-%d-%H-%M-%S", time.localtime())

time = datetime.datetime.now()
print "current time:", time
