
import json
import os.path
import csv

servers_total=0
processor_count_total=0
processor_core_count_total=0

for x in range(1, 5):
	file_path = os.path.join('/home/michal/Downloads', 'hponeview_'+str(x))

	with open(file_path, "r") as json_data:
		i = json.load(json_data)
		for x in i['members']:
			print('Name:' + ' ' + x['name'] + ',' + ' ' + 'Pocessor Count:' + ' ' + str(x['processorCount']) + ',' + ' ' + 'Processor Core Count:' + ' ' + str(x['processorCoreCount']))
			servers_total += 1
			processor_count_total += x['processorCount']
			processor_core_count_total += x['processorCoreCount']


print('Total number of Servers:' + ' ' + str(servers_total))
print('Processor Count total:' + ' ' + str(processor_count_total))
print('Processor Core Count total:' + ' ' + str(processor_core_count_total))