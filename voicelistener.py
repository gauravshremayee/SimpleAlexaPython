#!/usr/bin/python
import os
import subprocess
import signal 
import atexit
import time
global child_pid
child_pid = proc.pid
def excel(): 
        proc = subprocess.Popen(["python3", "demo.py"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    
def internet(): 
        os.system("start chrome.exe")
        
def media(): 
        os.system("start wmplayer.exe")
        
        
        def stop(): print("Killing Child Process...")           os.kill(child_pid, signal.SIGTERM)

 def mainfunction(source): 
        audio = r.listen(source) 
        user = r.recognize(audio) 
        print(user) 
        if user == "Excel": 
                excel() 
        elif user == "Internet": 
                        internet() 
        elif user == "music": 
                media()

                
 if __name__ == "__main__": 
        r = sr.Recognizer() with sr.Microphone() as source: 
                while 1: 
                        mainfunction(source)
