

import pyaudio
import speech_recognition as sr
from pygame import mixer
import os
import random
import socket
import webbrowser
import subprocess
import glob
from time import localtime, strftime
import speekmodule
import datetime
import time

doss = os.getcwd()
i=0
n=0

INFO = '''
        +=======================================+
        |........... VIRTUAL INTELLIGENCE......|
        +---------------------------------------+
        |     Darpan Mehra | Varun Mishra      |
        +---------------------------------------+
        |..VIRTUAL INTELLIGENCE Mini Project...|
        +=======================================+
        |              OPTIONS:                 |
        |#hello/hi     #goodbye    #sleep mode  |
        |#your name    #jarvis     #what time   |
        |#asite.com    #next music #music       |
        |#pause music  #wifi       #thank you   |
        |#start/stop someapp                    |
        +=======================================+
        '''
print(INFO)

while (i<1):
    r = sr.Recognizer()
    with sr.Microphone() as source:
        audio = r.adjust_for_ambient_noise(source)
        n=(n+1)
        print("Say something!")
        audio = r.listen(source)
                                                   #(Google Speech Recognition)
    try:
        s = (r.recognize_google(audio))
        message = (s.lower())
        print (message)



        if ('goodbye') in message or ('buy') in message or ('bye') in message or ('good bye') in message or ('by') in message:
            rand = ['Goodbye Sir', 'Jarvis powering off in 3, 2, 1, 0']
            speekmodule.speek(rand,n,mixer)
            break

        if ('hello') in message or ('hi') in message or ('hallo') in message:
            rand = ['Welcome to AI project, at your service sir.']
            speekmodule.speek(rand,n,mixer)

        if ('thanks') in message or ('tanks') in message or ('thank you') in message:
            rand = ['You are welcome', 'no problem']
            speekmodule.speek(rand,n,mixer)

        if message == ('jarvis'):
            rand = ['Yes Sir?', 'What can I doo for you sir?']
            speekmodule.speek(rand,n,mixer)

        if  ('how are you') in message or ('and you') in message or ('are you okay') in message:
            rand = ['Fine thank you']
            speekmodule.speek(rand,n,mixer)



        if ('your name') in message or ('yurr name') in message or ('name') in message or ('neem') in message:
            rand = ['I am unnamed at the moment, I can still help you']
            speekmodule.speek(rand,n,mixer)

        if ('wi-fi') in message:
            REMOTE_SERVER = "www.google.com"
            speekmodule.wifi()
            rand = ['We are connected']
            speekmodule.speek(rand,n,mixer)

        if ('.com') in message or ('dotkom') in message :
            rand = ['Opening' + message]
            Chrome = ("C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s")
            speekmodule.speek(rand,n,mixer)
            webbrowser.get(Chrome).open('http://www.'+message)
            print ('')




        if message != ('start music') and ('start') in message:
            query = message
            stopwords = ['start']
            querywords = query.split()
            resultwords  = [word for word in querywords if word.lower() not in stopwords]
            result = ' '.join(resultwords)
            os.system('start ' + result)
            rand = [('starting '+result)]
            speekmodule.speek(rand,n,mixer)

        if message != ('stop music') and ('stop') in message:
            query = message
            stopwords = ['stop']
            querywords = query.split()
            resultwords  = [word for word in querywords if word.lower() not in stopwords]
            result = ' '.join(resultwords)
            os.system('taskkill /im ' + result + '.exe /f')
            rand = [('stopping '+result)]
            speekmodule.speek(rand,n,mixer)

        if ('install') in message:
            query = message
            stopwords = ['install']
            querywords = query.split()
            resultwords  = [word for word in querywords if word.lower() not in stopwords]
            result = ' '.join(resultwords)
            rand = [('installing '+result)]
            speekmodule.speek(rand,n,mixer)
            os.system('python -m pip install ' + result)


        if ('sleep mode') in message:
            rand = ['good night']
            speekmodule.speek(rand,n,mixer)
            os.system('rundll32.exe powrprof.dll,SetSuspendState 0,1,0')

        if ('music') in message:
            mus = random.choice(glob.glob(doss + "\\music" + "\\*.mp3"))
            os.system('chown -R user-id:group-id mus')
            os.system('start ' + mus)
            rand = ['start playing']
            speekmodule.speek(rand,n,mixer)



    # exceptions
    except sr.UnknownValueError:
        print("$could not understand audio")
    except sr.RequestError as e:
        print("Could not request results$; {0}".format(e))
