#!/usr/bin/env python3
#14.5.2019 "Sollers culture of a world"
#v2.1
#Andrey Shilikov
#Buuart
# =============== imports ================
import time, random, os, subprocess, requests
# ================ define ================
radioListFolder='/home/pi/sollersRadio/Music/'
killStartPause=1
pkillCommand='killall vlc'
vlcRunCommand='cvlc'
vlcPostfix=' --aout=alsa --alsa-audio-device="front:CARD=Device,DEV=0" &'

# ================= func =================
def slackSend(message):
	message=':sound: now playing '+str(message)+' station'
	rs='https://slack.com/api/chat.postMessage?token=xoxb-5072418900-634684771584-l8Zda9ToRQoYAg4WJ46dvnqC&channel=sollers_radio&text={0}&as_user=sollersmusic&pretty=1'.format(message)
	requests.request('POST',rs)
def bash_command(cmd):
    subprocess.Popen(['/bin/bash', '-c', cmd])
def radio_randnomiser():
	radioList=os.listdir(radioListFolder)
	radio=radioList[random.randint(0,len(radioList)-1)]
	#slackSend(radio)
	res = vlcRunCommand+' '+radioListFolder+radio+vlcPostfix
	return res
# =============== routine ================
bash_command(pkillCommand)
time.sleep(killStartPause)
bash_command(radio_randnomiser())
# =============== copyLeft ===============
# это просто радио =)
# запускается через крон
# 8uu4rt
