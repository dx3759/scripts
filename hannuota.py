#!/usr/bin/env python
# -*- coding:utf-8 -*-
# By who 2013-11-12

# TODO  hannuota.py


import sys
reload(sys)
sys.setdefaultencoding('utf-8')

g_count = 0

def hanoi(n, a, b, c):
	global g_count
	if n == 1:
		print("Move sheet %d from %s to %s"%(n, a, c))
		g_count += 1
	else:
		hanoi(n-1,a,c,b)
		print("Move sheet %d from %s to %s"%(n, a, c))
		g_count += 1
		hanoi(n-1,b,a,c)

def main():
	if len(sys.argv) <2:
		print "Please give me a number as the number of pan."
		return
	num = sys.argv[1]
	hanoi(int(num), 'A', 'B', 'C')
	print "Total : %d"%g_count

if __name__=="__main__":
	main()
