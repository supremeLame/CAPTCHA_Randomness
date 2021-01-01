import requests
import hashlib

imageHashes = open("image_hases.txt","w")

counter = 1

while counter < 20000:

	response = requests.get(
		'ADD CAPTCHA URL',   
		headers={	
					'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:83.0) Gecko/20100101 Firefox/83.0',
					'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
					'Accept-Language': 'en-US,en;q=0.5',
					'Accept-Encoding': 'gzip, deflate',
					'Referer': 'ADD REFERRER IF REQUIRED',
					'Connection': 'keep-alive',
					'Cookie': 'ADD APP SESSION',
					'Upgrade-Insecure-Requests':'1',
					'Cache-Control': 'max-age=0'
	})

	print('HTTP Response status: '+str(response.status_code))
	print('SHA1 Hash value:\n')
	image = response.content
	hash_obj = hashlib.sha1(image)
	hexa_value = hash_obj.hexdigest()
	print('Print hashed values:')
	print(hexa_value)
	imageHashes.write(hexa_value+'\n')
	counter += 1
	print('||||||Print counter: ')
	print(str(counter))

imageHashes.close()
