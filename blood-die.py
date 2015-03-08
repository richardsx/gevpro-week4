#!/usr/bin/env python
# Richards Zheng

import json
from collections import namedtuple

def main():
	# Open bestand en assign het aan variabele
	File = open("blood-die.json", "r")
	data = json.load(File)
	
	# Open bestand waar het resultaat naar toe wordt geschreven
	outputFile = open("identical.json", "w")
	
	# Namedtuple
	Country = namedtuple('Country', 'name, classification, blood, die')
	
	# Loop door de objecten, assign de naam, classificatie, bloed en sterven
	# Check of 'blood' gelijk is aan 'die'
	# Schrijf het object waar het gelijk aan elkaar is naar outputFile
	for line in data:
		CountryTuple = Country(line[0], line[1], line[2], line[3])
		blood = CountryTuple.blood.split()
		die = CountryTuple.die.split()
		[json.dump(line, outputFile) for blood in line if blood in die]
		
	File.close()
	outputFile.close()
	
main()
