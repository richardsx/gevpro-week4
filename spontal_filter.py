#!/usr/bin/env python
# Richards Zheng

import sys
import xml.etree.ElementTree as ET



def main(argv):
	# Open bestand en assign het aan variabele
	tree = ET.parse(argv[1])
	root = tree.getroot()
	
	# Open bestand en assign het aan variabele
	tree = ET.parse(argv[1])
	root = tree.getroot()
	
	# Loop door de childs en check of de waarde van 
	# top en bottom hoger/lager dan end of start zijn
	# verwijder de hele child als dit zo is
	for child in root.findall('POINT'):
		bottom = float(child.find('BOTTOM_HZ').text)
		top = float(child.find('TOP_HZ').text)
		end = float(child.find('F0_END').text)
		start = float(child.find('F0_START').text)
		if end < bottom or start > top:
			root.remove(child)
			
	tree.write(argv[2])
			
main(sys.argv)

