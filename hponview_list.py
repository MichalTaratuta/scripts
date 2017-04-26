

from sys import argv
import json

#txt = open("/tmp/oneview1", "r").readlines()
#for x in range(4):

	with open("/tmp/hponeview", "r") as json_data:
		i = json.load(json_data)
		for x in i['members']:
			print('Name:' + ' ' + x['name'])
			print('Pocessor Count:' + ' ' + str(x['processorCount']))
			print('Processor Core Count:' + ' ' + str(x['processorCoreCount']))
			print('##########################')




