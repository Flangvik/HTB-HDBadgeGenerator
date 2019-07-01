#!/usr/bin/python3

import sys,getopt,urllib.request,urllib.parse,base64

banner = """
  _   _            _    _____ _          ____              _   _ _       _     ____        __   ____            _               ____                _             
 | | | | __ _  ___| | _|_   _| |__   ___| __ )  _____  __ | | | (_) __ _| |__ |  _ \  ___ / _| | __ )  __ _  __| | __ _  ___   / ___|_ __ ___  __ _| |_ ___  _ __ 
 | |_| |/ _` |/ __| |/ / | | | '_ \ / _ \  _ \ / _ \ \/ / | |_| | |/ _` | '_ \| | | |/ _ \ |_  |  _ \ / _` |/ _` |/ _` |/ _ \ | |   | '__/ _ \/ _` | __/ _ \| '__|
 |  _  | (_| | (__|   <  | | | | | |  __/ |_) | (_) >  <  |  _  | | (_| | | | | |_| |  __/  _| | |_) | (_| | (_| | (_| |  __/ | |___| | |  __/ (_| | || (_) | |   
 |_| |_|\__,_|\___|_|\_\ |_| |_| |_|\___|____/ \___/_/\_\ |_| |_|_|\__, |_| |_|____/ \___|_|   |____/ \__,_|\__,_|\__, |\___|  \____|_|  \___|\__,_|\__\___/|_|   
                                                                   |___/                                          |___/                                           

By Flangvik 
																   """
def generateHTB(htbId): 
        print(banner)
        htbUrl = "https://www.hackthebox.eu/badge/" + htbId

        signatureReq = urllib.request.urlopen(urllib.request.Request(htbUrl, headers={ 'User-Agent' : 'Mozilla/5.0 (Windows NT 6.1; Win64; x64)' }))
        signatureRaw =  signatureReq.read().decode('utf-8')
        signatureBase64 = signatureRaw.split('document.write(window.atob("')[1].split('"))')[0]

        signatureHTML = base64.b64decode(signatureBase64).decode('utf-8')

        signatureHTML = signatureHTML.replace('https://www.hackthebox.eu/images/screenshot.png',"assets/htb_crosshair.png")
        signatureHTML = signatureHTML.replace('_thumb.png',".png")
        signatureHTML = signatureHTML.replace('https://www.hackthebox.eu/images/star.png',"assets/htb_star.png")
        signatureHTML = signatureHTML.replace('url(https://www.hackthebox.eu/images/icon20.png); ',"url('assets/htb_logo.webp'); background-size: 20px;")

        signatureFile = open(htbId + '.html','w')
        signatureFile.write(signatureHTML)
        signatureFile.close()

        print("Check " + htbId + ".html!")
		

try:
    options, remainder = getopt.getopt(
        sys.argv[1:],
        '',
        ['htbid='])
except getopt.GetoptError as err:
    print ('HTBHDBadgeGenerator.py -htbid <HackTheBoxProfileID>')
    sys.exit(1)

for opt, arg in options:
    if opt == '--htbid':
        htbId = arg
		
generateHTB(htbId)




