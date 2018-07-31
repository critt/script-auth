import requests
import shutil
import time

preUrl = "http://s3.amazonaws.com/rdcms-himss/files/production/public/2015Conference/handouts/"
postUrl = ".pdf"

for n in range(0,401,1):
	response = requests.get(preUrl+str(n)+postUrl, stream=True)
	if response.status_code == 200:
		with open(str(n)+postUrl, 'wb') as out_file:
			shutil.copyfileobj(response.raw, out_file)
		del response
		print (str(n)+postUrl)
	time.sleep(5)