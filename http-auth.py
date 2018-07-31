import requests
import json
import base64
import sys
import time

#Example usage: 
#python httprequest.py 149.56.111.22:5984/app/_design/example/index.html# 10k

host = sys.argv[1]
url = 'http://' + host
wordlist = sys.argv[2]

print '\n===== HTTP CONNECTOR ====='
print '----- HOST: ' + host + '\n'

count = 0
with open(wordlist) as f:
	for line in f:
		count = count + 1
		#loginHeaders = {'GET': '/HTTP/1.1', 'Host': host, 'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:43.0) Gecko/20100101 Firefox/43.0 Iceweasel/43.0.4', 'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8', 'Accept-Language': 'en-US,en;q=0.5', 'Accept-Encoding': 'gzip, deflate', 'Connection': 'close'}
		
		timeSent = int(round(time.time() * 1000))
		r = requests.get(url)
		timeReceived = int(round(time.time() * 1000))
		print 'COUNT: ' + str(count) + ' / RESP_CODE: ' + str(r.status_code) + ' /  RTT: ' + str(timeReceived - timeSent)