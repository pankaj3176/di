import requests
import argparse
import random

from datetime import datetime

# DI pipeline path: DI-URL/<path>/<operation>
url = 'https://vsystem.ingress.dh-ia37o5zq.dhaas-live.shoot.live.k8s-hana.ondemand.com/app/pipeline-modeler/openapi/service/teched2020/sha_performance/test'

# commandline parser
parser = argparse.ArgumentParser(description='Sending device data to SAP Data Intelligence.')
parser.add_argument('--cellid', type = int, help = "device identifier")
parser.add_argument('--user',  type = str ,help = "user")
parser.add_argument('--pwd',  type = str , help = "password")
args = parser.parse_args()

# data creation
key1 = 115.14126754671503
key2 = 217.31973375175826
# modified script so date set as 'times' (for video editing)
times = '2021-01-06 13:45:11'
data_json = {'TIMESTAMP': times, 'CELLID': args.cellid, 'KEY1':key1, 'KEY2':key2}
#data_json = {'TIMESTAMP': datetime.now().strftime('%Y-%m-%d %H:%M:%S'), 'CELLID': args.cellid, 'KEY1':key1, 'KEY2':key2}
data_text = ','.join([str(times),str(args.cellid),str(key1),str(key2)]) + '\n'
print("Send data: {}".format(data_text))
# send request
auth = ('default\\' + args.user,args.pwd)
headers = {'X-Requested-With': 'XMLHttpRequest'}
resp = requests.post(url, data=data_text, auth=auth, headers=headers)
resp = requests.post(url, json = data_json,auth=auth,headers=headers) #JSON

# response
print(resp)
