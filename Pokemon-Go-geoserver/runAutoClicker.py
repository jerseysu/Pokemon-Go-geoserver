import os
import urllib2
import json
import time

def checkConnected():
	try:
		response = urllib2.urlopen("http://192.168.0.18/", timeout = 1)
		return json.load(response)
	except urllib2.URLError as e:
		print e.reason

def clickAction():
	os.system("./autoClicker -x1 457 -y1 442 -x2 463 -y2 489")

def start():
	print "Press 'SHIFT' to start AutoClick\nPress 'CONTROL' to pause AutoClick"
	if checkConnected() != None:
		clickAction()

start()