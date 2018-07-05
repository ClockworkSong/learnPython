#!/usr/bin/python
# -*- coding: utf-8 -*-

dict = {'acc': 40, 'speed': 400, 'time': 2.0, 'radius': 0.10}

print "radius", dict['radius']
print "time", dict['time']
print "speed", dict['speed']
print "acc", dict['acc']

dict = {'a':[1, 2], 'b': {"c": "d"}}

print "a = ", dict['a'][0]
print "b = ", dict['b']["c"]

user = {
	'A': {'acc': 40, 'speed': 200, 'time': 2.0, 'radius': 0.10},
	'B': {'acc': 80, 'speed': 400, 'time': 2.0, 'radius': 0.10},
	'C': {'acc': 100, 'speed': 600, 'time': 2.0, 'radius': 0.20},
	'D': {'acc': 120, 'speed': 800, 'time': 2.0, 'radius': 0.50},
	}
print "A.acc", user['A']['acc']
print "B.speed", user['B']['speed']
print "C.time", user['C']['time']
print "D.radius", user['D']['radius']

